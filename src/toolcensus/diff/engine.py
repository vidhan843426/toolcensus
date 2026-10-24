"""Compare two observations of the same server and classify each tool change (METHODOLOGY 7.2)."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from toolcensus.metrics.descriptions import redact_invisible
from toolcensus.metrics.schema import STRING_CONSTRAINTS
from toolcensus.models import (
    ChangeRecord,
    ChangeType,
    SchemaChangeKind,
    ServerRecord,
    Status,
    SupplyChainMetrics,
    ToolRecord,
)

_CONSTRAINTS = (*STRING_CONSTRAINTS, "minLength", "minimum", "maximum", "minItems", "maxItems")


def _safe(text: str) -> str:
    return str(redact_invisible(text)[0])


def _obj(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _types(prop: Mapping[str, Any]) -> set[str]:
    t = prop.get("type")
    return {t} if isinstance(t, str) else set(map(str, t)) if isinstance(t, list) else set()


def classify_schema_change(old: Any, new: Any) -> tuple[SchemaChangeKind, list[str]]:
    """Top-level comparison of two input schemas. Mixed or unclassifiable -> ``schema_other``."""
    o, n = _obj(old), _obj(new)
    op, np_ = _obj(o.get("properties")), _obj(n.get("properties"))
    oreq = set(o.get("required") or []) if isinstance(o.get("required"), list) else set()
    nreq = set(n.get("required") or []) if isinstance(n.get("required"), list) else set()
    wider: list[str] = []
    narrower: list[str] = []
    other: list[str] = []

    for name in sorted(np_.keys() - op.keys()):
        (narrower if name in nreq else wider).append(
            f"property '{name}' added ({'required' if name in nreq else 'optional'})"
        )
    for name in sorted(op.keys() - np_.keys()):
        narrower.append(f"property '{name}' removed")
    for name in sorted(oreq - nreq):
        if name in np_:
            wider.append(f"property '{name}' no longer required")
    for name in sorted((nreq - oreq) & op.keys()):
        narrower.append(f"property '{name}' now required")

    o_ap, n_ap = o.get("additionalProperties"), n.get("additionalProperties")
    if o_ap is False and n_ap is not False:
        wider.append("additionalProperties loosened")
    elif o_ap is not False and n_ap is False:
        narrower.append("additionalProperties set to false")

    for name in sorted(op.keys() & np_.keys()):
        a, b = _obj(op[name]), _obj(np_[name])
        if a == b:
            continue
        before = len(wider) + len(narrower)
        if "enum" in a and "enum" not in b:
            wider.append(f"property '{name}': enum constraint removed")
        elif "enum" not in a and "enum" in b:
            narrower.append(f"property '{name}': enum constraint added")
        elif isinstance(a.get("enum"), list) and isinstance(b.get("enum"), list):
            ea, eb = set(map(repr, a["enum"])), set(map(repr, b["enum"]))
            if eb - ea:
                wider.append(f"property '{name}': enum values added")
            if ea - eb:
                narrower.append(f"property '{name}': enum values removed")
        ta, tb = _types(a), _types(b)
        if ta != tb:
            if ta and tb and ta < tb:
                wider.append(f"property '{name}': type widened")
            elif ta and tb and tb < ta:
                narrower.append(f"property '{name}': type narrowed")
            else:
                other.append(f"property '{name}': type changed")
        for c in _CONSTRAINTS:
            if c == "enum":
                continue
            if c in a and c not in b:
                wider.append(f"property '{name}': {c} removed")
            elif c not in a and c in b:
                narrower.append(f"property '{name}': {c} added")
            elif c in a and a[c] != b[c]:
                other.append(f"property '{name}': {c} changed")
        if len(wider) + len(narrower) == before and not other:
            other.append(f"property '{name}' changed (annotations/descriptions)")

    details = [_safe(d) for d in wider + narrower + other]
    if wider and not narrower and not other:
        return SchemaChangeKind.WIDENED, details
    if narrower and not wider and not other:
        return SchemaChangeKind.NARROWED, details
    return SchemaChangeKind.OTHER, details or ["schema changed"]


def diff_tools(
    old: Iterable[ToolRecord],
    new: Iterable[ToolRecord],
    *,
    package: str,
    from_version: str,
    to_version: str,
) -> list[ChangeRecord]:
    om = {t.name: t for t in old}
    nm = {t.name: t for t in new}
    out: list[ChangeRecord] = []

    def add(
        name: str,
        change_type: ChangeType,
        *,
        before: ToolRecord | None = None,
        after: ToolRecord | None = None,
        schema_change: SchemaChangeKind | None = None,
        details: list[str] | None = None,
    ) -> None:
        out.append(
            ChangeRecord(
                package=package,
                from_version=from_version,
                to_version=to_version,
                version_bumped=from_version != to_version,
                tool=_safe(name),
                change_type=change_type,
                schema_change=schema_change,
                details=details or [],
                from_tool_hash=before.hashes.tool_hash if before else None,
                to_tool_hash=after.hashes.tool_hash if after else None,
            )
        )

    for name in sorted(nm.keys() - om.keys()):
        add(name, ChangeType.TOOL_ADDED, after=nm[name])
    for name in sorted(om.keys() - nm.keys()):
        add(name, ChangeType.TOOL_REMOVED, before=om[name])
    for name in sorted(om.keys() & nm.keys()):
        a, b = om[name], nm[name]
        if a.hashes.tool_hash == b.hashes.tool_hash:
            continue
        n_before = len(out)
        if a.hashes.description_hash != b.hashes.description_hash:
            length = f"length {a.description_metrics.length} -> {b.description_metrics.length}"
            add(name, ChangeType.DESCRIPTION_CHANGED, before=a, after=b, details=[length])
        if a.hashes.input_schema_hash != b.hashes.input_schema_hash:
            kind, details = classify_schema_change(
                a.definition.get("inputSchema"), b.definition.get("inputSchema")
            )
            add(
                name,
                ChangeType.INPUT_SCHEMA_CHANGED,
                before=a,
                after=b,
                schema_change=kind,
                details=details,
            )
        if a.hashes.output_schema_hash != b.hashes.output_schema_hash:
            add(name, ChangeType.OUTPUT_SCHEMA_CHANGED, before=a, after=b)
        if a.hashes.annotations_hash != b.hashes.annotations_hash:
            add(name, ChangeType.ANNOTATIONS_CHANGED, before=a, after=b)
        if len(out) == n_before:
            add(
                name,
                ChangeType.OTHER_CHANGED,
                before=a,
                after=b,
                details=["title or other top-level field changed"],
            )
    return out


def diff_servers(old: ServerRecord, new: ServerRecord) -> list[ChangeRecord]:
    if old.introspection.status is not Status.OK or new.introspection.status is not Status.OK:
        return []
    if old.introspection.surface_hash == new.introspection.surface_hash:
        return []
    return diff_tools(
        old.introspection.tools,
        new.introspection.tools,
        package=new.package.name,
        from_version=old.package.version,
        to_version=new.package.version,
    )


def diff_snapshots(
    old: Iterable[ServerRecord], new: Iterable[ServerRecord], *, package: str | None = None
) -> list[ChangeRecord]:
    om = {r.package.name: r for r in old}
    out: list[ChangeRecord] = []
    for rec in new:
        if package and rec.package.name != package:
            continue
        prev = om.get(rec.package.name)
        if prev is not None:
            out.extend(diff_servers(prev, rec))
    return out


def drift_without_bump(old: Iterable[ServerRecord], new: Iterable[ServerRecord]) -> list[str]:
    """Packages whose version string is unchanged but whose tool surface hash differs."""
    om = {r.package.name: r for r in old}
    return sorted(
        r.package.name
        for r in new
        if (p := om.get(r.package.name)) is not None
        and p.package.version == r.package.version
        and p.introspection.surface_hash
        and r.introspection.surface_hash
        and p.introspection.surface_hash != r.introspection.surface_hash
    )


def supply_chain_signals(
    old: SupplyChainMetrics | None, new: SupplyChainMetrics | None
) -> list[str]:
    """Neutral package-level changes between two versions (used by backtesting)."""
    if old is None or new is None:
        return []
    out = []
    if old.has_provenance and not new.has_provenance:
        out.append("provenance attestation no longer present")
    if set(new.install_scripts) - set(old.install_scripts):
        out.append(
            "install script(s) added: "
            + ", ".join(sorted(set(new.install_scripts) - set(old.install_scripts)))
        )
    if new.maintainer_count != old.maintainer_count:
        out.append(f"maintainer count {old.maintainer_count} -> {new.maintainer_count}")
    if new.direct_dependency_count > old.direct_dependency_count:
        out.append(
            f"direct dependencies {old.direct_dependency_count} -> {new.direct_dependency_count}"
        )
    if old.repo_linked and not new.repo_linked:
        out.append("repository link no longer present")
    return out
