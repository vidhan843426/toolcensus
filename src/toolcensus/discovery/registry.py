"""Official MCP Registry (https://registry.modelcontextprotocol.io), API v0.1.

Verified 2026-10-24: ``GET /v0.1/servers?version=latest&limit=N&cursor=C`` returns
``{"servers": [{"server": {...}, "_meta": {...}}], "metadata": {"nextCursor": ..., "count": N}}``.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any

from toolcensus.discovery.http import CachedHttp

REGISTRY_BASE = "https://registry.modelcontextprotocol.io"


@dataclass(frozen=True)
class RegistryPackage:
    registry_name: str
    package: str
    version: str | None
    required_env: tuple[str, ...]


@dataclass(frozen=True)
class RegistryRemote:
    registry_name: str
    url: str
    transport: str


async def iter_servers(
    http: CachedHttp, *, page_size: int = 100, max_pages: int = 500
) -> AsyncIterator[dict[str, Any]]:
    cursor: str | None = None
    for _ in range(max_pages):
        data = await http.get_json(
            f"{REGISTRY_BASE}/v0.1/servers",
            {"version": "latest", "limit": page_size, "cursor": cursor},
        )
        for entry in data.get("servers", []):
            server = entry.get("server")
            if isinstance(server, dict):
                yield server
        cursor = (data.get("metadata") or {}).get("nextCursor")
        if not cursor:
            return


def npm_stdio_packages(server: dict[str, Any]) -> list[RegistryPackage]:
    out = []
    for pkg in server.get("packages") or []:
        if pkg.get("registryType") != "npm":
            continue
        transport = (pkg.get("transport") or {}).get("type", "stdio")
        if transport != "stdio" or not pkg.get("identifier"):
            continue
        env = tuple(
            str(v["name"])
            for v in pkg.get("environmentVariables") or []
            if isinstance(v, dict) and v.get("isRequired") and v.get("name")
        )
        out.append(
            RegistryPackage(str(server["name"]), str(pkg["identifier"]), pkg.get("version"), env)
        )
    return out


def remotes(server: dict[str, Any]) -> list[RegistryRemote]:
    return [
        RegistryRemote(str(server["name"]), str(r["url"]), str(r.get("type", "")))
        for r in server.get("remotes") or []
        if isinstance(r, dict) and str(r.get("url", "")).startswith("https://")
    ]


async def registry_npm_index(http: CachedHttp) -> dict[str, RegistryPackage]:
    """npm package name -> registry entry, for every npm stdio package in the registry."""
    index: dict[str, RegistryPackage] = {}
    async for server in iter_servers(http):
        for pkg in npm_stdio_packages(server):
            index.setdefault(pkg.package, pkg)
    return index
