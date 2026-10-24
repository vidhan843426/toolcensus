"""npm registry + downloads API (official public endpoints)."""

from __future__ import annotations

import asyncio
from typing import Any
from urllib.parse import quote

from toolcensus.discovery.http import CachedHttp, HttpError

NPM_REGISTRY = "https://registry.npmjs.org"
NPM_API = "https://api.npmjs.org"
#: Official MCP TypeScript SDK packages a server can depend on (verified on npm 2026-10-24):
#: 1.x shipped as one package; 2.x splits the server side into @modelcontextprotocol/server.
MCP_SDK_PACKAGES = ("@modelcontextprotocol/sdk", "@modelcontextprotocol/server")
#: Keyword queries plus one free-text query: several official reference servers
#: (e.g. @modelcontextprotocol/server-filesystem) declare no npm keywords at all.
SEARCH_QUERIES = (
    "keywords:mcp-server",
    "keywords:mcp",
    "keywords:modelcontextprotocol",
    "mcp server",
)


def encode_name(name: str) -> str:
    return quote(name, safe="@")


async def packument(http: CachedHttp, name: str) -> dict[str, Any]:
    data = await http.get_json(f"{NPM_REGISTRY}/{encode_name(name)}")
    if not isinstance(data, dict) or "versions" not in data:
        raise HttpError(name, 404)
    return data


#: The bulk downloads endpoint accepts up to 128 *unscoped* names per request.
BULK_LIMIT = 128


async def weekly_downloads(http: CachedHttp, names: list[str]) -> dict[str, int]:
    async def one(name: str) -> tuple[str, int]:
        status, data = await http.get_json_status(
            f"{NPM_API}/downloads/point/last-week/{encode_name(name)}"
        )
        ok = status == 200 and isinstance(data, dict)
        return name, int(data.get("downloads", 0)) if ok else 0

    async def bulk(chunk: list[str]) -> dict[str, int]:
        status, data = await http.get_json_status(
            f"{NPM_API}/downloads/point/last-week/{','.join(chunk)}"
        )
        data = data if status == 200 and isinstance(data, dict) else {}
        return {n: int((data.get(n) or {}).get("downloads", 0)) for n in chunk}

    scoped = [n for n in names if n.startswith("@")]
    unscoped = [n for n in names if not n.startswith("@")]
    out: dict[str, int] = {}
    if len(unscoped) == 1:
        scoped.append(unscoped.pop())
    for i in range(0, len(unscoped), BULK_LIMIT):
        out.update(await bulk(unscoped[i : i + BULK_LIMIT]))
    out.update(await asyncio.gather(*(one(n) for n in scoped)))
    return out


async def search(http: CachedHttp, text: str, *, limit: int = 1000) -> list[dict[str, Any]]:
    """npm search results (each has ``package`` and ``downloads.weekly``)."""
    out: list[dict[str, Any]] = []
    size = 250
    for offset in range(0, limit, size):
        data = await http.get_json(
            f"{NPM_REGISTRY}/-/v1/search", {"text": text, "size": size, "from": offset}
        )
        objects = data.get("objects", [])
        out.extend(o for o in objects if isinstance(o, dict))
        if len(objects) < size:
            break
    return out


def latest_version(pack: dict[str, Any]) -> str:
    return str(pack.get("dist-tags", {}).get("latest") or sorted(pack["versions"])[-1])


def bin_entries(version_doc: dict[str, Any]) -> dict[str, str]:
    b = version_doc.get("bin")
    if isinstance(b, str):
        return {str(version_doc.get("name", "")).split("/")[-1]: b}
    return {str(k): str(v) for k, v in b.items()} if isinstance(b, dict) else {}


def depends_on_sdk(version_doc: dict[str, Any]) -> bool:
    deps = version_doc.get("dependencies") or {}
    return isinstance(deps, dict) and any(p in deps for p in MCP_SDK_PACKAGES)
