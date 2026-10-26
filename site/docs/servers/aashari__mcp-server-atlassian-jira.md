# `@aashari/mcp-server-atlassian-jira`

| | |
|---|---|
| Latest observed version | `3.3.0` |
| Status | ok |
| Weekly downloads | 13192 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:a6837baa4f6bcf80` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 5 of 5 tools.
    - Consider `additionalProperties: false` on the input schema of 5 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 9 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 0 |
| `median_days_between_releases` | 0.12 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (5)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `jira_delete` | — | yes | no | `bf06f3f06ea0` |
| `jira_get` | — | yes | no | `f746fa5d7354` |
| `jira_patch` | — | yes | no | `c53e9aa1206a` |
| `jira_post` | — | yes | no | `f930c58ef593` |
| `jira_put` | — | yes | no | `686002c998f8` |



## Change history

No tool-definition changes observed.
