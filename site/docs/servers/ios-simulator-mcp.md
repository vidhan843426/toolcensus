# `ios-simulator-mcp`

| | |
|---|---|
| Latest observed version | `2.2.1` |
| Status | ok |
| Weekly downloads | 14684 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:b8aa1c0c8c905c46` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 14 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 2 |
| `median_days_between_releases` | 13.68 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (17)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `get_booted_sim_id` | openWorldHint, readOnlyHint | no | no | `02109ead8d54` |
| `install_app` | openWorldHint, readOnlyHint | yes | no | `2d1cfc40e0a3` |
| `launch_app` | openWorldHint, readOnlyHint | yes | no | `66b19d01e99f` |
| `list_apps` | openWorldHint, readOnlyHint | no | no | `a02a75ec25e2` |
| `open_simulator` | openWorldHint, readOnlyHint | no | no | `0d0cd18f1d32` |
| `open_url` | openWorldHint, readOnlyHint | yes | no | `5d533810d3b7` |
| `record_video` | openWorldHint, readOnlyHint | no | no | `cc92cd529e1f` |
| `screenshot` | openWorldHint, readOnlyHint | yes | no | `0a5ffe5fb6c3` |
| `stop_recording` | openWorldHint, readOnlyHint | no | no | `362f10d9fde3` |
| `terminate_app` | openWorldHint, readOnlyHint | yes | no | `e44b16a84593` |
| `ui_describe_all` | openWorldHint, readOnlyHint | no | no | `faaf23579365` |
| `ui_describe_point` | openWorldHint, readOnlyHint | yes | no | `fc1e96919b24` |
| `ui_find_element` | openWorldHint, readOnlyHint | yes | no | `25b32c920835` |
| `ui_swipe` | openWorldHint, readOnlyHint | yes | no | `f691c5790650` |
| `ui_tap` | openWorldHint, readOnlyHint | yes | no | `20334fd59a35` |
| `ui_type` | openWorldHint, readOnlyHint | yes | no | `e6d9105028b7` |
| `ui_view` | openWorldHint, readOnlyHint | no | no | `46b93982d9bb` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-47 | `2.2.0` → `2.2.1` | `ui_type` | input_schema_changed (schema_other) | property 'method' changed (annotations/descriptions) |


