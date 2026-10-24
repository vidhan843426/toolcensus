"""Generate the MkDocs site sources (``site/docs``) from committed data only."""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jinja2 import Environment, PackageLoader, StrictUndefined

from toolcensus import METHODOLOGY_VERSION
from toolcensus.metrics.aggregate import weekly_aggregates
from toolcensus.models import ChangeRecord, ServerRecord
from toolcensus.pipeline import history_changes
from toolcensus.report.charts import line_chart
from toolcensus.report.hints import improvement_hints
from toolcensus.storage.snapshots import SnapshotStore, package_slug

HEADLINE: list[tuple[str, str, str]] = [
    ("Servers measured", "servers_measured", ""),
    ("Reached status `ok`", "pct_ok", "%"),
    ("Tools measured", "tools_measured", ""),
    ("Packages with npm provenance", "pct_provenance", "%"),
    ("Packages with install scripts", "pct_install_scripts", "%"),
    ("Tools declaring any annotation", "pct_tools_annotated", "%"),
    ("Servers with all tools annotated", "pct_servers_all_annotated", "%"),
    ("Tools with `additionalProperties: false`", "pct_tools_additional_properties_false", "%"),
    ("Tools with non-printing code points", "pct_tools_invisible_chars", "%"),
    ("Servers with a tool change vs previous week", "pct_servers_changed", "%"),
]

TREND_CHARTS: list[tuple[str, str, str]] = [
    ("Servers measured", "servers_measured", ""),
    ("% packages with npm provenance", "pct_provenance", "%"),
    ("% packages with install scripts", "pct_install_scripts", "%"),
    ("% tools annotated", "pct_tools_annotated", "%"),
    ("% servers with a tool change (week over week)", "pct_servers_changed", "%"),
]


def fmt(value: Any, unit: str) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.1f}{unit}" if unit else f"{value:g}"
    return f"{value}{unit}"


_CONTROL = re.compile(r"[\x00-\x1f\x7f]")


def untrusted(value: Any, limit: int = 200) -> str:
    """Neutralize server-controlled text before it is placed into Markdown/HTML pages."""
    text = _CONTROL.sub(" ", str(value))
    text = text.replace("`", "'").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
    return text if len(text) <= limit else text[: limit - 1] + "…"


@dataclass
class _Dated:
    when: str
    rec: ChangeRecord


def _env() -> Environment:
    env = Environment(
        loader=PackageLoader("toolcensus.report", "templates"),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        autoescape=False,  # noqa: S701 - output is Markdown; values are escaped by MkDocs
    )
    env.globals.update(fmt=fmt, slug=package_slug)
    env.filters["u"] = untrusted
    return env


def build_site(
    store: SnapshotStore,
    out_dir: Path,
    *,
    week: str | None = None,
    docs_root: Path = Path("."),
) -> list[Path]:
    weeks = store.weeks()
    if not weeks:
        raise ValueError("no snapshots found; run `toolcensus scan` first")
    week = week or weeks[-1]
    if week not in weeks:
        raise ValueError(f"no snapshot for week {week}")
    upto = [w for w in weeks if w <= week]
    env = _env()
    written: list[Path] = []

    def write(rel: str, text: str) -> None:
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, "utf-8")
        written.append(path)

    rows: list[dict[str, Any]] = []
    week_records: dict[str, list[ServerRecord]] = {}
    week_diffs: dict[str, list[ChangeRecord]] = {}
    for w in upto:
        week_records[w] = store.read_servers(w)
        week_diffs[w] = store.read_diffs(w)
        rows.append({"week": w, **weekly_aggregates(week_records[w], week_diffs[w])})
    agg = rows[-1]

    charts = []
    for title, key, unit in TREND_CHARTS:
        file = f"{key}.svg"
        write(
            f"assets/charts/{file}",
            line_chart(
                title,
                [r["week"] for r in rows],
                [r[key] for r in rows],
                unit=unit,
                y_max=100 if unit == "%" else None,
            ),
        )
        charts.append({"title": title, "file": file})

    # Backfilled history, kept visibly separate from live observations.
    backfill_by_pkg: dict[str, list[ServerRecord]] = defaultdict(list)
    for rec in store.all_backfill():
        backfill_by_pkg[rec.package.name].append(rec)
    hist_changes = {p: history_changes(recs) for p, recs in backfill_by_pkg.items()}
    pub_times = {
        (r.package.name, r.package.version): r.package.published_at
        for recs in backfill_by_pkg.values()
        for r in recs
    }
    per_month: dict[str, dict[str, Any]] = defaultdict(lambda: {"packages": set(), "changes": 0})
    for pkg, changes in hist_changes.items():
        for c in changes:
            ts = pub_times.get((pkg, c.to_version))
            if ts is None:
                continue
            m = per_month[ts.strftime("%Y-%m")]
            m["packages"].add(pkg)
            m["changes"] += 1
    history = [
        {"month": k, "packages": len(v["packages"]), "changes": v["changes"]}
        for k, v in sorted(per_month.items())
    ]

    keys = [k for k in agg if k != "week"]
    write(
        "index.md",
        env.get_template("index.md.j2").render(
            week=week,
            methodology_version=METHODOLOGY_VERSION,
            agg=agg,
            headline=HEADLINE,
            charts=charts,
        ),
    )
    write(
        "trends.md",
        env.get_template("trends.md.j2").render(
            charts=charts, rows=rows, keys=keys, history=history
        ),
    )

    latest = sorted(
        week_records[week], key=lambda r: (-(r.package.weekly_downloads or 0), r.package.name)
    )
    write(
        "servers/index.md",
        env.get_template("servers_index.md.j2").render(week=week, records=latest),
    )
    for rec in latest:
        dated = [
            _Dated(f"week {w}", c)
            for w in upto
            for c in week_diffs[w]
            if c.package == rec.package.name
        ]
        dated += [
            _Dated(
                f"backfill {ts:%Y-%m-%d}"
                if (ts := pub_times.get((rec.package.name, c.to_version)))
                else "backfill",
                c,
            )
            for c in hist_changes.get(rec.package.name, [])
        ]
        write(
            f"servers/{package_slug(rec.package.name)}.md",
            env.get_template("server.md.j2").render(
                rec=rec, hints=improvement_hints(rec), changes=dated
            ),
        )

    write(
        "download.md",
        env.get_template("download.md.j2").render(
            methodology_version=METHODOLOGY_VERSION, weeks=weeks
        ),
    )
    for name in ("METHODOLOGY.md", "ETHICS.md"):
        src = docs_root / name
        if src.exists():
            dest = out_dir / name.lower()
            shutil.copyfile(src, dest)
            written.append(dest)
    return written
