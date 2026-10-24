"""PyPI JSON API (phase 2: Python servers launched with ``uvx`` / ``pipx``)."""

from __future__ import annotations

from typing import Any

from toolcensus.discovery.http import CachedHttp

PYPI = "https://pypi.org/pypi"


async def project_metadata(
    http: CachedHttp, name: str, version: str | None = None
) -> dict[str, Any]:
    url = f"{PYPI}/{name}/{version}/json" if version else f"{PYPI}/{name}/json"
    data = await http.get_json(url)
    return data if isinstance(data, dict) else {}


def has_console_scripts_hint(meta: dict[str, Any]) -> bool:
    """PyPI JSON does not expose entry points; we can only check for MCP keywords/classifiers."""
    info = meta.get("info") or {}
    blob = " ".join([str(info.get("keywords") or ""), *map(str, info.get("classifiers") or [])])
    return "mcp" in blob.lower()
