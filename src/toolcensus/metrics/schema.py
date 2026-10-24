"""Schema strictness metrics (METHODOLOGY.md section 7.3). Top-level properties only."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from toolcensus.models import SchemaMetrics

STRING_CONSTRAINTS = ("enum", "const", "pattern", "format", "maxLength")


def _is_string_prop(prop: Mapping[str, Any]) -> bool:
    t = prop.get("type")
    return t == "string" or (isinstance(t, list) and "string" in t)


def _ratio(num: int, den: int) -> float | None:
    return round(num / den, 4) if den else None


def schema_metrics(definition: Mapping[str, Any]) -> SchemaMetrics:
    schema = definition.get("inputSchema")
    has_schema = isinstance(schema, dict)
    schema = schema if isinstance(schema, dict) else {}
    props = schema.get("properties")
    props = (
        {k: v for k, v in props.items() if isinstance(v, dict)} if isinstance(props, dict) else {}
    )
    required = schema.get("required")
    strings = [p for p in props.values() if _is_string_prop(p)]
    return SchemaMetrics(
        has_input_schema=has_schema,
        declares_required=isinstance(required, list) and len(required) > 0,
        additional_properties_false=schema.get("additionalProperties") is False,
        property_count=len(props),
        typed_property_ratio=_ratio(sum(1 for p in props.values() if "type" in p), len(props)),
        constrained_string_ratio=_ratio(
            sum(1 for p in strings if any(c in p for c in STRING_CONSTRAINTS)), len(strings)
        ),
        has_output_schema=isinstance(definition.get("outputSchema"), dict),
    )
