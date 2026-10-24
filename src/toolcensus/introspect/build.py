"""Turn a raw introspection into public records: hashes, metrics and redaction."""

from __future__ import annotations

from typing import Any

from toolcensus.introspect.collect import RawIntrospection
from toolcensus.metrics.annotations import annotation_metrics
from toolcensus.metrics.descriptions import description_metrics, redact_invisible
from toolcensus.metrics.schema import schema_metrics
from toolcensus.models import Introspection, LaunchInfo, ServerSummary, Status, ToolRecord
from toolcensus.normalize.toolhash import surface_hash, tool_hashes
from toolcensus.privacy import PrivateSink


def build_tool_record(definition: dict[str, Any]) -> tuple[ToolRecord, bool]:
    """Hashes and metrics are computed on the *original*; only the stored copy is redacted."""
    public_def, redacted = redact_invisible(definition)
    record = ToolRecord(
        name=str(definition.get("name", "")) if not redacted else str(public_def.get("name", "")),
        definition=public_def,
        redacted=redacted,
        hashes=tool_hashes(definition),
        schema_metrics=schema_metrics(definition),
        annotation_metrics=annotation_metrics(definition),
        description_metrics=description_metrics(definition),
    )
    return record, redacted


def summarize(tools: list[ToolRecord]) -> ServerSummary:
    n = len(tools)
    annotated = sum(1 for t in tools if t.annotation_metrics.has_any)
    return ServerSummary(
        tool_count=n,
        all_tools_annotated=(annotated == n) if n else None,
        annotated_tool_ratio=round(annotated / n, 4) if n else None,
        side_effect_unannotated_count=sum(
            1 for t in tools if t.annotation_metrics.side_effect_unannotated
        ),
        tools_with_invisible_chars=sum(
            1 for t in tools if t.description_metrics.invisible_char_count
        ),
        tools_with_markup=sum(1 for t in tools if t.description_metrics.markup_tag_count),
    )


def build_introspection(
    raw: RawIntrospection,
    *,
    launch: LaunchInfo | None,
    package: str,
    version: str,
    private: PrivateSink,
) -> Introspection:
    status = raw.status
    if status is Status.CRASHED and launch is not None and launch.placeholder_env:
        # It needed configuration we deliberately did not provide.
        status = Status.REQUIRES_CONFIGURATION
    intro = Introspection(status=status, error=raw.error, timings_ms=raw.timings_ms, launch=launch)
    if raw.result is None:
        return intro

    init = raw.result["initialize"]
    tools: list[ToolRecord] = []
    for definition in raw.result["tools"]:
        record, redacted = build_tool_record(definition)
        tools.append(record)
        if redacted:
            private.record(
                package=package,
                version=version,
                kind="non_printing_code_points",
                payload={"tool": definition.get("name"), "definition": definition},
            )

    def clean(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [redact_invisible(i)[0] for i in items]

    server_info, _ = redact_invisible(init.get("serverInfo"))
    intro.protocol_version = init.get("protocolVersion")
    intro.server_info = server_info if isinstance(server_info, dict) else None
    intro.capabilities = (
        init.get("capabilities") if isinstance(init.get("capabilities"), dict) else {}
    )
    intro.tools = sorted(tools, key=lambda t: t.name)
    intro.prompts = clean(raw.result["prompts"])
    intro.resources = clean(raw.result["resources"])
    intro.resource_templates = clean(raw.result["resource_templates"])
    intro.surface_hash = surface_hash((t.name, t.hashes.tool_hash) for t in tools)
    return intro
