"""CLI exit codes, report build from two fixture weeks, dataset export and leak checks."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest
from typer.testing import CliRunner

from toolcensus.cli import app
from toolcensus.config import Settings
from toolcensus.diff.engine import diff_snapshots
from toolcensus.models import Population, PopulationEntry
from toolcensus.privacy import PrivateSink
from toolcensus.report.build import build_site
from toolcensus.report.charts import line_chart
from toolcensus.storage.dataset import export_dataset
from toolcensus.storage.snapshots import SnapshotStore, iso_week, load_records, week_start
from toolcensus.storage.validate import schemas_up_to_date, verify_data, write_schemas

from helpers import fixture_cmd, fixture_record

runner = CliRunner()
ROOT = Path(__file__).parents[1]


async def _write_json(path: Path, variant: str, version: str = "1.0.0") -> Path:
    rec = await fixture_record(variant, version=version)
    path.write_text(rec.model_dump_json())
    return path


async def test_diff_exit_codes(tmp_path: Path) -> None:
    a = await _write_json(tmp_path / "a.json", "schema_v1")
    b = await _write_json(tmp_path / "b.json", "schema_widened", "1.1.0")
    same = await _write_json(tmp_path / "same.json", "schema_v1")

    res = runner.invoke(app, ["diff", str(a), str(same), "--fail-on-change"])
    assert res.exit_code == 0 and "no tool-surface changes" in res.output
    res = runner.invoke(app, ["diff", str(a), str(b), "--fail-on-change"])
    assert res.exit_code == 1 and "schema_widened" in res.output
    res = runner.invoke(app, ["diff", str(a), str(b)])
    assert res.exit_code == 0
    res = runner.invoke(app, ["diff", str(a), str(b), "--format", "json"])
    assert json.loads(res.output)[0]["schema_change"] == "schema_widened"
    res = runner.invoke(app, ["diff", str(a), str(b), "--format", "sarif"])
    assert json.loads(res.output)["version"] == "2.1.0"
    assert runner.invoke(app, ["diff", str(a), str(b), "--format", "xml"]).exit_code == 2
    assert runner.invoke(app, ["diff", str(tmp_path / "nope.json"), str(b)]).exit_code == 2


def test_check_local() -> None:
    res = runner.invoke(app, ["check-local", " ".join(fixture_cmd("annotated"))])
    assert res.exit_code == 0, res.output
    assert "read_file" in res.output and "ann=readOnly=yes,openWorld=no" in res.output
    res = runner.invoke(app, ["check-local", " ".join(fixture_cmd("unicode")), "--json"])
    rec = json.loads(res.output)
    assert rec["introspection"]["status"] == "ok"
    assert "​" not in res.output
    assert (
        "improvement hints"
        in runner.invoke(app, ["check-local", " ".join(fixture_cmd("unicode"))]).output
    )


def test_commands_refuse_without_container_engine(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("toolcensus.cli.shutil.which", lambda _: None)
    res = runner.invoke(app, ["check", "some-server"])
    assert res.exit_code == 2 and "sandbox" in res.output
    assert runner.invoke(app, ["version"]).output.startswith("toolcensus ")


async def _two_weeks(tmp_path: Path) -> tuple[SnapshotStore, Path]:
    store = SnapshotStore(tmp_path / "data")
    private = PrivateSink(tmp_path / "private")
    weeks = {
        "2026-42": [
            ("alpha", "normal", "1.0.0"),
            ("beta", "schema_v1", "2.0.0"),
            ("gamma", "crash", "0.1.0"),
        ],
        "2026-43": [
            ("alpha", "desc_v2", "1.1.0"),
            ("beta", "schema_widened", "2.1.0"),
            ("delta", "unicode", "1.0.0"),
        ],
    }
    prev = None
    for week, items in weeks.items():
        recs = [
            await fixture_record(
                v,
                package=p,
                version=ver,
                private=private,
                has_provenance=p != "beta",
                has_install_scripts=p == "gamma",
                install_scripts=["postinstall"] if p == "gamma" else [],
            )
            for p, v, ver in items
        ]
        store.write_population(
            Population(
                week=week,
                selection_rule="fixture",
                top_n=3,
                packages=[
                    PopulationEntry(
                        name=r.package.name,
                        version=r.package.version,
                        weekly_downloads=1,
                        registry_listed=True,
                        sources=["fixture"],
                    )
                    for r in recs
                ],
            )
        )
        store.write_servers(week, recs)
        store.write_diffs(week, diff_snapshots(prev, recs) if prev else [])
        prev = recs
    # A backfilled history for alpha, kept apart from live weeks.
    from toolcensus.storage.snapshots import append_jsonl

    for variant, ver in (("normal", "0.9.0"), ("added", "1.0.0")):
        rec = await fixture_record(variant, package="alpha", version=ver)
        from datetime import UTC, datetime

        rec.package.published_at = datetime(2026, 5 if ver == "0.9.0" else 6, 1, tzinfo=UTC)
        append_jsonl(store.backfill_path("alpha"), rec)
    return store, tmp_path / "private"


async def test_report_build_and_no_private_leak(tmp_path: Path) -> None:
    store, private_dir = await _two_weeks(tmp_path)
    out = tmp_path / "site" / "docs"
    files = build_site(store, out, docs_root=ROOT)
    names = {p.relative_to(out).as_posix() for p in files}
    assert {"index.md", "trends.md", "servers/index.md", "servers/alpha.md", "download.md"} <= names
    assert "methodology.md" in names and "ethics.md" in names
    index = (out / "index.md").read_text()
    assert "Week 2026-43" in index and "Servers measured | 3" in index
    alpha = (out / "servers" / "alpha.md").read_text()
    assert "description_changed" in alpha and "backfill 2026-06-01" in alpha
    beta = (out / "servers" / "beta.md").read_text()
    assert "schema_widened" in beta and "npm provenance" in beta
    assert "Backfilled tool-surface changes" in (out / "trends.md").read_text()
    assert (out / "assets" / "charts" / "pct_provenance.svg").read_text().startswith("<svg")

    # Explicit leak test: nothing from private/ may appear in public outputs.
    findings = [
        json.loads(line) for line in (private_dir / "findings.jsonl").read_text().splitlines()
    ]
    assert findings, "the unicode fixture should have produced a private finding"
    secret_texts = {f["payload"]["definition"]["description"] for f in findings}
    public_files = [p for p in (tmp_path / "data").rglob("*") if p.is_file()]
    public_files += [p for p in (tmp_path / "site").rglob("*") if p.is_file()]
    export_dataset(store, tmp_path / "data" / "dataset")
    public_files += list((tmp_path / "data" / "dataset").glob("*"))
    for path in public_files:
        text = path.read_text("utf-8", errors="replace")
        assert "​" not in text, path
        for secret in secret_texts:
            assert secret not in text, path

    # Explicit week + errors
    assert build_site(store, tmp_path / "s2", week="2026-42")
    with pytest.raises(ValueError):
        build_site(store, tmp_path / "s3", week="2020-01")
    with pytest.raises(ValueError):
        build_site(SnapshotStore(tmp_path / "empty"), tmp_path / "s4")


async def test_report_cli_dataset_and_verify(tmp_path: Path) -> None:
    _store, _ = await _two_weeks(tmp_path)
    data = tmp_path / "data"
    res = runner.invoke(app, ["report", "--data", str(data), "--out", str(tmp_path / "docs")])
    assert res.exit_code == 0, res.output
    assert runner.invoke(app, ["report", "--data", str(tmp_path / "none")]).exit_code == 2

    db = tmp_path / "tc.sqlite"
    res = runner.invoke(app, ["dataset", "--data", str(data), "--sqlite", str(db)])
    assert res.exit_code == 0, res.output
    conn = sqlite3.connect(db)
    rows = conn.execute("SELECT COUNT(*) FROM tools").fetchone()[0]
    conn.close()
    assert rows > 0
    header = (data / "dataset" / "changes.csv").read_text().splitlines()[0]
    assert "change_type" in header

    schemas = tmp_path / "schemas"
    assert runner.invoke(app, ["schemas", "--out", str(schemas), "--check"]).exit_code == 1
    assert runner.invoke(app, ["schemas", "--out", str(schemas)]).exit_code == 0
    assert runner.invoke(app, ["schemas", "--out", str(schemas), "--check"]).exit_code == 0
    res = runner.invoke(app, ["verify-data", "--data", str(data), "--schema-dir", str(schemas)])
    assert res.exit_code == 0, res.output

    weeks = [str(data / "snapshots" / w) for w in ("2026-42", "2026-43")]
    assert runner.invoke(app, ["diff", *weeks, "--fail-on-change"]).exit_code == 1

    bad = data / "snapshots" / "2026-43" / "servers.jsonl"
    bad.write_text(bad.read_text() + '{"schema_version": 1}\n')
    res = runner.invoke(app, ["verify-data", "--data", str(data), "--schema-dir", str(schemas)])
    assert res.exit_code == 1


def test_committed_schemas_are_current() -> None:
    assert schemas_up_to_date(ROOT / "schemas")


def test_committed_data_validates() -> None:
    _checked, errors = verify_data(ROOT / "data", ROOT / "schemas")
    assert errors == []


def test_weeks_and_loading(tmp_path: Path) -> None:
    from datetime import date

    assert iso_week(date(2026, 10, 24)) == "2026-43"
    assert week_start("2026-43") == date(2026, 10, 19)
    with pytest.raises(ValueError):
        SnapshotStore(tmp_path).week_dir("2026-W43")
    assert load_records(tmp_path / "missing.jsonl") == []
    write_schemas(tmp_path / "s")
    assert "no data yet" in line_chart("t", ["a"], [None])


def test_clean_command(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("toolcensus.cli.shutil.which", lambda _: None)
    assert "nothing to clean" in runner.invoke(app, ["clean"]).output
    cache = tmp_path / "cache"
    (cache / "x").mkdir(parents=True)
    monkeypatch.setenv("TOOLCENSUS_CACHE", str(cache))
    from toolcensus.config import HttpSettings

    monkeypatch.setattr(
        "toolcensus.cli._settings", lambda **kw: Settings(http=HttpSettings(cache_dir=cache))
    )
    res = runner.invoke(app, ["clean", "--cache"])
    assert res.exit_code == 0 and "HTTP cache" in res.output and not cache.exists()
