"""Population selection (METHODOLOGY.md section 5.1). The rule text is stored in every snapshot."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from toolcensus.discovery import npm
from toolcensus.discovery.http import CachedHttp, HttpError
from toolcensus.discovery.registry import RegistryPackage, registry_npm_index
from toolcensus.models import ExcludedEntry, Population, PopulationEntry

SELECTION_RULE = (
    "Union of (a) npm stdio packages listed in the official MCP Registry (latest versions) and "
    "(b) npm search results for keywords mcp-server / mcp / modelcontextprotocol and the free text "
    "'mcp server'. A candidate is "
    "kept if its latest version declares a `bin` and (is registry-listed OR depends on "
    "@modelcontextprotocol/sdk or @modelcontextprotocol/server OR has keyword `mcp-server`), its name does not match the "
    "library pattern (sdk|client|types|framework|inspector|proxy|gateway|bridge|cli-core), and it "
    "is not in exclusions.yaml. Ranked by npm weekly downloads; top N kept."
)

NO_REGISTRY_NOTE = (
    " [Source (a) DISABLED for this run (--no-registry): npm search only; registry_listed is"
    " false for every entry. Not comparable with full weekly populations.]"
)

_LIBRARY_NAME = re.compile(
    r"(?:^|[-/_.])(sdk|client|types|framework|inspector|proxy|gateway|bridge|cli-core)(?:$|[-_.])",
    re.IGNORECASE,
)


@dataclass
class Candidate:
    name: str
    weekly_downloads: int = 0
    sources: set[str] = field(default_factory=set)
    keywords: set[str] = field(default_factory=set)
    registry: RegistryPackage | None = None


def load_exclusions(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return {
        str(e["name"]): str(e.get("reason", "manual exclusion")) for e in data.get("exclude", [])
    }


def library_name(name: str) -> bool:
    return bool(_LIBRARY_NAME.search(name))


def classify(
    cand: Candidate, version_doc: dict[str, Any], exclusions: dict[str, str]
) -> str | None:
    """Return an exclusion reason, or None if the candidate is an MCP server."""
    if cand.name in exclusions:
        return f"exclusions.yaml: {exclusions[cand.name]}"
    if not npm.bin_entries(version_doc):
        return "no bin entry (not launchable as a stdio server)"
    if library_name(cand.name) and cand.registry is None:
        return "name matches library pattern"
    if (
        cand.registry is None
        and not npm.depends_on_sdk(version_doc)
        and "mcp-server" not in cand.keywords
    ):
        return (
            "no MCP server signal (not registry-listed, no SDK dependency, no mcp-server keyword)"
        )
    return None


async def gather_candidates(
    http: CachedHttp, *, search_limit: int, include_registry: bool = True
) -> dict[str, Candidate]:
    cands: dict[str, Candidate] = {}
    registry = await registry_npm_index(http) if include_registry else {}
    for name, reg in registry.items():
        cands[name] = Candidate(name, sources={"mcp_registry"}, registry=reg)
    for query in npm.SEARCH_QUERIES:
        for obj in await npm.search(http, query, limit=search_limit):
            pkg = obj.get("package") or {}
            pkg_name = str(pkg.get("name") or "")
            if not pkg_name:
                continue
            c = cands.setdefault(pkg_name, Candidate(pkg_name))
            c.sources.add("npm_search")
            c.keywords.update(str(k).lower() for k in pkg.get("keywords") or [])
            c.weekly_downloads = max(
                c.weekly_downloads, int((obj.get("downloads") or {}).get("weekly", 0))
            )
    missing = [n for n, c in cands.items() if "npm_search" not in c.sources]
    for name, dl in (await npm.weekly_downloads(http, missing)).items():
        cands[name].weekly_downloads = dl
    return cands


async def select_population(
    http: CachedHttp,
    *,
    week: str,
    top_n: int,
    exclusions_path: Path = Path("exclusions.yaml"),
    search_limit: int = 1000,
    include_registry: bool = True,
) -> Population:
    exclusions = load_exclusions(exclusions_path)
    cands = sorted(
        (
            await gather_candidates(
                http, search_limit=search_limit, include_registry=include_registry
            )
        ).values(),
        key=lambda c: (-c.weekly_downloads, c.name),
    )
    kept: list[PopulationEntry] = []
    excluded: list[ExcludedEntry] = []
    for cand in cands:
        if len(kept) >= top_n:
            break
        try:
            pack = await npm.packument(http, cand.name)
        except HttpError as exc:
            excluded.append(
                ExcludedEntry(name=cand.name, reason=f"metadata unavailable ({exc.status})")
            )
            continue
        version = npm.latest_version(pack)
        reason = classify(cand, pack["versions"].get(version, {}), exclusions)
        if reason:
            excluded.append(ExcludedEntry(name=cand.name, reason=reason))
            continue
        kept.append(
            PopulationEntry(
                name=cand.name,
                version=version,
                weekly_downloads=cand.weekly_downloads,
                registry_listed=cand.registry is not None,
                registry_name=cand.registry.registry_name if cand.registry else None,
                sources=sorted(cand.sources),
            )
        )
    rule = SELECTION_RULE if include_registry else SELECTION_RULE + NO_REGISTRY_NOTE
    return Population(week=week, selection_rule=rule, top_n=top_n, packages=kept, excluded=excluded)
