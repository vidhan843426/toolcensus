# `@aashari/mcp-server-atlassian-bitbucket`

| | |
|---|---|
| Latest observed version | `3.1.0` |
| Status | ok |
| Weekly downloads | 12109 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:7186ca95fd3fa9c3` |

!!! tip "Improvement hints"
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 6 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 8 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 0 |
| `median_days_between_releases` | 0.08 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (6)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `bb_clone` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2213ac691111` |
| `bb_delete` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `544aad48135a` |
| `bb_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `87bb1a68c442` |
| `bb_patch` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5a92133e4d4f` |
| `bb_post` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c6c94447a049` |
| `bb_put` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8e33129ff73e` |



## Change history

No tool-definition changes observed.
