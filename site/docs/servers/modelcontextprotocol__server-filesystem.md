# `@modelcontextprotocol/server-filesystem`

| | |
|---|---|
| Latest observed version | `2.3.0` |
| Status | ok |
| Weekly downloads | 1214417 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:323c203d33aeea40` |

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
| `releases_last_90d` | 7 |
| `median_days_between_releases` | 7.98 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (16)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `append_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6ae8b2cb5e21` |
| `copy_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9acfaef32ae2` |
| `create_directory` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fd9b667e92be` |
| `directory_tree` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `16c06e9c19fb` |
| `edit_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `91a68ef5f096` |
| `get_file_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0e61fbcad27f` |
| `list_allowed_directories` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f3b56bff4ea4` |
| `list_directory` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9e3faf2d47e2` |
| `list_directory_with_sizes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1ffdcd6005b4` |
| `move_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `15171f38a47a` |
| `read_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `09f3408a2cbf` |
| `read_media_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `06da1b120459` |
| `read_multiple_files` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c7f1382cbb9e` |
| `read_text_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8f62055a5c1c` |
| `search_files` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b5115581be44` |
| `write_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `46079661b497` |



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
| week 2026-47 | `2.2.0` → `2.3.0` | `append_file` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `create_directory` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `directory_tree` | input_schema_changed (schema_other) | property 'excludePatterns' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `edit_file` | input_schema_changed (schema_other) | property 'edits' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `get_file_info` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `list_directory` | description_changed | length 309 -&gt; 344 |
| week 2026-47 | `2.2.0` → `2.3.0` | `list_directory` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `list_directory_with_sizes` | description_changed | length 323 -&gt; 364 |
| week 2026-47 | `2.2.0` → `2.3.0` | `list_directory_with_sizes` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `move_file` | input_schema_changed (schema_other) | property 'destination' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `read_file` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `read_media_file` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `read_text_file` | input_schema_changed (schema_other) | property 'path' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `search_files` | input_schema_changed (schema_other) | property 'excludePatterns' changed (annotations/descriptions) |
| week 2026-47 | `2.2.0` → `2.3.0` | `write_file` | input_schema_changed (schema_other) | property 'content' changed (annotations/descriptions) |


