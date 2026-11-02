# `obsidian-mcp-server`

| | |
|---|---|
| Latest observed version | `3.8.0` |
| Status | ok |
| Weekly downloads | 10513 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.cyanheads/obsidian-mcp-server |
| Surface hash | `sha256:1efff975a8dd91e7` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 9 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 15 |
| `median_days_between_releases` | 1.22 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (12)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `obsidian_append_to_note` | destructiveHint | yes | yes | `94c6dfed68b6` |
| `obsidian_delete_note` | destructiveHint | yes | yes | `c19961352b1b` |
| `obsidian_get_note` | idempotentHint, readOnlyHint | yes | yes | `8329117694d3` |
| `obsidian_list_notes` | idempotentHint, readOnlyHint | no | yes | `ae697c55d190` |
| `obsidian_list_tags` | idempotentHint, readOnlyHint | no | yes | `dbc9dbe330a3` |
| `obsidian_manage_frontmatter` | destructiveHint | yes | yes | `fa91c120d052` |
| `obsidian_manage_tags` | destructiveHint | yes | yes | `44657c4e5ddf` |
| `obsidian_open_in_ui` | destructiveHint, idempotentHint, openWorldHint | yes | yes | `e180831fd5b7` |
| `obsidian_patch_note` | destructiveHint | yes | yes | `cbd889bc35bc` |
| `obsidian_replace_in_note` | destructiveHint | yes | yes | `6c02122b7adf` |
| `obsidian_search_notes` | idempotentHint, readOnlyHint | yes | yes | `1a696f3ebeff` |
| `obsidian_write_note` | destructiveHint, idempotentHint | yes | yes | `a66ebd371f95` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_append_to_note` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_delete_note` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_get_note` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_list_notes` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_list_tags` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_manage_frontmatter` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_manage_tags` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_open_in_ui` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_patch_note` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_replace_in_note` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_search_notes` | input_schema_changed (schema_other) | property 'cursor' changed (annotations/descriptions) |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_search_notes` | output_schema_changed |  |
| week 2026-45 | `3.7.2` → `3.8.0` | `obsidian_write_note` | output_schema_changed |  |


