# `@modelcontextprotocol/server-filesystem`

| | |
|---|---|
| Latest observed version | `2.2.0` |
| Status | ok |
| Weekly downloads | 1352654 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:32e2c4cc85f3ee7f` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 15 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 4 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 6 |
| `median_days_between_releases` | 8.17 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (16)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `append_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3ae904df05c7` |
| `copy_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9acfaef32ae2` |
| `create_directory` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c736eae545b2` |
| `directory_tree` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `da0a85bc8860` |
| `edit_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9e1db8ed7c22` |
| `get_file_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b12f1cd916d5` |
| `list_allowed_directories` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f3b56bff4ea4` |
| `list_directory` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f9c4133df4f5` |
| `list_directory_with_sizes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `33df27bfd759` |
| `move_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `df5d8cc5da5a` |
| `read_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `70e04a7ed49f` |
| `read_media_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ca4f3132d7d9` |
| `read_multiple_files` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c7f1382cbb9e` |
| `read_text_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6cd40d5ac547` |
| `search_files` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c5b8c125f952` |
| `write_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `af64d19ac275` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `2.0.1` → `2.1.0` | `get_file_info` | description_changed | length 296 -&gt; 312 |
| week 2026-46 | `2.1.0` → `2.2.0` | `append_file` | tool_added |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `copy_file` | tool_added |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `directory_tree` | description_changed | length 360 -&gt; 474 |
| week 2026-46 | `2.1.0` → `2.2.0` | `directory_tree` | input_schema_changed (schema_widened) | property 'depth' added (optional) |
| week 2026-46 | `2.1.0` → `2.2.0` | `directory_tree` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `edit_file` | description_changed | length 185 -&gt; 693 |
| week 2026-46 | `2.1.0` → `2.2.0` | `get_file_info` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `list_allowed_directories` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `list_directory` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `list_directory_with_sizes` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_file` | input_schema_changed (schema_other) | property 'head': minimum added; property 'head': maximum added; property 'tail': minimum added; property 'tail': maximum added; property 'head': type changed; property 'tail': type changed |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_file` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_media_file` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_multiple_files` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_text_file` | input_schema_changed (schema_other) | property 'head': minimum added; property 'head': maximum added; property 'tail': minimum added; property 'tail': maximum added; property 'head': type changed; property 'tail': type changed |
| week 2026-46 | `2.1.0` → `2.2.0` | `read_text_file` | annotations_changed |  |
| week 2026-46 | `2.1.0` → `2.2.0` | `search_files` | description_changed | length 424 -&gt; 473 |
| week 2026-46 | `2.1.0` → `2.2.0` | `search_files` | annotations_changed |  |


