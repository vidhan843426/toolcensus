"""Flattened analyst tables (CSV always, Parquet when pyarrow is installed) + SQLite."""

from __future__ import annotations

import csv
import sqlite3
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from toolcensus.metrics.aggregate import weekly_aggregates
from toolcensus.storage.snapshots import SnapshotStore

TABLES = ("servers", "tools", "changes", "weekly_aggregates")


def build_tables(store: SnapshotStore) -> dict[str, list[dict[str, Any]]]:
    servers: list[dict[str, Any]] = []
    tools: list[dict[str, Any]] = []
    changes: list[dict[str, Any]] = []
    weekly: list[dict[str, Any]] = []
    for week in store.weeks():
        recs = store.read_servers(week)
        diffs = store.read_diffs(week)
        weekly.append({"week": week, **weekly_aggregates(recs, diffs)})
        for r in recs:
            sc = r.supply_chain.model_dump() if r.supply_chain else {}
            sc["install_scripts"] = ";".join(sc.get("install_scripts", []))
            servers.append(
                {
                    "week": week,
                    "package": r.package.name,
                    "version": r.package.version,
                    "weekly_downloads": r.package.weekly_downloads,
                    "status": r.introspection.status.value,
                    "protocol_version": r.introspection.protocol_version,
                    "surface_hash": r.introspection.surface_hash,
                    "tool_count": len(r.introspection.tools),
                    **{f"sc_{k}": v for k, v in sc.items()},
                    "methodology_version": r.methodology_version,
                }
            )
            for t in r.introspection.tools:
                tools.append(
                    {
                        "week": week,
                        "package": r.package.name,
                        "version": r.package.version,
                        "tool": t.name,
                        "tool_hash": t.hashes.tool_hash,
                        **t.schema_metrics.model_dump(),
                        **{f"ann_{k}": v for k, v in t.annotation_metrics.declared.items()},
                        "side_effect_unannotated": t.annotation_metrics.side_effect_unannotated,
                        "description_length": t.description_metrics.length,
                        "invisible_char_count": t.description_metrics.invisible_char_count,
                        "markup_tag_count": t.description_metrics.markup_tag_count,
                    }
                )
        for c in diffs:
            changes.append(
                {
                    "week": week,
                    "package": c.package,
                    "from_version": c.from_version,
                    "to_version": c.to_version,
                    "version_bumped": c.version_bumped,
                    "tool": c.tool,
                    "change_type": c.change_type.value,
                    "schema_change": c.schema_change.value if c.schema_change else None,
                }
            )
    return {"servers": servers, "tools": tools, "changes": changes, "weekly_aggregates": weekly}


def _write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    cols: list[str] = []
    for row in rows:
        cols.extend(k for k in row if k not in cols)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def export_dataset(
    store: SnapshotStore, out_dir: Path, *, sqlite_path: Path | None = None
) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    tables = build_tables(store)
    written = []
    for name, rows in tables.items():
        path = out_dir / f"{name}.csv"
        _write_csv(path, rows)
        written.append(path)
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq

        for name, rows in tables.items():
            if rows:
                path = out_dir / f"{name}.parquet"
                pq.write_table(pa.Table.from_pylist(rows), path)
                written.append(path)
    except ImportError:
        pass
    if sqlite_path is not None:
        sqlite_path.unlink(missing_ok=True)
        db = sqlite3.connect(sqlite_path)
        for name, rows in tables.items():
            if not rows:
                continue
            cols: list[str] = []
            for row in rows:
                cols.extend(k for k in row if k not in cols)
            db.execute(f"CREATE TABLE {name} ({', '.join(f'"{c}"' for c in cols)})")
            db.executemany(
                f"INSERT INTO {name} VALUES ({', '.join('?' for _ in cols)})",  # noqa: S608
                [[row.get(c) for c in cols] for row in rows],
            )
        db.commit()
        db.close()
        written.append(sqlite_path)
    return written
