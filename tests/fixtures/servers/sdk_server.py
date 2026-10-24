"""A server built with the official MCP Python SDK, to prove interoperability."""

from mcp.server import MCPServer
from mcp.types import ToolAnnotations

server = MCPServer("sdk-fixture", version="0.0.1")


@server.tool(annotations=ToolAnnotations(read_only_hint=True))
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


if __name__ == "__main__":
    server.run("stdio")
