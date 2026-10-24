"""JSON Schemas for every record type, generated from the pydantic models, and data validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema
from pydantic import BaseModel

from toolcensus.models import ChangeRecord, Population, ServerRecord

SCHEMAS: dict[str, type[BaseModel]] = {
    "server-record": ServerRecord,
    "population": Population,
    "change-record": ChangeRecord,
}


def generate_schemas() -> dict[str, dict[str, Any]]:
    out = {}
    for name, model in SCHEMAS.items():
        schema = model.model_json_schema()
        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        schema["$id"] = (
            f"https://raw.githubusercontent.com/vidhan843426/toolcensus/main/schemas/{name}.schema.json"
        )
        out[name] = schema
    return out


def write_schemas(directory: Path) -> list[Path]:
    directory.mkdir(parents=True, exist_ok=True)
    paths = []
    for name, schema in generate_schemas().items():
        path = directory / f"{name}.schema.json"
        path.write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n", "utf-8")
        paths.append(path)
    return paths


def schemas_up_to_date(directory: Path) -> bool:
    for name, schema in generate_schemas().items():
        path = directory / f"{name}.schema.json"
        if not path.exists() or json.loads(path.read_text("utf-8")) != schema:
            return False
    return True


def _validator(directory: Path, name: str) -> jsonschema.Draft202012Validator:
    path = directory / f"{name}.schema.json"
    schema = json.loads(path.read_text("utf-8")) if path.exists() else generate_schemas()[name]
    return jsonschema.Draft202012Validator(schema)


def verify_data(data_dir: Path, schema_dir: Path) -> tuple[int, list[str]]:
    """Validate every snapshot/backfill file. Returns (records checked, errors)."""
    validators = {name: _validator(schema_dir, name) for name in SCHEMAS}
    errors: list[str] = []
    checked = 0

    def check(path: Path, name: str, doc: Any, where: str) -> None:
        nonlocal checked
        checked += 1
        for err in validators[name].iter_errors(doc):
            errors.append(f"{path}{where}: {err.json_path}: {err.message}")

    for path in sorted(data_dir.rglob("population.json")):
        check(path, "population", json.loads(path.read_text("utf-8")), "")
    for path in sorted(data_dir.rglob("*.jsonl")):
        name = "change-record" if path.name == "diffs.jsonl" else "server-record"
        for i, line in enumerate(path.read_text("utf-8").splitlines(), 1):
            if line.strip():
                check(path, name, json.loads(line), f":{i}")
    return checked, errors
