"""Pydantic records. Every persisted record carries schema/methodology/tool versions and a timestamp."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from toolcensus import METHODOLOGY_VERSION, SCHEMA_VERSION, __version__


def utcnow() -> datetime:
    return datetime.now(UTC).replace(microsecond=0)


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Versioned(_Model):
    schema_version: str = SCHEMA_VERSION
    methodology_version: str = METHODOLOGY_VERSION
    tool_version: str = __version__
    scanned_at: datetime = Field(default_factory=utcnow)


class Status(StrEnum):
    OK = "ok"
    TIMEOUT = "timeout"
    CRASHED = "crashed"
    REQUIRES_CONFIGURATION = "requires_configuration"
    INSTALL_FAILED = "install_failed"
    NOT_MCP = "not_mcp"


class ObservedVia(StrEnum):
    WEEKLY_SCAN = "weekly_scan"
    BACKFILL = "backfill"
    CHECK = "check"


# --- package level ---------------------------------------------------------------------------


class PackageInfo(_Model):
    ecosystem: str = "npm"
    name: str
    version: str
    published_at: datetime | None = None
    weekly_downloads: int | None = None
    registry_name: str | None = None
    repository_url: str | None = None


class SupplyChainMetrics(_Model):
    has_provenance: bool
    has_install_scripts: bool
    install_scripts: list[str] = Field(default_factory=list)
    direct_dependency_count: int
    maintainer_count: int
    releases_last_90d: int
    median_days_between_releases: float | None
    repo_linked: bool
    registry_listed: bool


# --- tool level ------------------------------------------------------------------------------


class ToolHashes(_Model):
    tool_hash: str
    description_hash: str
    input_schema_hash: str
    output_schema_hash: str
    annotations_hash: str


class SchemaMetrics(_Model):
    has_input_schema: bool
    declares_required: bool
    additional_properties_false: bool
    property_count: int
    typed_property_ratio: float | None
    constrained_string_ratio: float | None
    has_output_schema: bool


class AnnotationMetrics(_Model):
    declared: dict[str, bool]
    has_any: bool
    #: Heuristic (see METHODOLOGY.md 7.4): name/description suggests side effects.
    side_effect_verb: bool
    side_effect_unannotated: bool


class DescriptionMetrics(_Model):
    length: int
    invisible_char_count: int
    invisible_categories: dict[str, int] = Field(default_factory=dict)
    markup_tag_count: int


class ToolRecord(_Model):
    name: str
    #: The full definition exactly as the server sent it (after public-output redaction).
    definition: dict[str, Any]
    redacted: bool = False
    hashes: ToolHashes
    schema_metrics: SchemaMetrics
    annotation_metrics: AnnotationMetrics
    description_metrics: DescriptionMetrics


# --- server level ----------------------------------------------------------------------------


class LaunchInfo(_Model):
    source: str  # "bin" | "registry" | "override" | "local"
    command: list[str]
    placeholder_env: list[str] = Field(default_factory=list)
    install_scripts_ran: bool = False


class Introspection(_Model):
    status: Status
    protocol_version: str | None = None
    server_info: dict[str, Any] | None = None
    capabilities: dict[str, Any] | None = None
    tools: list[ToolRecord] = Field(default_factory=list)
    prompts: list[dict[str, Any]] = Field(default_factory=list)
    resources: list[dict[str, Any]] = Field(default_factory=list)
    resource_templates: list[dict[str, Any]] = Field(default_factory=list)
    surface_hash: str | None = None
    timings_ms: dict[str, float] = Field(default_factory=dict)
    error: str | None = None
    launch: LaunchInfo | None = None


class ServerSummary(_Model):
    tool_count: int
    all_tools_annotated: bool | None
    annotated_tool_ratio: float | None
    side_effect_unannotated_count: int
    tools_with_invisible_chars: int
    tools_with_markup: int


class ServerRecord(Versioned):
    observed_via: ObservedVia
    package: PackageInfo
    supply_chain: SupplyChainMetrics | None = None
    introspection: Introspection
    summary: ServerSummary | None = None


# --- population ------------------------------------------------------------------------------


class PopulationEntry(_Model):
    name: str
    version: str
    weekly_downloads: int
    registry_listed: bool
    registry_name: str | None = None
    sources: list[str]


class ExcludedEntry(_Model):
    name: str
    reason: str


class Population(Versioned):
    week: str
    selection_rule: str
    top_n: int
    packages: list[PopulationEntry]
    excluded: list[ExcludedEntry] = Field(default_factory=list)


# --- diffs -----------------------------------------------------------------------------------


class ChangeType(StrEnum):
    TOOL_ADDED = "tool_added"
    TOOL_REMOVED = "tool_removed"
    DESCRIPTION_CHANGED = "description_changed"
    INPUT_SCHEMA_CHANGED = "input_schema_changed"
    OUTPUT_SCHEMA_CHANGED = "output_schema_changed"
    ANNOTATIONS_CHANGED = "annotations_changed"
    OTHER_CHANGED = "other_changed"


class SchemaChangeKind(StrEnum):
    WIDENED = "schema_widened"
    NARROWED = "schema_narrowed"
    OTHER = "schema_other"


class ChangeRecord(Versioned):
    package: str
    from_version: str
    to_version: str
    version_bumped: bool
    tool: str
    change_type: ChangeType
    schema_change: SchemaChangeKind | None = None
    details: list[str] = Field(default_factory=list)
    from_tool_hash: str | None = None
    to_tool_hash: str | None = None
