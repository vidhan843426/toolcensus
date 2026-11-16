# `@next-ai-drawio/mcp-server`

| | |
|---|---|
| Latest observed version | `0.4.15` |
| Status | ok |
| Weekly downloads | 34374 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.DayuanJiang/next-ai-drawio |
| Surface hash | `sha256:3d013c6aca885c91` |

!!! tip "Improvement hints"
    - Consider `additionalProperties: false` on the input schema of 13 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 6 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 17 |
| `median_days_between_releases` | 1.43 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (16)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_page` | destructiveHint, openWorldHint | no | no | `1a4c54e3facf` |
| `create_new_diagram` | openWorldHint | yes | no | `294307f1f8b8` |
| `delete_page` | openWorldHint | no | no | `a237bd7f4d61` |
| `edit_diagram` | openWorldHint | yes | no | `5c782ba37b5b` |
| `export_diagram` | openWorldHint | yes | no | `fe4e5fd0ef58` |
| `get_diagram` | openWorldHint, readOnlyHint | no | no | `7ae7fa7d7538` |
| `get_drawing_guide` | openWorldHint, readOnlyHint | no | no | `117c02086cb3` |
| `get_selection` | openWorldHint, readOnlyHint | no | no | `db84dd7111c9` |
| `get_shape_library` | openWorldHint, readOnlyHint | yes | no | `e0d54ae9e714` |
| `list_pages` | openWorldHint, readOnlyHint | no | no | `fa879e04f069` |
| `list_saved_diagrams` | openWorldHint, readOnlyHint | no | no | `560e7abb2b38` |
| `load_diagram` | openWorldHint | no | no | `5432609647ac` |
| `rename_page` | destructiveHint, openWorldHint | yes | no | `ac995064af34` |
| `restore_version` | destructiveHint, openWorldHint | no | no | `78869835711b` |
| `screenshot_diagram` | openWorldHint, readOnlyHint | no | no | `4a0957498d7c` |
| `start_session` | destructiveHint, openWorldHint | no | no | `126f6844565d` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-47 | `0.4.13` → `0.4.15` | `add_page` | input_schema_changed (schema_widened) | property 'type' added (optional) |
| week 2026-47 | `0.4.13` → `0.4.15` | `create_new_diagram` | input_schema_changed (schema_widened) | property 'type' added (optional) |
| week 2026-47 | `0.4.13` → `0.4.15` | `edit_diagram` | input_schema_changed (schema_other) | property 'operations' changed (annotations/descriptions) |
| week 2026-47 | `0.4.13` → `0.4.15` | `export_diagram` | description_changed | length 899 -&gt; 947 |
| week 2026-47 | `0.4.13` → `0.4.15` | `export_diagram` | input_schema_changed (schema_other) | property 'path': minLength added; property 'transparent' changed (annotations/descriptions) |
| week 2026-47 | `0.4.13` → `0.4.15` | `get_drawing_guide` | description_changed | length 248 -&gt; 387 |
| week 2026-47 | `0.4.13` → `0.4.15` | `get_drawing_guide` | input_schema_changed (schema_widened) | property 'topic': enum constraint removed |
| week 2026-47 | `0.4.13` → `0.4.15` | `start_session` | description_changed | length 297 -&gt; 372 |


