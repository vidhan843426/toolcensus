# `chelaile-mcp-server`

| | |
|---|---|
| Latest observed version | `1.1.0` |
| Status | ok |
| Weekly downloads | 28133 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:e932310ec63e04f7` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 0 |
| `median_days_between_releases` | — |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (15)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `bus_get_city_config` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `0e9c5c8d8b26` |
| `bus_get_line_detail` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4601a726cef4` |
| `bus_get_line_realtime` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `a8468c4f4a99` |
| `bus_get_line_route` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `04c77c820320` |
| `bus_get_my_location` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `5c16986c05cb` |
| `bus_get_nearby_stops` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `d84e3326cfd3` |
| `bus_get_stop_detail` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4fc14f69e73e` |
| `bus_get_timetable` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `24d8bcbfd3aa` |
| `bus_list_cities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `a43f5c3b5c73` |
| `bus_list_line_buses` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `dbdf43ec3a5d` |
| `bus_plan_transit` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `768da6d63ff2` |
| `bus_refresh_lines` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `59fb1921d144` |
| `bus_reverse_geocode` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `7a6d8510baa8` |
| `bus_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `b284e36c0bde` |
| `bus_search_more` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `b165a568f98b` |



## Change history

No tool-definition changes observed.
