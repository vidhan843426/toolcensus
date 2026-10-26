# `obsidian-mcp-server`

| | |
|---|---|
| Latest observed version | `3.7.2` |
| Status | ok |
| Weekly downloads | 8428 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.cyanheads/obsidian-mcp-server |
| Surface hash | `sha256:df327c7c4fff6ef4` |

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
| `releases_last_90d` | 17 |
| `median_days_between_releases` | 1.21 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (12)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `obsidian_append_to_note` | destructiveHint | yes | yes | `13359a871a99` |
| `obsidian_delete_note` | destructiveHint | yes | yes | `0b8f1061c7d8` |
| `obsidian_get_note` | idempotentHint, readOnlyHint | yes | yes | `4705bc27f3fe` |
| `obsidian_list_notes` | idempotentHint, readOnlyHint | no | yes | `d5b24cb0d04e` |
| `obsidian_list_tags` | idempotentHint, readOnlyHint | no | yes | `24f9a38eb817` |
| `obsidian_manage_frontmatter` | destructiveHint | yes | yes | `858c39bde51b` |
| `obsidian_manage_tags` | destructiveHint | yes | yes | `fa077268a8eb` |
| `obsidian_open_in_ui` | destructiveHint, idempotentHint, openWorldHint | yes | yes | `662b33c67534` |
| `obsidian_patch_note` | destructiveHint | yes | yes | `247e9d9b5099` |
| `obsidian_replace_in_note` | destructiveHint | yes | yes | `2e0341fbbe5a` |
| `obsidian_search_notes` | idempotentHint, readOnlyHint | yes | yes | `0eb315047725` |
| `obsidian_write_note` | destructiveHint, idempotentHint | yes | yes | `f997d7963e32` |



## Change history

No tool-definition changes observed.
