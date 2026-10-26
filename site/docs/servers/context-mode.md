# `context-mode`

| | |
|---|---|
| Latest observed version | `1.0.169` |
| Status | ok |
| Weekly downloads | 35510 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:6f238f3e8f21d2eb` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 7 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 8 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 0 |
| `median_days_between_releases` | 0.03 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (11)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `ctx_batch_execute` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `95529af89478` |
| `ctx_doctor` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b4e58819486e` |
| `ctx_execute` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0388dab6238a` |
| `ctx_execute_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c346e12fedd7` |
| `ctx_fetch_and_index` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `8bb11afd5896` |
| `ctx_index` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `1ce02bfe85a8` |
| `ctx_insight` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `bd74654f6349` |
| `ctx_purge` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a47159838b70` |
| `ctx_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e9cfc13a62b4` |
| `ctx_stats` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `4fb7c8055d5c` |
| `ctx_upgrade` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `2fc9e487b1bb` |



## Change history

No tool-definition changes observed.
