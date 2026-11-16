# `@aikidosec/mcp`

| | |
|---|---|
| Latest observed version | `1.0.34` |
| Status | ok |
| Weekly downloads | 96820 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:934d388b1a3651ab` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 12 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 7 |
| `maintainer_count` | 2 |
| `releases_last_90d` | 14 |
| `median_days_between_releases` | 6.43 |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (13)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `aikido_adjust_issue_severity` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f8f4dfdc091b` |
| `aikido_deep_review` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `dd63aa8627bd` |
| `aikido_deep_review_status` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `35e36b1927b0` |
| `aikido_full_scan` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b08ad1dc8f12` |
| `aikido_ignore_issue` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `74005dcc51fb` |
| `aikido_issues_list` | destructiveHint, openWorldHint, readOnlyHint | no | no | `16d8517491ca` |
| `aikido_login` | destructiveHint, openWorldHint, readOnlyHint | no | no | `c06b5a01c0b9` |
| `aikido_oss_dependency_scan` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `42f42d76cdc7` |
| `aikido_scan_paths` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `910cf51d697c` |
| `aikido_snooze_issue` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ed3003101bec` |
| `aikido_unignore_issue` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ee3a6f689e61` |
| `aikido_unsnooze_issue` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `716282817b4d` |
| `aikido_workspaces_list` | destructiveHint, openWorldHint, readOnlyHint | no | no | `5db01241c75d` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `1.0.33` → `1.0.34` | `aikido_deep_review` | tool_added |  |
| week 2026-46 | `1.0.33` → `1.0.34` | `aikido_deep_review_status` | tool_added |  |
| week 2026-46 | `1.0.33` → `1.0.34` | `aikido_snooze_issue` | description_changed | length 350 -&gt; 522 |
| week 2026-46 | `1.0.33` → `1.0.34` | `aikido_snooze_issue` | input_schema_changed (schema_other) | property 'snooze_until_date' added (optional); property 'duration' no longer required; property 'duration' changed (annotations/descriptions) |


