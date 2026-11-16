# `@mastergo/magic-mcp`

| | |
|---|---|
| Latest observed version | `0.2.18` |
| Status | ok |
| Weekly downloads | 14476 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:de6b94e4e33f4e7d` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 14 of 14 tools.
    - Consider `additionalProperties: false` on the input schema of 13 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 8 |
| `releases_last_90d` | 10 |
| `median_days_between_releases` | 3.84 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (14)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `mcp__C2d` | — | yes | no | `753142992f02` |
| `mcp__applyDesign` | — | yes | no | `af7caad12cde` |
| `mcp__downloadExportAssets` | — | no | no | `006c6538b711` |
| `mcp__extractSvg` | — | no | no | `a726a3b887b9` |
| `mcp__getComponentGenerator` | — | yes | no | `76a47a8e121e` |
| `mcp__getComponentLink` | — | yes | no | `549d3d436a35` |
| `mcp__getD2c` | — | yes | no | `db4c701a7b22` |
| `mcp__getDesignSections` | — | no | no | `c0034e9d711a` |
| `mcp__getDsl` | — | no | no | `c66a9c5d203b` |
| `mcp__getExportList` | — | no | no | `09b3b0da83d7` |
| `mcp__getFlutterGenerator` | — | yes | no | `407cfad42660` |
| `mcp__getMeta` | — | yes | no | `05381ddce79d` |
| `mcp__getPageLayers` | — | no | no | `de96cc8660fd` |
| `version_0_2_18` | — | no | no | `b57f742ad67f` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__downloadExportAssets` | tool_added |  |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getExportList` | tool_added |  |
| week 2026-47 | `0.2.15` → `0.2.18` | `version_0_2_18` | tool_added |  |
| week 2026-47 | `0.2.15` → `0.2.18` | `version_0_2_15` | tool_removed |  |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__C2d` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__applyDesign` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__extractSvg` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getComponentGenerator` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getComponentLink` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getD2c` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getDesignSections` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getDsl` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getFlutterGenerator` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getMeta` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `0.2.15` → `0.2.18` | `mcp__getPageLayers` | input_schema_changed (schema_widened) | additionalProperties loosened |


