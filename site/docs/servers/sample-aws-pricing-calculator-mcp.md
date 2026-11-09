# `sample-aws-pricing-calculator-mcp`

| | |
|---|---|
| Latest observed version | `1.3.7` |
| Status | ok |
| Weekly downloads | 13763 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:e57f28b477c05b9e` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 9 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 8 |
| `median_days_between_releases` | 6.82 |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (10)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_service` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1603bc95462a` |
| `build_estimate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4112f3e2fc07` |
| `create_estimate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e93d53a6ebbf` |
| `export_estimate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `53321eb9f771` |
| `get_estimate_cost` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `569d7a6b5407` |
| `get_server_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6c49a7cc9087` |
| `get_service_fields` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `13125f66a5c3` |
| `import_estimate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `601d069429ce` |
| `search_services` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `89454b5088ec` |
| `validate_estimate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a3acdd147ad7` |



## Change history

No tool-definition changes observed.
