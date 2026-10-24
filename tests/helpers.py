from __future__ import annotations

import sys
from pathlib import Path

from toolcensus.introspect.build import build_introspection, summarize
from toolcensus.introspect.collect import introspect_command
from toolcensus.models import ObservedVia, PackageInfo, ServerRecord, Status, SupplyChainMetrics
from toolcensus.privacy import NullSink, PrivateSink

FIXTURES = Path(__file__).parent / "fixtures"
SERVER = FIXTURES / "servers" / "fixture_server.py"


def fixture_cmd(variant: str) -> list[str]:
    return [sys.executable, "-I", str(SERVER), variant]


def supply(**kw: object) -> SupplyChainMetrics:
    base: dict[str, object] = dict(
        has_provenance=True,
        has_install_scripts=False,
        direct_dependency_count=2,
        maintainer_count=1,
        releases_last_90d=3,
        median_days_between_releases=7.0,
        repo_linked=True,
        registry_listed=True,
    )
    base.update(kw)
    return SupplyChainMetrics.model_validate(base)


async def fixture_record(
    variant: str,
    *,
    package: str = "fixture-pkg",
    version: str = "1.0.0",
    private: PrivateSink | None = None,
    downloads: int = 100,
    **supply_kw: object,
) -> ServerRecord:
    raw = await introspect_command(fixture_cmd(variant), timeout_s=10)
    intro = build_introspection(
        raw, launch=None, package=package, version=version, private=private or NullSink()
    )
    return ServerRecord(
        observed_via=ObservedVia.WEEKLY_SCAN,
        package=PackageInfo(name=package, version=version, weekly_downloads=downloads),
        supply_chain=supply(**supply_kw),
        introspection=intro,
        summary=summarize(intro.tools) if intro.status is Status.OK else None,
    )
