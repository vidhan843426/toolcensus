# `mcp-searxng`

| | |
|---|---|
| Latest observed version | `2.9.0` |
| Status | ok |
| Weekly downloads | 19443 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.ihor-sokoliuk/mcp-searxng |
| Surface hash | `sha256:98a544393a158588` |

!!! tip "Improvement hints"
    - Consider `additionalProperties: false` on the input schema of 4 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 14 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 15 |
| `median_days_between_releases` | 2.04 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (4)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `searxng_instance_info` | openWorldHint, readOnlyHint | no | no | `8898f6303440` |
| `searxng_search_suggestions` | openWorldHint, readOnlyHint | yes | no | `1616ab1f714a` |
| `searxng_web_search` | openWorldHint, readOnlyHint | yes | no | `444a41d8a4b2` |
| `web_url_read` | openWorldHint, readOnlyHint | yes | no | `4d765a61d29e` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `2.8.1` → `2.9.0` | `searxng_web_search` | input_schema_changed (schema_widened) | property 'pages' added (optional) |


