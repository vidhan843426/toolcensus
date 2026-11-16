# `@statelyai/mcp`

| | |
|---|---|
| Latest observed version | `0.28.1` |
| Status | ok |
| Weekly downloads | 51238 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:ed043f5abd7039d1` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 20 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 41 |
| `median_days_between_releases` | 1.46 |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (22)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `apply_machine_patches` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b4c85cb01bfd` |
| `check_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2a2102915f5d` |
| `convert_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3b2c01d86b7e` |
| `diff_machines` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f3c6c3e3eaca` |
| `export_machine_image` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f1f9670b742c` |
| `extract_machines_from_code` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `83f4db543ac5` |
| `generate_graph_paths` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `9b6a52fb523a` |
| `get_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6905b7a9903a` |
| `get_stately_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f5b370cb5964` |
| `get_stately_project` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a8a79ca33bf3` |
| `list_machines` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `1b4d76f1ebde` |
| `list_stately_project_machines` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6d955bf57086` |
| `list_stately_projects` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `770ef148015b` |
| `read_visualization_workspace` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ea2ab2f4979c` |
| `report_visualization_rendered` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `dce0ca763b82` |
| `review_machine_implementation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3f31f05192cd` |
| `simulate_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5bf0384c0f3c` |
| `update_visualization_workspace` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `33fe71fb589b` |
| `validate_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f7712c4cde0d` |
| `visualize_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `28ba6a6b996a` |
| `visualize_machines` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `bde42f5c5a32` |
| `visualize_stately_machine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0d32a2e2fade` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `0.21.0` → `0.23.0` | `read_visualization_workspace` | tool_added |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `update_visualization_workspace` | tool_added |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `visualize_machines` | tool_added |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `analyze_stately_test_report` | tool_removed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `coverage_report` | tool_removed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `generate_test_paths` | tool_removed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `get_stately_testing_guidance` | tool_removed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `verify` | tool_removed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `get_stately_machine` | output_schema_changed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `get_stately_project` | output_schema_changed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `list_stately_project_machines` | output_schema_changed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `list_stately_projects` | output_schema_changed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `visualize_machine` | input_schema_changed (schema_widened) | property 'focus' added (optional); property 'machineId' added (optional); property 'name' added (optional); property 'workspaceId' added (optional) |
| week 2026-45 | `0.21.0` → `0.23.0` | `visualize_machine` | output_schema_changed |  |
| week 2026-45 | `0.21.0` → `0.23.0` | `visualize_stately_machine` | output_schema_changed |  |
| week 2026-46 | `0.23.0` → `0.26.1` | `apply_machine_patches` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `convert_machine` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `diff_machines` | input_schema_changed (schema_other) | property 'base' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `generate_graph_paths` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `read_visualization_workspace` | other_changed | title or other top-level field changed |
| week 2026-46 | `0.23.0` → `0.26.1` | `review_machine_implementation` | input_schema_changed (schema_other) | property 'base' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `simulate_machine` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `validate_machine` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `visualize_machine` | input_schema_changed (schema_other) | property 'source' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `visualize_machines` | input_schema_changed (schema_other) | property 'models' changed (annotations/descriptions) |
| week 2026-46 | `0.23.0` → `0.26.1` | `visualize_stately_machine` | other_changed | title or other top-level field changed |
| week 2026-47 | `0.26.1` → `0.28.1` | `check_machine` | tool_added |  |
| week 2026-47 | `0.26.1` → `0.28.1` | `export_machine_image` | tool_added |  |
| week 2026-47 | `0.26.1` → `0.28.1` | `get_stately_project` | output_schema_changed |  |
| week 2026-47 | `0.26.1` → `0.28.1` | `list_stately_projects` | output_schema_changed |  |
| week 2026-47 | `0.26.1` → `0.28.1` | `read_visualization_workspace` | other_changed | title or other top-level field changed |
| week 2026-47 | `0.26.1` → `0.28.1` | `visualize_machine` | output_schema_changed |  |
| week 2026-47 | `0.26.1` → `0.28.1` | `visualize_machines` | other_changed | title or other top-level field changed |
| week 2026-47 | `0.26.1` → `0.28.1` | `visualize_stately_machine` | output_schema_changed |  |


