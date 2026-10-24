"""Pipeline logic with a fake runner that launches local fixtures instead of containers."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from toolcensus.backtest import Incident, evaluate, load_incidents, render_markdown
from toolcensus.config import SandboxSettings, Settings
from toolcensus.discovery.http import CachedHttp
from toolcensus.discovery.registry import RegistryPackage
from toolcensus.models import ObservedVia, Population, PopulationEntry, Status
from toolcensus.pipeline import (
    ScanContext,
    backfill_package,
    history_changes,
    introspect_version,
    scan_population,
    select_backfill_versions,
)
from toolcensus.privacy import PrivateSink
from toolcensus.sandbox.runner import InstallFailedError, LaunchSpec
from toolcensus.storage.snapshots import SnapshotStore

from helpers import fixture_cmd

VARIANT_BY_VERSION = {
    "1.0.0": "normal",
    "1.1.0": "desc_v2",
    "1.2.0": "added",
    "2.0.0": "needs_config",
}


class FakeRunner:
    def __init__(self) -> None:
        self.cleaned: list[str] = []

    async def prepare(self, spec: LaunchSpec) -> str:
        if spec.package == "broken":
            raise InstallFailedError("npm ERR! 404")
        return "img"

    def run_command(self, image: str, spec: LaunchSpec, name: str) -> list[str]:
        if spec.package == "crashy":
            return fixture_cmd("crash")
        return fixture_cmd(VARIANT_BY_VERSION.get(spec.version, "normal"))

    async def cleanup(self, name: str) -> None:
        self.cleaned.append(name)

    def cli_env(self) -> dict[str, str]:
        return {"PATH": "/usr/bin:/bin"}


def packument(name: str = "pkg", versions: tuple[str, ...] = ("1.0.0", "1.1.0", "1.2.0")) -> dict:
    times = {v: f"2026-0{i + 1}-01T00:00:00Z" for i, v in enumerate(versions)}
    return {
        "name": name,
        "dist-tags": {"latest": versions[-1]},
        "time": {"created": "2025-12-01T00:00:00Z", **times},
        "versions": {v: {"name": name, "version": v, "bin": "cli.js"} for v in versions},
    }


def ctx(tmp_path: Path, http: CachedHttp) -> ScanContext:
    settings = Settings(sandbox=SandboxSettings(timeout_s=10), private_dir=tmp_path / "private")
    return ScanContext.create(http, FakeRunner(), settings, overrides_path=tmp_path / "none.yaml")


async def test_introspect_version_statuses(tmp_path: Path) -> None:
    async with CachedHttp(cache_path=None) as http:
        c = ctx(tmp_path, http)
        c.registry = {"pkg": RegistryPackage("io.x/pkg", "pkg", None, ("API_KEY",))}
        ok = await introspect_version(c, packument(), "1.0.0", observed_via=ObservedVia.WEEKLY_SCAN)
        assert ok.introspection.status is Status.OK and ok.summary and ok.summary.tool_count == 2
        assert (
            ok.package.registry_name == "io.x/pkg"
            and ok.supply_chain
            and ok.supply_chain.registry_listed
        )
        assert ok.introspection.launch and ok.introspection.launch.placeholder_env == ["API_KEY"]
        assert c.runner.cleaned  # type: ignore[attr-defined]

        broken = await introspect_version(
            c, packument("broken"), "1.0.0", observed_via=ObservedVia.WEEKLY_SCAN
        )
        assert broken.introspection.status is Status.INSTALL_FAILED

        nobin = packument("nobin")
        del nobin["versions"]["1.0.0"]["bin"]
        rec = await introspect_version(c, nobin, "1.0.0", observed_via=ObservedVia.WEEKLY_SCAN)
        assert rec.introspection.status is Status.NOT_MCP

        # A crash while placeholders were supplied is classified as needing configuration.
        c.registry["crashy"] = RegistryPackage("io.x/crashy", "crashy", None, ("TOKEN",))
        crashy = await introspect_version(
            c, packument("crashy"), "1.0.0", observed_via=ObservedVia.WEEKLY_SCAN
        )
        assert crashy.introspection.status is Status.REQUIRES_CONFIGURATION


async def test_scan_population_never_fails_whole_scan(tmp_path: Path) -> None:
    import respx

    from toolcensus.discovery import npm

    pop = Population(
        week="2026-43",
        selection_rule="test",
        top_n=2,
        packages=[
            PopulationEntry(
                name="pkg",
                version="1.0.0",
                weekly_downloads=5,
                registry_listed=False,
                sources=["t"],
            ),
            PopulationEntry(
                name="missing",
                version="1.0.0",
                weekly_downloads=1,
                registry_listed=False,
                sources=["t"],
            ),
        ],
    )
    seen = []
    with respx.mock:
        respx.get(f"{npm.NPM_REGISTRY}/pkg").respond(json=packument())
        respx.get(f"{npm.NPM_REGISTRY}/missing").respond(404)
        async with CachedHttp(cache_path=None) as http:
            recs = await scan_population(
                ctx(tmp_path, http), pop, concurrency=2, progress=seen.append
            )
    by = {r.package.name: r for r in recs}
    assert by["pkg"].introspection.status is Status.OK
    assert by["missing"].introspection.status is Status.INSTALL_FAILED
    assert len(seen) == 2


def test_select_backfill_versions() -> None:
    pack = packument(versions=("0.9.0", "1.0.0", "1.1.0-beta.1", "1.1.0", "1.2.0"))
    since = datetime(2026, 2, 1, tzinfo=UTC)
    assert select_backfill_versions(pack, since=since, max_versions=0, done=set()) == [
        "1.0.0",
        "1.1.0",
        "1.2.0",
    ]
    assert select_backfill_versions(pack, since=since, max_versions=2, done={"1.2.0"}) == ["1.1.0"]


async def test_backfill_is_resumable_and_backtest(tmp_path: Path) -> None:
    import respx

    from toolcensus.discovery import npm

    store = SnapshotStore(tmp_path / "data")
    with respx.mock:
        respx.get(f"{npm.NPM_REGISTRY}/pkg").respond(json=packument())
        async with CachedHttp(cache_path=None) as http:
            c = ctx(tmp_path, http)
            first = await backfill_package(
                c, store, "pkg", since=datetime(2025, 1, 1, tzinfo=UTC), max_versions=10
            )
            again = await backfill_package(
                c, store, "pkg", since=datetime(2025, 1, 1, tzinfo=UTC), max_versions=10
            )
            assert [r.package.version for r in first] == ["1.0.0", "1.1.0", "1.2.0"]
            assert again == []
            history = store.read_backfill("pkg")
            assert all(r.observed_via is ObservedVia.BACKFILL for r in history)
            kinds = [(c.to_version, c.change_type.value) for c in history_changes(history)]
            assert kinds == [
                ("1.1.0", "description_changed"),
                ("1.2.0", "tool_added"),
                ("1.2.0", "description_changed"),
            ]

            hit = Incident(
                id="T-1",
                package="pkg",
                affected_versions=["1.1.0"],
                disclosed="2026-03-01",
                kind="test",
                description="Test incident.",
                references=["https://example.test"],
            )
            result = await evaluate(hit, store, c)
            assert (
                result.hit
                and result.lead_days == 28
                and "description_changed: delete_file" in result.signals
            )

    # Offline mode works purely from committed data.
    offline = await evaluate(hit, store, None)
    assert offline.hit
    gone = hit.model_copy(update={"id": "T-2", "affected_versions": ["9.9.9"]})
    miss = await evaluate(gone, store, None)
    assert not miss.hit and "unpublished" in miss.reason
    first_version = hit.model_copy(update={"id": "T-3", "affected_versions": ["1.0.0"]})
    assert "no preceding version" in (await evaluate(first_version, store, None)).reason
    md = render_markdown([result, miss])
    assert "| T-1 |" in md and "| T-2 |" in md and "miss" in md


def test_incident_file_parses() -> None:
    incidents = load_incidents(Path(__file__).parents[1] / "incidents" / "incidents.yaml")
    assert incidents and all(i.references for i in incidents)
    assert {i.split for i in incidents} == {"dev", "holdout"}


def test_private_sink_refuses_public_dirs(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    import pytest

    monkeypatch.chdir(tmp_path)
    for bad in ("data", "data/private", "site/x", "reports"):
        with pytest.raises(ValueError):
            PrivateSink(Path(bad))
    PrivateSink(Path("private"))
