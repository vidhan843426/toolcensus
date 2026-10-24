"""ToolCensus: reproducible security-hygiene measurement of the public MCP server ecosystem."""

__version__ = "0.1.0"

#: Bump (semver) whenever the definition of any metric changes. Recorded in every snapshot.
METHODOLOGY_VERSION = "1.0.0"

#: Bump whenever the shape of a stored record changes.
SCHEMA_VERSION = "1.0.0"

REPO_URL = "https://github.com/vidhan843426/toolcensus"
USER_AGENT = f"toolcensus/{__version__} (+{REPO_URL})"
