"""Allowlisted, metadata-only MCP client over newline-delimited JSON-RPC (stdio transport).

This is deliberately *not* a general MCP client. Every outgoing message passes through
:meth:`MetadataClient._send`, which refuses any method outside :data:`ALLOWED_METHODS`.
There is no code path that can emit ``tools/call``, ``resources/read``, ``prompts/get``,
sampling responses, or anything else that would execute server functionality.

Why not the official SDK's ``ClientSession``? See docs/verification-notes.md: the 2.x SDK
filters and re-validates tool listings (e.g. drops tools under the 2026-07-28 header rules),
which would distort what we measure. We need the raw definitions exactly as sent.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Awaitable, Callable
from typing import Any, Protocol

ALLOWED_REQUESTS: frozenset[str] = frozenset(
    {
        "initialize",
        "tools/list",
        "prompts/list",
        "resources/list",
        "resources/templates/list",
    }
)
ALLOWED_NOTIFICATIONS: frozenset[str] = frozenset({"notifications/initialized"})
ALLOWED_METHODS: frozenset[str] = ALLOWED_REQUESTS | ALLOWED_NOTIFICATIONS

#: Protocol version we offer. Servers negotiate down if needed.
CLIENT_PROTOCOL_VERSION = "2025-11-25"

METHOD_NOT_FOUND = -32601

_LIST_KEYS = {
    "tools/list": "tools",
    "prompts/list": "prompts",
    "resources/list": "resources",
    "resources/templates/list": "resourceTemplates",
}


class MethodNotAllowedError(RuntimeError):
    """Raised before anything is written when a non-allowlisted method is attempted."""


class ConnectionClosedError(RuntimeError):
    """The server closed stdout before answering."""


class ServerError(RuntimeError):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(f"server error {code}: {message}")
        self.code = code
        self.message = message


class LineReader(Protocol):
    async def readline(self) -> bytes: ...


class LineWriter(Protocol):
    def write(self, data: bytes) -> None: ...

    async def drain(self) -> None: ...


def check_method(method: str, *, notification: bool) -> None:
    allowed = ALLOWED_NOTIFICATIONS if notification else ALLOWED_REQUESTS
    if method not in allowed:
        kind = "notification" if notification else "request"
        raise MethodNotAllowedError(f"{kind} {method!r} is not in the metadata-only allowlist")


class MetadataClient:
    def __init__(
        self,
        reader: LineReader,
        writer: LineWriter,
        *,
        client_name: str = "toolcensus",
        client_version: str = "0",
        max_pages: int = 100,
        on_noise: Callable[[bytes], Awaitable[None] | None] | None = None,
    ) -> None:
        self._reader = reader
        self._writer = writer
        self._next_id = 1
        self._client_info = {"name": client_name, "version": client_version}
        self._max_pages = max_pages
        self._on_noise = on_noise
        #: Number of JSON-RPC messages received; 0 means the peer never spoke MCP.
        self.messages_received = 0
        self.noise_lines = 0

    # -- the single choke point ---------------------------------------------------------------

    async def _send(self, message: dict[str, Any]) -> None:
        method = message.get("method")
        if method is not None:
            check_method(str(method), notification="id" not in message)
        elif "id" not in message or not ("result" in message or "error" in message):
            raise MethodNotAllowedError(
                "refusing to send a message that is neither allowed nor a reply"
            )
        self._writer.write(json.dumps(message, separators=(",", ":")).encode() + b"\n")
        await self._writer.drain()

    # -- primitives ---------------------------------------------------------------------------

    async def request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        check_method(method, notification=False)
        req_id = self._next_id
        self._next_id += 1
        msg: dict[str, Any] = {"jsonrpc": "2.0", "id": req_id, "method": method}
        if params is not None:
            msg["params"] = params
        await self._send(msg)
        while True:
            incoming = await self._read_message()
            if "method" in incoming:
                if "id" in incoming:
                    # Server-initiated request (sampling, roots, elicitation, ping...). We do not
                    # provide any client capability, so we decline every one of them.
                    await self._send(
                        {
                            "jsonrpc": "2.0",
                            "id": incoming["id"],
                            "error": {"code": METHOD_NOT_FOUND, "message": "not supported"},
                        }
                    )
                continue  # notifications (logging, list_changed...) are ignored
            if incoming.get("id") != req_id:
                continue
            if "error" in incoming:
                err = incoming["error"] if isinstance(incoming["error"], dict) else {}
                raise ServerError(int(err.get("code", 0)), str(err.get("message", "")))
            result = incoming.get("result")
            return result if isinstance(result, dict) else {}

    async def notify(self, method: str, params: dict[str, Any] | None = None) -> None:
        check_method(method, notification=True)
        msg: dict[str, Any] = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            msg["params"] = params
        await self._send(msg)

    async def _read_message(self) -> dict[str, Any]:
        while True:
            line = await self._reader.readline()
            if not line:
                raise ConnectionClosedError("server closed the connection")
            stripped = line.strip()
            if not stripped:
                continue
            try:
                obj = json.loads(stripped)
            except ValueError:
                obj = None
            if isinstance(obj, dict) and obj.get("jsonrpc") == "2.0":
                self.messages_received += 1
                return obj
            # Log lines or banners written to stdout by some servers.
            self.noise_lines += 1
            if self._on_noise is not None:
                maybe = self._on_noise(stripped)
                if maybe is not None:
                    await maybe

    # -- high level ---------------------------------------------------------------------------

    async def initialize(self) -> dict[str, Any]:
        result = await self.request(
            "initialize",
            {
                "protocolVersion": CLIENT_PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": self._client_info,
            },
        )
        await self.notify("notifications/initialized")
        return result

    async def list_all(self, method: str) -> list[dict[str, Any]]:
        """Follow ``nextCursor`` pagination. Stops on repeated cursors or after ``max_pages``."""
        key = _LIST_KEYS[method]
        items: list[dict[str, Any]] = []
        cursor: str | None = None
        seen: set[str] = set()
        for _ in range(self._max_pages):
            result = await self.request(method, {"cursor": cursor} if cursor else None)
            page = result.get(key, [])
            if isinstance(page, list):
                items.extend(item for item in page if isinstance(item, dict))
            nxt = result.get("nextCursor")
            if not isinstance(nxt, str) or not nxt or nxt in seen:
                break
            seen.add(nxt)
            cursor = nxt
        return items

    async def list_optional(self, method: str) -> list[dict[str, Any]]:
        try:
            return await self.list_all(method)
        except ServerError as exc:
            if exc.code == METHOD_NOT_FOUND:
                return []
            raise


async def collect_metadata(client: MetadataClient) -> dict[str, Any]:
    """Run the full metadata handshake and return the raw results."""
    loop = asyncio.get_running_loop()
    timings: dict[str, float] = {}

    t0 = loop.time()
    init = await client.initialize()
    timings["initialize"] = (loop.time() - t0) * 1000
    caps = init.get("capabilities") if isinstance(init.get("capabilities"), dict) else {}
    assert isinstance(caps, dict)

    t0 = loop.time()
    tools = await client.list_optional("tools/list")
    timings["tools_list"] = (loop.time() - t0) * 1000

    prompts: list[dict[str, Any]] = []
    resources: list[dict[str, Any]] = []
    templates: list[dict[str, Any]] = []
    if "prompts" in caps:
        prompts = await client.list_optional("prompts/list")
    if "resources" in caps:
        resources = await client.list_optional("resources/list")
        templates = await client.list_optional("resources/templates/list")

    return {
        "initialize": init,
        "tools": tools,
        "prompts": prompts,
        "resources": resources,
        "resource_templates": templates,
        "timings_ms": timings,
    }
