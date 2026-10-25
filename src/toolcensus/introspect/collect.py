"""Launch a server command, run the metadata handshake, and classify the outcome.

The command is whatever the sandbox runner produced (normally ``docker run ... --network none``).
This module never decides *how* to isolate a server; it only talks to it.
"""

from __future__ import annotations

import asyncio
import contextlib
import re
from collections.abc import Awaitable, Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

from toolcensus import __version__
from toolcensus.introspect.client import (
    ConnectionClosedError,
    MetadataClient,
    ServerError,
    collect_metadata,
)
from toolcensus.models import Status

#: stdout lines can carry very large tool lists.
_STREAM_LIMIT = 16 * 1024 * 1024
_STDERR_TAIL = 4096

_CONFIG_HINT = re.compile(
    r"api[_ -]?key|access[_ -]?token|\btoken\b|environment variable|env(?:ironment)? var|"
    r"is required|must be (?:set|provided)|missing required|not set|credential|"
    r"unauthori[sz]ed|no such file or directory.*config|"
    r"cannot find (?:a |the )?config|config(?:uration)? file (?:not found|missing|is required)",
    re.IGNORECASE,
)


@dataclass
class RawIntrospection:
    status: Status
    result: dict[str, Any] | None = None
    error: str | None = None
    stderr_tail: str = ""
    exit_code: int | None = None
    timings_ms: dict[str, float] = field(default_factory=dict)


def looks_like_config_error(text: str) -> bool:
    return bool(_CONFIG_HINT.search(text))


class _Tail:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.buf = bytearray()

    def add(self, chunk: bytes) -> None:
        self.buf.extend(chunk)
        if len(self.buf) > self.limit:
            del self.buf[: len(self.buf) - self.limit]

    def text(self) -> str:
        return self.buf.decode("utf-8", "replace")


async def _drain(stream: asyncio.StreamReader | None, tail: _Tail) -> None:
    if stream is None:
        return
    while chunk := await stream.read(4096):
        tail.add(chunk)


def _classify_failure(exc: BaseException, client: MetadataClient, stderr: str) -> Status:
    if client.messages_received == 0 and looks_like_config_error(stderr):
        return Status.REQUIRES_CONFIGURATION
    if isinstance(exc, ServerError):
        return (
            Status.REQUIRES_CONFIGURATION
            if looks_like_config_error(exc.message)
            else Status.CRASHED
        )
    if client.messages_received == 0 and client.noise_lines > 0 and not stderr.strip():
        return Status.NOT_MCP
    return Status.CRASHED


async def introspect_command(
    command: Sequence[str],
    *,
    env: Mapping[str, str] | None = None,
    timeout_s: float = 60.0,
    cleanup: Callable[[], Awaitable[None]] | None = None,
) -> RawIntrospection:
    """Run ``command`` as an MCP stdio server and collect its advertised metadata.

    ``env`` is the environment of the *launching* process. It defaults to an almost-empty
    environment so host variables (and any secrets in them) never reach a server.
    """
    proc = await asyncio.create_subprocess_exec(
        *command,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=dict(env) if env is not None else minimal_env(),
        limit=_STREAM_LIMIT,
    )
    assert proc.stdin is not None and proc.stdout is not None
    tail = _Tail(_STDERR_TAIL)
    stderr_task = asyncio.create_task(_drain(proc.stderr, tail))
    client = MetadataClient(proc.stdout, proc.stdin, client_version=__version__)
    loop = asyncio.get_running_loop()
    started = loop.time()

    raw: RawIntrospection
    try:
        result = await asyncio.wait_for(collect_metadata(client), timeout=timeout_s)
        raw = RawIntrospection(Status.OK, result=result, timings_ms=dict(result["timings_ms"]))
    except TimeoutError:
        status = (
            Status.NOT_MCP
            if client.messages_received == 0 and client.noise_lines
            else Status.TIMEOUT
        )
        raw = RawIntrospection(status, error=f"no complete answer within {timeout_s:.0f}s")
    except (ConnectionClosedError, ServerError, BrokenPipeError, ConnectionResetError) as exc:
        with contextlib.suppress(TimeoutError):
            await asyncio.wait_for(stderr_task, timeout=2)
        raw = RawIntrospection(
            _classify_failure(exc, client, tail.text()),
            error=_short(str(exc) or type(exc).__name__),
        )
    finally:
        await _shutdown(proc)
        if cleanup is not None:
            with contextlib.suppress(Exception):
                await cleanup()
        stderr_task.cancel()
        with contextlib.suppress(asyncio.CancelledError, Exception):
            await stderr_task

    raw.stderr_tail = tail.text()
    raw.exit_code = proc.returncode
    raw.timings_ms["total"] = (loop.time() - started) * 1000
    return raw


async def _shutdown(proc: asyncio.subprocess.Process) -> None:
    if proc.returncode is not None:
        return
    if proc.stdin is not None:
        with contextlib.suppress(Exception):
            proc.stdin.close()
    try:
        await asyncio.wait_for(proc.wait(), timeout=2)
    except TimeoutError:
        with contextlib.suppress(ProcessLookupError):
            proc.kill()
        with contextlib.suppress(Exception):
            await asyncio.wait_for(proc.wait(), timeout=5)


def minimal_env() -> dict[str, str]:
    import os

    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"}


def _short(text: str, limit: int = 300) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "…"
