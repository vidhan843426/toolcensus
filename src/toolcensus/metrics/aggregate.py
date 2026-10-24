"""Population-level aggregates (counts, percentages, medians)."""

from __future__ import annotations

import statistics
from collections import Counter
from collections.abc import Iterable, Sequence
from datetime import datetime

from toolcensus.metrics.annotations import HINTS
from toolcensus.models import ChangeRecord, ServerRecord, Status


def pct(num: int, den: int) -> float | None:
    return round(100 * num / den, 1) if den else None


def weekly_aggregates(
    records: Sequence[ServerRecord], changes: Iterable[ChangeRecord] = ()
) -> dict[str, float | int | None]:
    n = len(records)
    status = Counter(r.introspection.status for r in records)
    ok = [r for r in records if r.introspection.status is Status.OK]
    sc = [r.supply_chain for r in records if r.supply_chain is not None]
    tools = [t for r in ok for t in r.introspection.tools]
    with_tools = [r for r in ok if r.introspection.tools]
    changed_pkgs = {c.package for c in changes}

    out: dict[str, float | int | None] = {
        "servers_measured": n,
        "servers_ok": len(ok),
        "pct_ok_or_classified": pct(sum(status.values()), n),
        "pct_ok": pct(len(ok), n),
        "tools_measured": len(tools),
        "median_tools_per_server": statistics.median([len(r.introspection.tools) for r in ok])
        if ok
        else None,
        "pct_provenance": pct(sum(s.has_provenance for s in sc), len(sc)),
        "pct_install_scripts": pct(sum(s.has_install_scripts for s in sc), len(sc)),
        "pct_repo_linked": pct(sum(s.repo_linked for s in sc), len(sc)),
        "pct_registry_listed": pct(sum(s.registry_listed for s in sc), len(sc)),
        "median_direct_dependencies": statistics.median([s.direct_dependency_count for s in sc])
        if sc
        else None,
        "pct_tools_annotated": pct(sum(t.annotation_metrics.has_any for t in tools), len(tools)),
        "pct_servers_all_annotated": pct(
            sum(
                1
                for r in with_tools
                if all(t.annotation_metrics.has_any for t in r.introspection.tools)
            ),
            len(with_tools),
        ),
        "pct_tools_side_effect_unannotated": pct(
            sum(t.annotation_metrics.side_effect_unannotated for t in tools), len(tools)
        ),
        "pct_tools_declares_required": pct(
            sum(t.schema_metrics.declares_required for t in tools), len(tools)
        ),
        "pct_tools_additional_properties_false": pct(
            sum(t.schema_metrics.additional_properties_false for t in tools), len(tools)
        ),
        "pct_tools_output_schema": pct(
            sum(t.schema_metrics.has_output_schema for t in tools), len(tools)
        ),
        "pct_tools_invisible_chars": pct(
            sum(1 for t in tools if t.description_metrics.invisible_char_count), len(tools)
        ),
        "pct_tools_markup": pct(
            sum(1 for t in tools if t.description_metrics.markup_tag_count), len(tools)
        ),
        "median_description_length": statistics.median(
            [t.description_metrics.length for t in tools]
        )
        if tools
        else None,
        "pct_servers_changed": pct(len(changed_pkgs & {r.package.name for r in ok}), len(ok)),
    }
    for hint in HINTS:
        out[f"pct_tools_{hint}"] = pct(
            sum(t.annotation_metrics.declared[hint] for t in tools), len(tools)
        )
    for st in Status:
        out[f"status_{st.value}"] = status.get(st, 0)
    return out


def month_of(dt: datetime) -> str:
    return dt.strftime("%Y-%m")
