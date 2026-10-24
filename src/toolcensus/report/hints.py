"""Neutral, actionable improvement hints for per-server pages. No grades, no scores."""

from __future__ import annotations

from toolcensus.models import ServerRecord, Status


def improvement_hints(rec: ServerRecord) -> list[str]:
    hints: list[str] = []
    sc = rec.supply_chain
    if sc is not None:
        if not sc.has_provenance:
            hints.append(
                "Consider publishing from CI with npm provenance (`npm publish --provenance`)."
            )
        if sc.has_install_scripts:
            hints.append(
                "Consider whether the install-time script(s) "
                f"({', '.join(sc.install_scripts)}) are necessary; many users install with `--ignore-scripts`."
            )
        if not sc.repo_linked:
            hints.append(
                "Consider adding a `repository` field pointing at the public source repository."
            )
        if not sc.registry_listed:
            hints.append("Consider listing the server in the official MCP Registry.")
    if rec.introspection.status is Status.REQUIRES_CONFIGURATION:
        hints.append(
            "The server did not start without configuration. Consider advertising tool definitions "
            "even when credentials are missing, so clients can inspect them before configuring."
        )
    tools = rec.introspection.tools
    if tools:
        unannotated = [t for t in tools if not t.annotation_metrics.has_any]
        if unannotated:
            hints.append(
                f"Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to "
                f"{len(unannotated)} of {len(tools)} tools."
            )
        loose = [
            t
            for t in tools
            if t.schema_metrics.property_count and not t.schema_metrics.additional_properties_false
        ]
        if loose:
            hints.append(
                f"Consider `additionalProperties: false` on the input schema of {len(loose)} tool(s) "
                "so unexpected arguments are rejected."
            )
        hidden = [t for t in tools if t.description_metrics.invisible_char_count]
        if hidden:
            hints.append(
                f"{len(hidden)} tool definition(s) contain non-printing Unicode code points; "
                "consider removing them."
            )
    return hints
