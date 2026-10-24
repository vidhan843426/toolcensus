from __future__ import annotations

import pytest

from toolcensus.diff.engine import (
    classify_schema_change,
    diff_servers,
    diff_snapshots,
    drift_without_bump,
    supply_chain_signals,
)
from toolcensus.diff.sarif import to_sarif
from toolcensus.models import ChangeType, SchemaChangeKind

from helpers import fixture_record, supply


async def _pair(a: str, b: str, *, same_version: bool = False):  # type: ignore[no-untyped-def]
    old = await fixture_record(a, version="1.0.0")
    new = await fixture_record(b, version="1.0.0" if same_version else "1.1.0")
    return old, new


async def test_no_change() -> None:
    old, new = await _pair("normal", "normal")
    assert diff_servers(old, new) == []


async def test_description_change() -> None:
    old, new = await _pair("normal", "desc_v2")
    [c] = diff_servers(old, new)
    assert c.change_type is ChangeType.DESCRIPTION_CHANGED
    assert c.tool == "delete_file" and c.version_bumped
    assert c.from_tool_hash != c.to_tool_hash


async def test_added_and_removed() -> None:
    old, new = await _pair("normal", "added")
    [c] = diff_servers(old, new)
    assert (c.change_type, c.tool) == (ChangeType.TOOL_ADDED, "search")
    [r] = diff_servers(new, old)
    assert (r.change_type, r.tool) == (ChangeType.TOOL_REMOVED, "search")


async def test_schema_widened() -> None:
    old, new = await _pair("schema_v1", "schema_widened")
    [c] = diff_servers(old, new)
    assert c.change_type is ChangeType.INPUT_SCHEMA_CHANGED
    assert c.schema_change is SchemaChangeKind.WIDENED
    assert any("limit" in d for d in c.details)
    assert any("enum constraint removed" in d for d in c.details)
    assert "additionalProperties loosened" in c.details


async def test_schema_narrowed() -> None:
    old, new = await _pair("schema_v1", "schema_narrowed")
    [c] = diff_servers(old, new)
    assert c.schema_change is SchemaChangeKind.NARROWED


async def test_annotations_changed() -> None:
    old, new = await _pair("normal", "annotated")
    changes = diff_servers(old, new)
    assert {c.change_type for c in changes} == {ChangeType.ANNOTATIONS_CHANGED}


async def test_failed_observations_are_not_diffed() -> None:
    old, new = await _pair("normal", "crash")
    assert diff_servers(old, new) == []


async def test_drift_without_version_bump() -> None:
    old, new = await _pair("normal", "desc_v2", same_version=True)
    assert drift_without_bump([old], [new]) == ["fixture-pkg"]
    changes = diff_snapshots([old], [new])
    assert changes and not changes[0].version_bumped
    assert diff_snapshots([old], [new], package="other") == []


@pytest.mark.parametrize(
    ("old", "new", "kind"),
    [
        (
            {"properties": {"a": {"type": "string"}}},
            {"properties": {"a": {"type": ["string", "null"]}}},
            SchemaChangeKind.WIDENED,
        ),
        (
            {"properties": {"a": {"type": ["string", "null"]}}},
            {"properties": {"a": {"type": "string"}}},
            SchemaChangeKind.NARROWED,
        ),
        (
            {"properties": {"a": {"type": "string"}}},
            {"properties": {"a": {"type": "integer"}}},
            SchemaChangeKind.OTHER,
        ),
        (
            {"properties": {"a": {"enum": [1]}}},
            {"properties": {"a": {"enum": [1, 2]}}},
            SchemaChangeKind.WIDENED,
        ),
        (
            {"properties": {"a": {"maxLength": 5}}},
            {"properties": {"a": {"maxLength": 6}}},
            SchemaChangeKind.OTHER,
        ),
        (
            {"properties": {"a": {}}},
            {"properties": {"a": {"pattern": "x"}}},
            SchemaChangeKind.NARROWED,
        ),
        (
            {"properties": {"a": {}}},
            {"properties": {"a": {"description": "d"}}},
            SchemaChangeKind.OTHER,
        ),
        ({}, {"additionalProperties": False}, SchemaChangeKind.NARROWED),
        ({"properties": {"a": {}}}, {}, SchemaChangeKind.NARROWED),
        (None, {"type": "object"}, SchemaChangeKind.OTHER),
    ],
)
def test_classify_schema_change(old, new, kind) -> None:  # type: ignore[no-untyped-def]
    assert classify_schema_change(old, new)[0] is kind


def test_supply_chain_signals() -> None:
    a = supply()
    b = supply(
        has_provenance=False,
        has_install_scripts=True,
        install_scripts=["postinstall"],
        maintainer_count=2,
        direct_dependency_count=9,
        repo_linked=False,
    )
    signals = supply_chain_signals(a, b)
    assert len(signals) == 5
    assert supply_chain_signals(a, a) == [] and supply_chain_signals(None, a) == []


async def test_sarif_shape() -> None:
    old, new = await _pair("schema_v1", "schema_widened")
    sarif = to_sarif(diff_servers(old, new), artifact_uri="b.json")
    assert sarif["version"] == "2.1.0"
    [res] = sarif["runs"][0]["results"]
    assert res["ruleId"] == "toolcensus/input_schema_changed"
    assert res["level"] == "warning"
    assert res["locations"][0]["physicalLocation"]["artifactLocation"]["uri"] == "b.json"
