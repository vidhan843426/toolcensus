# `@modelcontextprotocol/server-filesystem`

| | |
|---|---|
| Latest observed version | `2.0.1` |
| Status | ok |
| Weekly downloads | 395900 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:69b3e7744b7f5a85` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 13 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 4 |
| `median_days_between_releases` | 18.0 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (14)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `create_directory` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c736eae545b2` |
| `directory_tree` | openWorldHint, readOnlyHint | yes | no | `17f792a5284a` |
| `edit_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `64394ff801f9` |
| `get_file_info` | openWorldHint, readOnlyHint | yes | no | `1d8585f3d596` |
| `list_allowed_directories` | openWorldHint, readOnlyHint | no | no | `3ca0e52085e6` |
| `list_directory` | openWorldHint, readOnlyHint | yes | no | `d8f41bcca189` |
| `list_directory_with_sizes` | openWorldHint, readOnlyHint | yes | no | `2f5447f34154` |
| `move_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `df5d8cc5da5a` |
| `read_file` | openWorldHint, readOnlyHint | yes | no | `2072073670c6` |
| `read_media_file` | openWorldHint, readOnlyHint | yes | no | `be345da6f6ce` |
| `read_multiple_files` | openWorldHint, readOnlyHint | yes | no | `583249302614` |
| `read_text_file` | openWorldHint, readOnlyHint | yes | no | `a853d369e3b7` |
| `search_files` | openWorldHint, readOnlyHint | yes | no | `0fca7199c50b` |
| `write_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `af64d19ac275` |



## Change history

No tool-definition changes observed.
