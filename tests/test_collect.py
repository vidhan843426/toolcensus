"""Introspection against local fixture servers: statuses, pagination, interop, allowlist on the wire."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from toolcensus.introspect.client import ALLOWED_METHODS
from toolcensus.introspect.collect import introspect_command, looks_like_config_error
from toolcensus.models import Status

from helpers import FIXTURES, fixture_cmd, fixture_record


async def test_normal_server() -> None:
    raw = await introspect_command(fixture_cmd("normal"), timeout_s=10)
    assert raw.status is Status.OK
    assert raw.result is not None
    assert [t["name"] for t in raw.result["tools"]] == ["read_file", "delete_file"]
    assert raw.result["initialize"]["serverInfo"]["name"] == "fixture-normal"
    assert raw.timings_ms["total"] > 0


@pytest.mark.parametrize(
    ("variant", "status"),
    [
        ("crash", Status.CRASHED),
        ("needs_config", Status.REQUIRES_CONFIGURATION),
        ("not_mcp", Status.NOT_MCP),
        ("banner", Status.OK),
    ],
)
async def test_status_classification(variant: str, status: Status) -> None:
    raw = await introspect_command(fixture_cmd(variant), timeout_s=10)
    assert raw.status is status, raw


async def test_hang_times_out_and_is_killed() -> None:
    raw = await introspect_command(fixture_cmd("hang"), timeout_s=1.5)
    assert raw.status is Status.TIMEOUT
    assert raw.exit_code is not None  # process was reaped
    assert raw.timings_ms["total"] < 10_000


async def test_cleanup_hook_always_runs() -> None:
    calls: list[str] = []

    async def cleanup() -> None:
        calls.append("x")

    await introspect_command(fixture_cmd("hang"), timeout_s=0.5, cleanup=cleanup)
    await introspect_command(fixture_cmd("normal"), timeout_s=5, cleanup=cleanup)
    assert calls == ["x", "x"]


async def test_pagination_followed() -> None:
    raw = await introspect_command(fixture_cmd("paginated"), timeout_s=10)
    assert raw.result is not None
    assert [t["name"] for t in raw.result["tools"]] == ["read_file", "delete_file"]


async def test_only_allowlisted_methods_reach_the_server(tmp_path: Path) -> None:
    log = tmp_path / "wire.jsonl"
    env = {"PATH": "/usr/bin:/bin", "FIXTURE_LOG": str(log)}
    raw = await introspect_command(fixture_cmd("spy"), env=env, timeout_s=10)
    assert raw.status is Status.OK
    assert raw.result is not None
    assert raw.result["prompts"] == [{"name": "summarize"}]
    assert raw.result["resource_templates"] == []  # -32601 tolerated
    received = [json.loads(line) for line in log.read_text().splitlines()]
    methods = {m["method"] for m in received if "method" in m}
    assert methods <= ALLOWED_METHODS
    assert "tools/call" not in methods
    # The sampling request was answered with an error, never served.
    replies = [m for m in received if m.get("id") == "srv-1"]
    assert replies and "error" in replies[0]


async def test_host_environment_is_not_forwarded(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("SUPER_SECRET_TOKEN", "hunter2")
    script = tmp_path / "envdump.py"
    script.write_text(
        "import os,sys,json\nsys.stderr.write(json.dumps(dict(os.environ)))\nsys.exit(1)\n"
    )
    raw = await introspect_command([sys.executable, "-I", str(script)], timeout_s=5)
    assert "hunter2" not in raw.stderr_tail
    assert "SUPER_SECRET_TOKEN" not in raw.stderr_tail


async def test_sdk_built_server_interop() -> None:
    cmd = [sys.executable, str(FIXTURES / "servers" / "sdk_server.py")]
    raw = await introspect_command(cmd, env={"PATH": "/usr/bin:/bin"}, timeout_s=20)
    assert raw.status is Status.OK, raw
    assert raw.result is not None
    [tool] = raw.result["tools"]
    assert tool["name"] == "add"
    assert tool["annotations"]["readOnlyHint"] is True


async def test_unicode_fixture_is_redacted_and_routed_privately(tmp_path: Path) -> None:
    from toolcensus.privacy import PrivateSink

    sink = PrivateSink(tmp_path / "private")
    rec = await fixture_record("unicode", private=sink)
    tool = next(t for t in rec.introspection.tools if t.name == "delete_file")
    assert tool.redacted
    assert "​" not in tool.definition["description"]
    assert tool.description_metrics.invisible_categories == {"zero_width": 1}
    assert sink.count == 1
    assert "​" in (tmp_path / "private" / "findings.jsonl").read_text()
    assert (tmp_path / "private" / ".gitignore").read_text() == "*\n"


def test_config_hint() -> None:
    assert looks_like_config_error("Please set the OPENAI_API_KEY")
    assert not looks_like_config_error("Segmentation fault")
    assert looks_like_config_error("PandaError: Cannot find config file `panda.config.ts`")
