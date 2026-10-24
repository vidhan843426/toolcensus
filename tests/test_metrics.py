from __future__ import annotations

from datetime import UTC, datetime

from toolcensus.metrics.aggregate import pct, weekly_aggregates
from toolcensus.metrics.annotations import annotation_metrics, name_tokens, suggests_side_effect
from toolcensus.metrics.descriptions import (
    char_category,
    description_metrics,
    redact_invisible,
)
from toolcensus.metrics.schema import schema_metrics
from toolcensus.metrics.supply_chain import install_scripts, supply_chain_metrics


def test_schema_metrics() -> None:
    m = schema_metrics(
        {
            "inputSchema": {
                "type": "object",
                "properties": {
                    "a": {"type": "string", "enum": ["x"]},
                    "b": {"type": "string"},
                    "c": {"description": "untyped"},
                    "d": {"type": ["string", "null"], "format": "uri"},
                },
                "required": ["a"],
                "additionalProperties": False,
            },
            "outputSchema": {"type": "object"},
        }
    )
    assert m.has_input_schema and m.declares_required and m.additional_properties_false
    assert m.property_count == 4
    assert m.typed_property_ratio == 0.75
    assert m.constrained_string_ratio == round(2 / 3, 4)
    assert m.has_output_schema
    empty = schema_metrics({"name": "x"})
    assert not empty.has_input_schema and empty.typed_property_ratio is None
    assert empty.constrained_string_ratio is None


def test_annotations_and_side_effect_heuristic() -> None:
    assert name_tokens("createIssueComment") == ["create", "issue", "comment"]
    assert name_tokens("delete-file_now") == ["delete", "file", "now"]
    assert suggests_side_effect("issue", "Creates an issue")
    assert not suggests_side_effect("get_issue", "Returns an issue")
    m = annotation_metrics({"name": "send_email", "annotations": {"openWorldHint": True}})
    assert m.has_any and m.side_effect_verb and m.side_effect_unannotated
    m2 = annotation_metrics({"name": "send_email", "annotations": {"destructiveHint": False}})
    assert not m2.side_effect_unannotated
    m3 = annotation_metrics({"name": "list"})
    assert not m3.has_any and not m3.side_effect_verb


def test_description_hygiene() -> None:
    text = "ok​ ‮ x \U000e0041 <b>bold</b> <IMPORTANT> ­ ️\U000e0100"
    m = description_metrics({"description": text})
    assert m.invisible_categories == {
        "bidi_control": 1,
        "other_format": 1,
        "tag": 1,
        "variation_selector": 1,
        "zero_width": 1,
    }
    assert m.markup_tag_count == 3
    assert char_category("a") is None and char_category("\x07") == "control"
    assert char_category("") == "private_or_unassigned"
    assert char_category("\n") is None
    redacted, flag = redact_invisible({"a": ["x​", 1], "b": "clean"})
    assert flag and redacted["b"] == "clean" and "​" not in redacted["a"][0]
    assert redact_invisible("clean") == ("clean", False)


PACK = {
    "name": "p",
    "maintainers": [{"name": "a"}, {"name": "b"}],
    "time": {
        "created": "2026-01-01T00:00:00Z",
        "1.0.0": "2026-01-01T00:00:00Z",
        "1.1.0": "2026-08-01T00:00:00Z",
        "1.2.0": "2026-09-01T00:00:00Z",
        "2.0.0": "2026-10-01T00:00:00.000Z",
    },
    "versions": {
        "1.0.0": {"name": "p", "version": "1.0.0"},
        "1.1.0": {"name": "p", "version": "1.1.0"},
        "1.2.0": {"name": "p", "version": "1.2.0", "gypfile": True},
        "2.0.0": {
            "name": "p",
            "version": "2.0.0",
            "scripts": {"postinstall": "node x.js", "test": "jest"},
            "dependencies": {"@modelcontextprotocol/sdk": "^1", "zod": "^3"},
            "repository": {"type": "git", "url": "git+https://github.com/o/p.git"},
            "dist": {"attestations": {"url": "u", "provenance": {"predicateType": "x"}}},
        },
    },
}


def test_supply_chain() -> None:
    m = supply_chain_metrics(
        PACK, "2.0.0", as_of=datetime(2026, 10, 24, tzinfo=UTC), registry_listed=True
    )
    assert m.has_provenance and m.has_install_scripts and m.install_scripts == ["postinstall"]
    assert m.direct_dependency_count == 2 and m.maintainer_count == 2
    assert m.releases_last_90d == 3
    assert m.median_days_between_releases == 31.0
    assert m.repo_linked and m.registry_listed
    old = supply_chain_metrics(
        PACK, "1.0.0", as_of=datetime(2026, 1, 2, tzinfo=UTC), registry_listed=False
    )
    assert (
        not old.has_provenance and not old.repo_linked and old.median_days_between_releases is None
    )
    assert install_scripts(PACK["versions"]["1.2.0"]) == ["install(gypfile)"]


def test_repo_link_patterns() -> None:
    from toolcensus.metrics.supply_chain import _PUBLIC_REPO

    for ok in ["github:o/r", "o/r", "git@github.com:o/r.git", "https://gitlab.com/g/p"]:
        assert _PUBLIC_REPO.search(ok), ok
    for bad in ["https://example.com/o/r", "file:../x", "."]:
        assert not _PUBLIC_REPO.search(bad), bad


async def test_weekly_aggregates() -> None:
    from helpers import fixture_record

    recs = [
        await fixture_record("annotated", package="a"),
        await fixture_record("normal", package="b", has_provenance=False, has_install_scripts=True),
        await fixture_record("crash", package="c"),
    ]
    agg = weekly_aggregates(recs)
    assert agg["servers_measured"] == 3
    assert agg["servers_ok"] == 2
    assert agg["pct_provenance"] == pct(2, 3)
    assert agg["pct_tools_annotated"] == 50.0
    assert agg["pct_servers_all_annotated"] == 50.0
    assert agg["status_crashed"] == 1
    assert agg["pct_tools_readOnlyHint"] == 25.0
    assert pct(1, 0) is None
