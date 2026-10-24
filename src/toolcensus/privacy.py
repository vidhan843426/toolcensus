"""Responsible-disclosure routing (ETHICS.md rule 5).

Anything that needs human review before it could ever be discussed publicly (for example the
original text of a description containing hidden code points) is written *only* here. The
directory is git-ignored, and the report/dataset builders refuse to read from it.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

PUBLIC_DIRS = ("data", "site", "reports", "schemas")


class PrivateSink:
    def __init__(self, root: Path) -> None:
        resolved = root.resolve()
        for public in PUBLIC_DIRS:
            pub = Path(public).resolve()
            if resolved == pub or pub in resolved.parents:
                raise ValueError(f"private output must not live under public dir {public}/")
        self.root = root
        self.count = 0

    def record(self, *, package: str, version: str, kind: str, payload: dict[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        gitignore = self.root / ".gitignore"
        if not gitignore.exists():
            gitignore.write_text("*\n")
        entry = {
            "recorded_at": datetime.now(UTC).isoformat(timespec="seconds"),
            "package": package,
            "version": version,
            "kind": kind,
            "payload": payload,
        }
        with (self.root / "findings.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self.count += 1


class NullSink(PrivateSink):
    """Discards findings (used by `check`, which prints only counts)."""

    def __init__(self) -> None:
        self.root = Path("/dev/null")
        self.count = 0

    def record(self, *, package: str, version: str, kind: str, payload: dict[str, Any]) -> None:
        self.count += 1
