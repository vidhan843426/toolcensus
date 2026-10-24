"""discover -> metadata -> sandbox image -> introspect -> normalize/hash -> metrics -> store -> diff."""

from __future__ import annotations

import asyncio
import itertools
import uuid
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from toolcensus.config import Settings
from toolcensus.diff.engine import diff_servers
from toolcensus.discovery import npm
from toolcensus.discovery.http import CachedHttp, HttpError
from toolcensus.discovery.registry import RegistryPackage
from toolcensus.introspect.build import build_introspection, summarize
from toolcensus.introspect.collect import RawIntrospection, introspect_command
from toolcensus.metrics.supply_chain import (
    parse_time,
    release_times,
    repository_url,
    supply_chain_metrics,
)
from toolcensus.models import (
    ChangeRecord,
    Introspection,
    LaunchInfo,
    ObservedVia,
    PackageInfo,
    Population,
    ServerRecord,
    Status,
)
from toolcensus.privacy import PrivateSink
from toolcensus.sandbox.runner import (
    InstallFailedError,
    SandboxError,
    SandboxRunner,
    load_overrides,
    resolve_launch,
)
from toolcensus.storage.snapshots import SnapshotStore, append_jsonl


@dataclass
class ScanContext:
    http: CachedHttp
    runner: SandboxRunner
    settings: Settings
    private: PrivateSink
    overrides: dict[str, dict[str, Any]] = field(default_factory=dict)
    registry: dict[str, RegistryPackage] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        http: CachedHttp,
        runner: SandboxRunner,
        settings: Settings,
        *,
        overrides_path: Path = Path("launch_overrides.yaml"),
    ) -> ScanContext:
        return cls(
            http=http,
            runner=runner,
            settings=settings,
            private=PrivateSink(settings.private_dir),
            overrides=load_overrides(overrides_path),
        )


async def introspect_version(
    ctx: ScanContext,
    packument: dict[str, Any],
    version: str,
    *,
    observed_via: ObservedVia,
    weekly_downloads: int | None = None,
    as_of: datetime | None = None,
) -> ServerRecord:
    name = str(packument["name"])
    doc = packument["versions"][version]
    published = packument.get("time", {}).get(version)
    published_at = parse_time(published) if isinstance(published, str) else None
    reg = ctx.registry.get(name)
    package = PackageInfo(
        name=name,
        version=version,
        published_at=published_at,
        weekly_downloads=weekly_downloads,
        registry_name=reg.registry_name if reg else None,
        repository_url=repository_url(doc),
    )
    supply = supply_chain_metrics(
        packument,
        version,
        as_of=as_of or published_at or datetime.now(UTC),
        registry_listed=reg is not None,
    )

    def record(intro: Introspection) -> ServerRecord:
        return ServerRecord(
            observed_via=observed_via,
            package=package,
            supply_chain=supply,
            introspection=intro,
            summary=summarize(intro.tools) if intro.status is Status.OK else None,
        )

    try:
        spec = resolve_launch(
            doc, overrides=ctx.overrides, required_env=reg.required_env if reg else ()
        )
    except SandboxError as exc:
        return record(Introspection(status=Status.NOT_MCP, error=str(exc)))
    launch = LaunchInfo(
        source=spec.source,
        command=["node", f"node_modules/{spec.package}/{spec.bin_path}", *spec.args],
        placeholder_env=sorted(spec.env),
        install_scripts_ran=spec.allow_install_scripts,
    )
    try:
        image = await ctx.runner.prepare(spec)
    except InstallFailedError as exc:
        return record(
            Introspection(status=Status.INSTALL_FAILED, error=str(exc)[-300:], launch=launch)
        )

    container = f"toolcensus-{uuid.uuid4().hex[:12]}"
    raw: RawIntrospection = await introspect_command(
        ctx.runner.run_command(image, spec, container),
        env=ctx.runner.cli_env(),
        timeout_s=ctx.settings.sandbox.timeout_s,
        cleanup=lambda: ctx.runner.cleanup(container),
    )
    intro = build_introspection(
        raw, launch=launch, package=name, version=version, private=ctx.private
    )
    return record(intro)


async def scan_population(
    ctx: ScanContext,
    population: Population,
    *,
    concurrency: int = 4,
    progress: Callable[[ServerRecord], None] | None = None,
) -> list[ServerRecord]:
    sem = asyncio.Semaphore(concurrency)
    now = datetime.now(UTC)

    async def one(entry: Any) -> ServerRecord:
        async with sem:
            try:
                pack = await npm.packument(ctx.http, entry.name)
                rec = await introspect_version(
                    ctx,
                    pack,
                    entry.version
                    if entry.version in pack["versions"]
                    else npm.latest_version(pack),
                    observed_via=ObservedVia.WEEKLY_SCAN,
                    weekly_downloads=entry.weekly_downloads,
                    as_of=now,
                )
            except (HttpError, KeyError) as exc:
                # Never fail the whole scan because one package failed.
                rec = ServerRecord(
                    observed_via=ObservedVia.WEEKLY_SCAN,
                    package=PackageInfo(name=entry.name, version=entry.version),
                    introspection=Introspection(
                        status=Status.INSTALL_FAILED, error=f"metadata: {exc}"
                    ),
                )
            if progress:
                progress(rec)
            return rec

    return list(await asyncio.gather(*(one(e) for e in population.packages)))


def select_backfill_versions(
    packument: dict[str, Any], *, since: datetime, max_versions: int, done: set[str]
) -> list[str]:
    times = release_times(packument)
    eligible = sorted(
        (t, v)
        for v, t in times.items()
        if t >= since and "-" not in v  # skip pre-releases
    )
    chosen = [v for _, v in eligible[-max_versions:]] if max_versions else [v for _, v in eligible]
    return [v for v in chosen if v not in done]


async def backfill_package(
    ctx: ScanContext,
    store: SnapshotStore,
    package: str,
    *,
    since: datetime,
    max_versions: int,
    progress: Callable[[ServerRecord], None] | None = None,
) -> list[ServerRecord]:
    """Introspect historical versions oldest->newest. Resumable: already-stored versions are skipped."""
    pack = await npm.packument(ctx.http, package)
    done = {r.package.version for r in store.read_backfill(package)}
    out = []
    for version in select_backfill_versions(
        pack, since=since, max_versions=max_versions, done=done
    ):
        rec = await introspect_version(ctx, pack, version, observed_via=ObservedVia.BACKFILL)
        append_jsonl(store.backfill_path(package), rec)
        out.append(rec)
        if progress:
            progress(rec)
    return out


def history_changes(records: Sequence[ServerRecord]) -> list[ChangeRecord]:
    """Consecutive-version diffs over a package's (backfilled) history."""
    ordered = sorted(
        (r for r in records if r.introspection.status is Status.OK),
        key=lambda r: r.package.published_at or r.scanned_at,
    )
    out: list[ChangeRecord] = []
    for a, b in itertools.pairwise(ordered):
        out.extend(diff_servers(a, b))
    return out
