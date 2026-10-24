"""``toolcensus`` command-line interface."""

from __future__ import annotations

import asyncio
import json
import shlex
import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer

from toolcensus import METHODOLOGY_VERSION, __version__
from toolcensus.config import Settings
from toolcensus.models import ObservedVia, PackageInfo, Population, ServerRecord, Status

app = typer.Typer(
    help="Reproducible, metadata-only health measurements for public MCP servers.",
    no_args_is_help=True,
    add_completion=False,
)

DataDir = Annotated[Path, typer.Option("--data", help="Data directory.")]


def _settings(**kw: object) -> Settings:
    return Settings(**kw)  # type: ignore[arg-type]


def _this_week() -> str:
    from toolcensus.storage.snapshots import iso_week

    return iso_week(datetime.now(UTC))


def _require_engine(settings: Settings) -> None:
    if shutil.which(settings.sandbox.engine) is None:
        typer.secho(
            f"`{settings.sandbox.engine}` was not found. ToolCensus only runs third-party servers "
            "inside a container sandbox; install Docker (or set TOOLCENSUS_CONTAINER_ENGINE=podman).",
            fg="red",
            err=True,
        )
        raise typer.Exit(2)


def _progress(rec: ServerRecord) -> None:
    intro = rec.introspection
    typer.echo(
        f"  {intro.status.value:<24} {rec.package.name}@{rec.package.version} ({len(intro.tools)} tools)"
    )


@app.command()
def version() -> None:
    """Print tool and methodology versions."""
    typer.echo(f"toolcensus {__version__} (methodology {METHODOLOGY_VERSION})")


@app.command()
def discover(
    top: Annotated[int, typer.Option(help="Population size.")] = 200,
    out: Annotated[Path | None, typer.Option(help="Write population JSON here.")] = None,
    week: Annotated[str | None, typer.Option(help="ISO week YYYY-WW (default: current).")] = None,
    exclusions: Path = Path("exclusions.yaml"),
    registry: Annotated[
        bool, typer.Option(help="Include the MCP Registry source (slow on a cold cache).")
    ] = True,
    data: DataDir = Path("data"),
) -> None:
    """Select the population: MCP Registry + npm search, ranked by weekly downloads."""
    from toolcensus.discovery.http import CachedHttp
    from toolcensus.discovery.population import select_population
    from toolcensus.storage.snapshots import SnapshotStore

    wk = week or _this_week()

    async def run() -> Population:
        async with CachedHttp() as http:
            return await select_population(
                http, week=wk, top_n=top, exclusions_path=exclusions, include_registry=registry
            )

    pop = asyncio.run(run())
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pop.model_dump_json(indent=2) + "\n")
        path = out
    else:
        path = SnapshotStore(data).write_population(pop)
    typer.echo(f"{len(pop.packages)} servers selected, {len(pop.excluded)} excluded -> {path}")


@app.command()
def scan(
    population: Annotated[
        Path | None, typer.Option(help="Population JSON (default: this week's).")
    ] = None,
    week: Annotated[str | None, typer.Option(help="ISO week YYYY-WW.")] = None,
    concurrency: int = 4,
    timeout: Annotated[float, typer.Option(help="Per-server wall-clock limit (s).")] = 60.0,
    data: DataDir = Path("data"),
    overrides: Path = Path("launch_overrides.yaml"),
) -> None:
    """Introspect every server in the population (sandboxed) and write the week's snapshot + diffs."""
    from dataclasses import replace

    from toolcensus.diff.engine import diff_snapshots, drift_without_bump
    from toolcensus.discovery.http import CachedHttp
    from toolcensus.discovery.registry import registry_npm_index
    from toolcensus.pipeline import ScanContext, scan_population
    from toolcensus.sandbox.docker import DockerRunner
    from toolcensus.storage.snapshots import SnapshotStore

    settings = _settings(data_dir=data)
    settings = replace(settings, sandbox=replace(settings.sandbox, timeout_s=timeout))
    _require_engine(settings)
    store = SnapshotStore(data)
    wk = week or _this_week()
    pop = (
        Population.model_validate_json(population.read_text())
        if population
        else store.read_population(wk)
    )
    if population:
        pop = pop.model_copy(update={"week": wk})
        store.write_population(pop)

    async def run() -> list[ServerRecord]:
        async with CachedHttp(settings.http) as http:
            ctx = ScanContext.create(
                http, DockerRunner(settings.sandbox), settings, overrides_path=overrides
            )
            ctx.registry = await registry_npm_index(http)
            typer.echo(f"scanning {len(pop.packages)} servers (concurrency {concurrency})")
            return await scan_population(ctx, pop, concurrency=concurrency, progress=_progress)

    records = asyncio.run(run())
    path = store.write_servers(wk, records)
    prev = store.previous_week(wk)
    changes = diff_snapshots(store.read_servers(prev), records) if prev else []
    store.write_diffs(wk, changes)
    ok = sum(r.introspection.status is Status.OK for r in records)
    typer.echo(
        f"{ok}/{len(records)} ok -> {path}; {len(changes)} change records vs {prev or 'nothing'}"
    )
    if prev:
        silent = drift_without_bump(store.read_servers(prev), records)
        if silent:
            typer.echo(f"{len(silent)} server(s) changed their tool surface without a version bump")


@app.command()
def backfill(
    since: Annotated[str, typer.Option(help="YYYY-MM-DD")],
    max_versions_per_package: int = 30,
    population: Annotated[
        Path | None, typer.Option(help="Population JSON (default: latest week).")
    ] = None,
    package: Annotated[list[str] | None, typer.Option(help="Only these packages.")] = None,
    data: DataDir = Path("data"),
    overrides: Path = Path("launch_overrides.yaml"),
) -> None:
    """Introspect past versions (oldest to newest) into data/backfill/. Resumable."""
    from toolcensus.discovery.http import CachedHttp
    from toolcensus.discovery.registry import registry_npm_index
    from toolcensus.pipeline import ScanContext, backfill_package
    from toolcensus.sandbox.docker import DockerRunner
    from toolcensus.storage.snapshots import SnapshotStore

    settings = _settings(data_dir=data)
    _require_engine(settings)
    store = SnapshotStore(data)
    if package:
        names = list(package)
    else:
        if population:
            pop = Population.model_validate_json(population.read_text())
        else:
            weeks = store.weeks()
            if not weeks:
                typer.secho(
                    "no population found; run `toolcensus discover` first", fg="red", err=True
                )
                raise typer.Exit(2)
            pop = store.read_population(weeks[-1])
        names = [p.name for p in pop.packages]
    start = datetime.fromisoformat(since).replace(tzinfo=UTC)

    async def run() -> int:
        total = 0
        async with CachedHttp(settings.http) as http:
            ctx = ScanContext.create(
                http, DockerRunner(settings.sandbox), settings, overrides_path=overrides
            )
            ctx.registry = await registry_npm_index(http)
            for name in names:
                typer.echo(f"{name}:")
                try:
                    total += len(
                        await backfill_package(
                            ctx,
                            store,
                            name,
                            since=start,
                            max_versions=max_versions_per_package,
                            progress=_progress,
                        )
                    )
                except Exception as exc:  # one package must never stop the backfill
                    typer.echo(f"  skipped: {exc}")
        return total

    typer.echo(f"{asyncio.run(run())} historical versions introspected -> {store.backfill}")


@app.command()
def backtest(
    incidents: Path = Path("incidents/incidents.yaml"),
    out: Path = Path("reports/backtest.md"),
    from_data: Annotated[
        bool, typer.Option(help="Use committed backfill data only (no sandbox).")
    ] = False,
    data: DataDir = Path("data"),
) -> None:
    """Evaluate which signals changed around publicly documented incidents; write a hit/miss scorecard."""
    from toolcensus.backtest import evaluate, load_incidents, render_markdown
    from toolcensus.discovery.http import CachedHttp
    from toolcensus.pipeline import ScanContext
    from toolcensus.sandbox.docker import DockerRunner
    from toolcensus.storage.snapshots import SnapshotStore

    settings = _settings(data_dir=data)
    store = SnapshotStore(data)
    items = load_incidents(incidents)
    if not from_data:
        _require_engine(settings)

    async def run() -> str:
        if from_data:
            return render_markdown([await evaluate(i, store, None) for i in items])
        async with CachedHttp(settings.http) as http:
            ctx = ScanContext.create(http, DockerRunner(settings.sandbox), settings)
            return render_markdown([await evaluate(i, store, ctx) for i in items])

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(asyncio.run(run()))
    typer.echo(f"scorecard -> {out}")


def _print_summary(rec: ServerRecord) -> None:
    intro = rec.introspection
    sc = rec.supply_chain
    typer.secho(f"\n{rec.package.name}@{rec.package.version}", bold=True)
    typer.echo(
        f"  status            {intro.status.value}" + (f" ({intro.error})" if intro.error else "")
    )
    if intro.server_info:
        typer.echo(
            f"  server            {intro.server_info.get('name')} {intro.server_info.get('version')}"
        )
    if intro.protocol_version:
        typer.echo(f"  protocol          {intro.protocol_version}")
    if sc:
        typer.echo("\n  supply chain")
        typer.echo(f"    provenance            {'yes' if sc.has_provenance else 'no'}")
        typer.echo(f"    install scripts       {', '.join(sc.install_scripts) or 'none'}")
        typer.echo(f"    direct dependencies   {sc.direct_dependency_count}")
        typer.echo(f"    maintainers           {sc.maintainer_count}")
        typer.echo(f"    releases (90 days)    {sc.releases_last_90d}")
        typer.echo(f"    repository linked     {'yes' if sc.repo_linked else 'no'}")
        typer.echo(f"    MCP Registry listed   {'yes' if sc.registry_listed else 'no'}")
    if intro.tools:
        s = rec.summary
        typer.echo(f"\n  tools ({len(intro.tools)})  surface {intro.surface_hash}")
        for t in intro.tools:
            values = t.definition.get("annotations") or {}
            ann = (
                ",".join(
                    f"{k.removesuffix('Hint')}={'yes' if values.get(k) else 'no'}"
                    for k, declared in t.annotation_metrics.declared.items()
                    if declared
                )
                or "-"
            )
            flags = []
            if t.description_metrics.invisible_char_count:
                flags.append("non-printing chars")
            if t.annotation_metrics.side_effect_unannotated:
                flags.append("side-effect verb, no hint")
            typer.echo(
                f"    {t.name:<32} {t.hashes.tool_hash[7:19]}  ann={ann}  {'; '.join(flags)}"
            )
        if s:
            typer.echo(
                f"\n  annotated tools {s.annotated_tool_ratio:.0%}  ·  "
                f"side-effect verbs without hint {s.side_effect_unannotated_count}"
            )
    from toolcensus.report.hints import improvement_hints

    hints = improvement_hints(rec)
    if hints:
        typer.echo("\n  improvement hints")
        for h in hints:
            typer.echo(f"    - {h}")


@app.command()
def check(
    package: Annotated[str, typer.Argument(help="npm package, optionally @version")],
    as_json: Annotated[bool, typer.Option("--json", help="Emit the full record as JSON.")] = False,
    timeout: float = 60.0,
    overrides: Path = Path("launch_overrides.yaml"),
) -> None:
    """Measure one npm MCP server locally, with the same sandbox and allowlist as the weekly scan."""
    from dataclasses import replace

    from toolcensus.discovery import npm
    from toolcensus.discovery.http import CachedHttp
    from toolcensus.discovery.registry import registry_npm_index
    from toolcensus.pipeline import ScanContext, introspect_version
    from toolcensus.privacy import NullSink
    from toolcensus.sandbox.docker import DockerRunner

    settings = _settings()
    settings = replace(settings, sandbox=replace(settings.sandbox, timeout_s=timeout))
    _require_engine(settings)
    name, _, ver = (
        package.rpartition("@")
        if package.count("@") > (1 if package.startswith("@") else 0)
        else (package, "", "")
    )

    async def run() -> ServerRecord:
        async with CachedHttp(settings.http) as http:
            ctx = ScanContext.create(
                http, DockerRunner(settings.sandbox), settings, overrides_path=overrides
            )
            ctx.private = NullSink()
            ctx.registry = await registry_npm_index(http)
            pack = await npm.packument(http, name)
            [dl] = (await npm.weekly_downloads(http, [name])).values()
            return await introspect_version(
                ctx,
                pack,
                ver or npm.latest_version(pack),
                observed_via=ObservedVia.CHECK,
                weekly_downloads=dl,
                as_of=datetime.now(UTC),
            )

    if not as_json:
        typer.echo(
            f"building sandbox for {package} (install has network; run has none)...", err=True
        )
    rec = asyncio.run(run())
    if as_json:
        typer.echo(rec.model_dump_json(indent=2))
    else:
        _print_summary(rec)


@app.command("check-local")
def check_local(
    command: Annotated[str, typer.Argument(help="Command that starts YOUR OWN stdio server.")],
    as_json: Annotated[bool, typer.Option("--json")] = False,
    timeout: float = 30.0,
) -> None:
    """Measure a server you are developing (NOT sandboxed - only for your own code)."""
    from toolcensus.introspect.build import build_introspection, summarize
    from toolcensus.introspect.collect import introspect_command
    from toolcensus.models import LaunchInfo
    from toolcensus.privacy import NullSink

    argv = shlex.split(command)
    raw = asyncio.run(introspect_command(argv, timeout_s=timeout))
    intro = build_introspection(
        raw,
        launch=LaunchInfo(source="local", command=argv),
        package="local",
        version="0",
        private=NullSink(),
    )
    info = intro.server_info or {}
    rec = ServerRecord(
        observed_via=ObservedVia.CHECK,
        package=PackageInfo(
            ecosystem="local",
            name=str(info.get("name", "local")),
            version=str(info.get("version", "0")),
        ),
        introspection=intro,
        summary=summarize(intro.tools) if intro.status is Status.OK else None,
    )
    if as_json:
        typer.echo(rec.model_dump_json(indent=2))
    else:
        _print_summary(rec)


@app.command()
def diff(
    snapshot_a: Annotated[
        Path, typer.Argument(help="Week dir, servers.jsonl, or `check --json` file")
    ],
    snapshot_b: Annotated[Path, typer.Argument()],
    package: Annotated[str | None, typer.Option(help="Only this package.")] = None,
    fail_on_change: Annotated[
        bool, typer.Option(help="Exit 1 if any tool-surface change is found.")
    ] = False,
    format: Annotated[str, typer.Option(help="text | json | sarif")] = "text",
) -> None:
    """Compare two snapshots and classify tool-definition changes. Usable as a CI gate."""
    from toolcensus.diff.engine import diff_snapshots
    from toolcensus.diff.sarif import to_sarif
    from toolcensus.storage.snapshots import load_records

    try:
        old, new = load_records(snapshot_a), load_records(snapshot_b)
    except (OSError, ValueError) as exc:
        typer.secho(f"cannot read snapshots: {exc}", fg="red", err=True)
        raise typer.Exit(2) from exc
    if (
        len(old) == 1
        and len(new) == 1
        and old[0].package.name != new[0].package.name
        and package is None
    ):
        # Two single-server records (e.g. two `check --json` runs of a locally renamed server).
        new = [
            new[0].model_copy(
                update={"package": new[0].package.model_copy(update={"name": old[0].package.name})}
            )
        ]
    changes = diff_snapshots(old, new, package=package)

    if format == "json":
        typer.echo(json.dumps([json.loads(c.model_dump_json()) for c in changes], indent=2))
    elif format == "sarif":
        typer.echo(json.dumps(to_sarif(changes, artifact_uri=str(snapshot_b)), indent=2))
    elif format == "text":
        if not changes:
            typer.echo("no tool-surface changes")
        for c in changes:
            kind = f" [{c.schema_change.value}]" if c.schema_change else ""
            details = f" - {'; '.join(c.details)}" if c.details else ""
            typer.echo(
                f"{c.package} {c.from_version} -> {c.to_version}  {c.tool}: {c.change_type.value}{kind}{details}"
            )
    else:
        typer.secho(f"unknown format {format!r}", fg="red", err=True)
        raise typer.Exit(2)
    if fail_on_change and changes:
        raise typer.Exit(1)


@app.command()
def report(
    week: Annotated[str | None, typer.Option(help="ISO week YYYY-WW (default: latest).")] = None,
    out: Path = Path("site/docs"),
    data: DataDir = Path("data"),
) -> None:
    """Build the static site pages from committed data."""
    from toolcensus.report.build import build_site
    from toolcensus.storage.snapshots import SnapshotStore

    try:
        files = build_site(SnapshotStore(data), out, week=week)
    except ValueError as exc:
        typer.secho(str(exc), fg="red", err=True)
        raise typer.Exit(2) from exc
    typer.echo(f"{len(files)} files written to {out}")


@app.command()
def dataset(
    data: DataDir = Path("data"),
    sqlite: Annotated[Path | None, typer.Option(help="Also build a SQLite DB here.")] = None,
) -> None:
    """Export flattened CSV (+ Parquet if pyarrow is installed) tables to data/dataset/."""
    from toolcensus.storage.dataset import export_dataset
    from toolcensus.storage.snapshots import SnapshotStore

    files = export_dataset(SnapshotStore(data), data / "dataset", sqlite_path=sqlite)
    typer.echo("\n".join(str(f) for f in files))


@app.command()
def schemas(
    out: Path = Path("schemas"),
    check: Annotated[
        bool, typer.Option("--check", help="Fail if committed schemas are stale.")
    ] = False,
) -> None:
    """Write (or check) JSON Schemas for every record type."""
    from toolcensus.storage.validate import schemas_up_to_date, write_schemas

    if check:
        if not schemas_up_to_date(out):
            typer.secho("schemas are out of date; run `toolcensus schemas`", fg="red", err=True)
            raise typer.Exit(1)
        typer.echo("schemas up to date")
        return
    for p in write_schemas(out):
        typer.echo(str(p))


@app.command("verify-data")
def verify_data_cmd(data: DataDir = Path("data"), schema_dir: Path = Path("schemas")) -> None:
    """Schema-validate every snapshot and backfill file."""
    from toolcensus.storage.validate import verify_data

    checked, errors = verify_data(data, schema_dir)
    for e in errors[:50]:
        typer.secho(e, fg="red", err=True)
    typer.echo(f"{checked} records checked, {len(errors)} errors")
    if errors:
        raise typer.Exit(1)


def main() -> None:  # pragma: no cover
    sys.exit(app())
