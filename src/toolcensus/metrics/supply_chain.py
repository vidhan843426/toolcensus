"""Package-level supply-chain signals from npm metadata (METHODOLOGY.md section 7.1)."""

from __future__ import annotations

import itertools
import re
import statistics
from collections.abc import Mapping
from datetime import datetime, timedelta
from typing import Any

from toolcensus.models import SupplyChainMetrics

INSTALL_SCRIPTS = ("preinstall", "install", "postinstall")

_PUBLIC_REPO = re.compile(
    r"^(?:git\+)?(?:https?|git|ssh)://(?:[^@/]+@)?(?:www\.)?"
    r"(github\.com|gitlab\.com|bitbucket\.org|codeberg\.org|git\.sr\.ht)[/:][^/\s]+/[^/\s]+"
    r"|^git@(github\.com|gitlab\.com|bitbucket\.org|codeberg\.org):[^/\s]+/[^/\s]+"
    r"|^(?:github|gitlab|bitbucket):[^/\s]+/[^/\s]+$"
    r"|^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$",
    re.IGNORECASE,
)


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def repository_url(version_doc: Mapping[str, Any]) -> str | None:
    repo = version_doc.get("repository")
    if isinstance(repo, dict):
        repo = repo.get("url")
    return repo.strip() if isinstance(repo, str) and repo.strip() else None


def release_times(packument: Mapping[str, Any]) -> dict[str, datetime]:
    times = packument.get("time", {})
    versions = packument.get("versions", {})
    return {
        v: parse_time(t)
        for v, t in times.items()
        if v not in ("created", "modified") and v in versions and isinstance(t, str)
    }


def install_scripts(version_doc: Mapping[str, Any]) -> list[str]:
    scripts = version_doc.get("scripts")
    scripts = scripts if isinstance(scripts, dict) else {}
    found = [s for s in INSTALL_SCRIPTS if s in scripts]
    # npm runs an implicit `node-gyp rebuild` for packages with a binding.gyp.
    if version_doc.get("gypfile") and "install" not in found:
        found.append("install(gypfile)")
    return found


def has_provenance(version_doc: Mapping[str, Any]) -> bool:
    dist = version_doc.get("dist")
    att = dist.get("attestations") if isinstance(dist, dict) else None
    return isinstance(att, dict) and isinstance(att.get("provenance"), dict)


def supply_chain_metrics(
    packument: Mapping[str, Any], version: str, *, as_of: datetime, registry_listed: bool
) -> SupplyChainMetrics:
    doc = packument["versions"][version]
    times = sorted(t for t in release_times(packument).values() if t <= as_of)
    gaps = [(b - a).total_seconds() / 86400 for a, b in itertools.pairwise(times)]
    maintainers = doc.get("maintainers") or packument.get("maintainers") or []
    deps = doc.get("dependencies")
    repo = repository_url(doc)
    scripts = install_scripts(doc)
    return SupplyChainMetrics(
        has_provenance=has_provenance(doc),
        has_install_scripts=bool(scripts),
        install_scripts=scripts,
        direct_dependency_count=len(deps) if isinstance(deps, dict) else 0,
        maintainer_count=len(maintainers) if isinstance(maintainers, list) else 0,
        releases_last_90d=sum(1 for t in times if t > as_of - timedelta(days=90)),
        median_days_between_releases=round(statistics.median(gaps), 2) if gaps else None,
        repo_linked=bool(repo and _PUBLIC_REPO.search(repo)),
        registry_listed=registry_listed,
    )
