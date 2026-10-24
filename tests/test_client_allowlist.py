"""Safety rule #1: only metadata methods can ever be sent."""

from __future__ import annotations

import asyncio
import json
import typing

import mcp.types as mcp_types
import pytest

from toolcensus.introspect.client import (
    ALLOWED_METHODS,
    ALLOWED_NOTIFICATIONS,
    ALLOWED_REQUESTS,
    ConnectionClosedError,
    MetadataClient,
    MethodNotAllowedError,
    ServerError,
    check_method,
)


class FakeWriter:
    def __init__(self) -> None:
        self.sent: list[dict] = []

    def write(self, data: bytes) -> None:
        self.sent.append(json.loads(data))

    async def drain(self) -> None:
        pass


class FakeReader:
    def __init__(self, lines: list[dict | str]) -> None:
        self.lines = [(json.dumps(x) if isinstance(x, dict) else x).encode() + b"\n" for x in lines]

    async def readline(self) -> bytes:
        return self.lines.pop(0) if self.lines else b""


def test_allowlist_is_exactly_the_metadata_methods() -> None:
    assert {
        "initialize",
        "tools/list",
        "prompts/list",
        "resources/list",
        "resources/templates/list",
    } == ALLOWED_REQUESTS
    assert {"notifications/initialized"} == ALLOWED_NOTIFICATIONS


async def test_tools_call_cannot_be_sent() -> None:
    writer = FakeWriter()
    client = MetadataClient(FakeReader([]), writer)
    with pytest.raises(MethodNotAllowedError):
        await client.request("tools/call", {"name": "delete_everything", "arguments": {}})
    # Even the low-level choke point refuses it.
    with pytest.raises(MethodNotAllowedError):
        await client._send({"jsonrpc": "2.0", "id": 99, "method": "tools/call", "params": {}})
    with pytest.raises(MethodNotAllowedError):
        await client.notify("tools/call")
    assert writer.sent == []
    assert not hasattr(client, "call_tool")


def _sdk_client_methods() -> set[str]:
    methods = set()
    for union in (mcp_types.ClientRequest, mcp_types.ClientNotification):
        for cls in typing.get_args(union):
            field = cls.model_fields["method"]
            methods.update(typing.get_args(field.annotation))
    return methods


@pytest.mark.parametrize("method", sorted(_sdk_client_methods() - ALLOWED_METHODS))
async def test_every_other_sdk_method_is_blocked(method: str) -> None:
    writer = FakeWriter()
    client = MetadataClient(FakeReader([]), writer)
    with pytest.raises(MethodNotAllowedError):
        await client.request(method)
    with pytest.raises(MethodNotAllowedError):
        await client.notify(method)
    assert writer.sent == []


def test_sdk_enumeration_actually_found_methods() -> None:
    found = _sdk_client_methods()
    assert {"tools/call", "resources/read", "prompts/get", "initialize"} <= found


@pytest.mark.parametrize("method", ["", "TOOLS/LIST", "tools/list ", "tools/call\n", "x"])
def test_lookalike_methods_rejected(method: str) -> None:
    with pytest.raises(MethodNotAllowedError):
        check_method(method, notification=False)


def test_request_and_notification_lists_are_not_interchangeable() -> None:
    with pytest.raises(MethodNotAllowedError):
        check_method("notifications/initialized", notification=False)
    with pytest.raises(MethodNotAllowedError):
        check_method("tools/list", notification=True)


async def test_choke_point_refuses_arbitrary_messages() -> None:
    client = MetadataClient(FakeReader([]), FakeWriter())
    with pytest.raises(MethodNotAllowedError):
        await client._send({"jsonrpc": "2.0", "params": {}})


async def test_server_requests_are_declined_not_served() -> None:
    writer = FakeWriter()
    reader = FakeReader(
        [
            "some banner text",
            {"jsonrpc": "2.0", "id": "s1", "method": "sampling/createMessage", "params": {}},
            {"jsonrpc": "2.0", "method": "notifications/message", "params": {}},
            {"jsonrpc": "2.0", "id": 999, "result": {}},
            {"jsonrpc": "2.0", "id": 1, "result": {"tools": [{"name": "a"}]}},
        ]
    )
    client = MetadataClient(reader, writer)
    tools = await client.list_all("tools/list")
    assert tools == [{"name": "a"}]
    assert writer.sent[0]["method"] == "tools/list"
    assert writer.sent[1] == {
        "jsonrpc": "2.0",
        "id": "s1",
        "error": {"code": -32601, "message": "not supported"},
    }
    assert client.noise_lines == 1


async def test_pagination_stops_on_cursor_loop() -> None:
    page = {"tools": [{"name": "x"}], "nextCursor": "same"}
    reader = FakeReader([{"jsonrpc": "2.0", "id": i, "result": page} for i in range(1, 5)])
    client = MetadataClient(reader, FakeWriter())
    assert len(await client.list_all("tools/list")) == 2


async def test_errors_and_eof() -> None:
    reader = FakeReader([{"jsonrpc": "2.0", "id": 1, "error": {"code": -32000, "message": "boom"}}])
    client = MetadataClient(reader, FakeWriter())
    with pytest.raises(ServerError):
        await client.list_all("tools/list")
    with pytest.raises(ConnectionClosedError):
        await MetadataClient(FakeReader([]), FakeWriter()).initialize()


async def test_noise_callback_supports_sync_and_async() -> None:
    seen: list[bytes] = []

    async def acb(line: bytes) -> None:
        seen.append(line)

    for cb in (seen.append, acb):
        reader = FakeReader(["noise", {"jsonrpc": "2.0", "id": 1, "result": {}}])
        await MetadataClient(reader, FakeWriter(), on_noise=cb).request("tools/list")
    assert seen == [b"noise", b"noise"]
    await asyncio.sleep(0)
