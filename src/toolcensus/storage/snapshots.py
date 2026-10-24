"""Snapshot I/O: ``data/snapshots/YYYY-WW/{population.json,servers.jsonl,diffs.jsonl}``
and ``data/backfill/<package>.jsonl``."""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Iterator
from datetime import date, datetime
from pathlib import Path

from pydantic import BaseModel

from toolcensus.models import ChangeRecord, Population, ServerRecord

WEEK_RE = re.compile(r"^\d{4}-\d{2}$")


def iso_week(d: date | datetime) -> str:
    year, week, _ = d.isocalendar()
    return f"{year}-{week:02d}"


def week_start(week: str) -> date:
    year, wk = map(int, week.split("-"))
    return date.fromisocalendar(year, wk, 1)


def write_jsonl(path: Path, records: Iterable[BaseModel]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8") as fh:
        for r in records:
            fh.write(r.model_dump_json() + "\n")
            n += 1
    return n


def append_jsonl(path: Path, record: BaseModel) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(record.model_dump_json() + "\n")


def read_jsonl[M: BaseModel](path: Path, model: type[M]) -> list[M]:
    if not path.exists():
        return []
    return [
        model.model_validate_json(line)
        for line in path.read_text("utf-8").splitlines()
        if line.strip()
    ]


def package_slug(name: str) -> str:
    return name.replace("@", "").replace("/", "__")


class SnapshotStore:
    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self.snapshots = data_dir / "snapshots"
        self.backfill = data_dir / "backfill"

    def week_dir(self, week: str) -> Path:
        if not WEEK_RE.match(week):
            raise ValueError(f"week must look like YYYY-WW, got {week!r}")
        return self.snapshots / week

    def weeks(self) -> list[str]:
        if not self.snapshots.exists():
            return []
        return sorted(
            p.name for p in self.snapshots.iterdir() if p.is_dir() and WEEK_RE.match(p.name)
        )

    def previous_week(self, week: str) -> str | None:
        earlier = [
            w for w in self.weeks() if w < week and (self.week_dir(w) / "servers.jsonl").exists()
        ]
        return earlier[-1] if earlier else None

    def write_population(self, pop: Population) -> Path:
        path = self.week_dir(pop.week) / "population.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(pop.model_dump_json(indent=2) + "\n", "utf-8")
        return path

    def read_population(self, week: str) -> Population:
        return Population.model_validate_json(
            (self.week_dir(week) / "population.json").read_text("utf-8")
        )

    def write_servers(self, week: str, records: Iterable[ServerRecord]) -> Path:
        path = self.week_dir(week) / "servers.jsonl"
        ordered: list[ServerRecord] = sorted(records, key=lambda r: r.package.name)
        write_jsonl(path, ordered)
        return path

    def read_servers(self, week: str) -> list[ServerRecord]:
        return read_jsonl(self.week_dir(week) / "servers.jsonl", ServerRecord)

    def write_diffs(self, week: str, changes: Iterable[ChangeRecord]) -> Path:
        path = self.week_dir(week) / "diffs.jsonl"
        write_jsonl(path, changes)
        return path

    def read_diffs(self, week: str) -> list[ChangeRecord]:
        return read_jsonl(self.week_dir(week) / "diffs.jsonl", ChangeRecord)

    def backfill_path(self, package: str) -> Path:
        return self.backfill / f"{package_slug(package)}.jsonl"

    def read_backfill(self, package: str) -> list[ServerRecord]:
        return read_jsonl(self.backfill_path(package), ServerRecord)

    def all_backfill(self) -> Iterator[ServerRecord]:
        if self.backfill.exists():
            for path in sorted(self.backfill.glob("*.jsonl")):
                yield from read_jsonl(path, ServerRecord)


def load_records(path: Path) -> list[ServerRecord]:
    """Load ServerRecords from a week dir, a .jsonl file or a single-record .json (``check --json``)."""
    if path.is_dir():
        path = path / "servers.jsonl"
    if path.suffix == ".json":
        data = json.loads(path.read_text("utf-8"))
        items = data if isinstance(data, list) else [data]
        return [ServerRecord.model_validate(i) for i in items]
    return read_jsonl(path, ServerRecord)
