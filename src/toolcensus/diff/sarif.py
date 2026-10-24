"""SARIF 2.1.0 output for GitHub code scanning (schema verified: sarif-schema-2.1.0.json)."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from toolcensus import REPO_URL, __version__
from toolcensus.models import ChangeRecord, ChangeType, SchemaChangeKind

SARIF_SCHEMA = "https://json.schemastore.org/sarif-2.1.0.json"

_DESCRIPTIONS = {
    ChangeType.TOOL_ADDED: "A tool was added to the server's advertised tool surface.",
    ChangeType.TOOL_REMOVED: "A tool was removed from the server's advertised tool surface.",
    ChangeType.DESCRIPTION_CHANGED: "A tool description changed.",
    ChangeType.INPUT_SCHEMA_CHANGED: "A tool input schema changed.",
    ChangeType.OUTPUT_SCHEMA_CHANGED: "A tool output schema changed.",
    ChangeType.ANNOTATIONS_CHANGED: "A tool's annotations changed.",
    ChangeType.OTHER_CHANGED: "Another top-level field of a tool definition changed.",
}


def _level(change: ChangeRecord) -> str:
    if (
        change.change_type is ChangeType.TOOL_ADDED
        or change.schema_change is SchemaChangeKind.WIDENED
    ):
        return "warning"
    if change.change_type in (ChangeType.DESCRIPTION_CHANGED, ChangeType.ANNOTATIONS_CHANGED):
        return "warning"
    return "note"


def to_sarif(changes: Sequence[ChangeRecord], *, artifact_uri: str) -> dict[str, Any]:
    rules = [
        {
            "id": f"toolcensus/{ct.value}",
            "name": ct.value,
            "shortDescription": {"text": text},
            "helpUri": f"{REPO_URL}/blob/main/METHODOLOGY.md",
        }
        for ct, text in _DESCRIPTIONS.items()
    ]
    results = []
    for c in changes:
        kind = f" ({c.schema_change.value})" if c.schema_change else ""
        detail = f": {'; '.join(c.details)}" if c.details else ""
        results.append(
            {
                "ruleId": f"toolcensus/{c.change_type.value}",
                "level": _level(c),
                "message": {
                    "text": f"{c.package} {c.from_version} -> {c.to_version}: tool '{c.tool}' "
                    f"{c.change_type.value}{kind}{detail}"
                },
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": artifact_uri},
                            "region": {"startLine": 1},
                        },
                        "logicalLocations": [
                            {"fullyQualifiedName": f"{c.package}/{c.tool}", "kind": "function"}
                        ],
                    }
                ],
                "partialFingerprints": {
                    "toolcensus/v1": f"{c.package}|{c.tool}|{c.change_type.value}|{c.to_tool_hash}"
                },
            }
        )
    return {
        "$schema": SARIF_SCHEMA,
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "toolcensus",
                        "version": __version__,
                        "informationUri": REPO_URL,
                        "rules": rules,
                    }
                },
                "results": results,
            }
        ],
    }
