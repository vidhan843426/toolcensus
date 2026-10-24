"""Tool and surface hashes (METHODOLOGY.md section 6.2)."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from toolcensus.models import ToolHashes
from toolcensus.normalize.canonical import jcs_sha256

#: Absent components hash as JSON null so "missing" and "present" are always distinguishable.
_ABSENT = None


def tool_hashes(definition: Mapping[str, Any]) -> ToolHashes:
    return ToolHashes(
        tool_hash=jcs_sha256(dict(definition)),
        description_hash=jcs_sha256(definition.get("description", _ABSENT)),
        input_schema_hash=jcs_sha256(definition.get("inputSchema", _ABSENT)),
        output_schema_hash=jcs_sha256(definition.get("outputSchema", _ABSENT)),
        annotations_hash=jcs_sha256(definition.get("annotations", _ABSENT)),
    )


def surface_hash(pairs: Iterable[tuple[str, str]]) -> str:
    """Hash of the sorted ``[name, tool_hash]`` list for a whole server."""
    return jcs_sha256(sorted([name, h] for name, h in pairs))
