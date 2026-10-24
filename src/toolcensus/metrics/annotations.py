"""Tool annotation adoption (METHODOLOGY.md section 7.4).

Annotation names verified against the MCP spec (2025-03-26 onward, unchanged in 2025-11-25).
The side-effect verb check is a *heuristic*: it is only ever reported in aggregate.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from toolcensus.models import AnnotationMetrics

HINTS = ("readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint")

#: Documented in METHODOLOGY.md. Changing this list bumps the methodology version.
SIDE_EFFECT_VERBS = frozenset(
    {
        "add",
        "append",
        "archive",
        "cancel",
        "commit",
        "create",
        "delete",
        "deploy",
        "drop",
        "edit",
        "execute",
        "exec",
        "insert",
        "install",
        "kill",
        "merge",
        "modify",
        "move",
        "patch",
        "post",
        "publish",
        "push",
        "put",
        "remove",
        "rename",
        "replace",
        "restart",
        "run",
        "send",
        "set",
        "submit",
        "terminate",
        "trigger",
        "uninstall",
        "update",
        "upload",
        "upsert",
        "write",
    }
)

_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_SPLIT = re.compile(r"[^A-Za-z0-9]+")


def name_tokens(name: str) -> list[str]:
    return [t.lower() for t in _SPLIT.split(_CAMEL.sub(" ", name)) if t]


def suggests_side_effect(name: str, description: str | None) -> bool:
    if any(tok in SIDE_EFFECT_VERBS for tok in name_tokens(name)):
        return True
    first = name_tokens((description or "").strip().split(" ", 1)[0]) if description else []
    # "Creates a ..." / "Deletes the ..." -> strip a trailing "s"/"es" from the first word.
    return any(tok in SIDE_EFFECT_VERBS or tok.rstrip("s") in SIDE_EFFECT_VERBS for tok in first)


def annotation_metrics(definition: Mapping[str, Any]) -> AnnotationMetrics:
    ann = definition.get("annotations")
    ann = ann if isinstance(ann, dict) else {}
    declared = {h: h in ann for h in HINTS}
    desc = definition.get("description")
    verb = suggests_side_effect(
        str(definition.get("name", "")), desc if isinstance(desc, str) else None
    )
    return AnnotationMetrics(
        declared=declared,
        has_any=any(declared.values()),
        side_effect_verb=verb,
        side_effect_unannotated=verb
        and not (declared["readOnlyHint"] or declared["destructiveHint"]),
    )
