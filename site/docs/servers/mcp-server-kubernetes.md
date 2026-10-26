# `mcp-server-kubernetes`

| | |
|---|---|
| Latest observed version | `4.2.1` |
| Status | ok |
| Weekly downloads | 11393 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:ac5f360e6883a8a2` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 3 of 23 tools.
    - Consider `additionalProperties: false` on the input schema of 20 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 12 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 11 |
| `median_days_between_releases` | 2.81 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (23)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `cleanup` | destructiveHint | no | no | `71c342985c47` |
| `exec_in_pod` | destructiveHint | yes | no | `03331e840056` |
| `explain_resource` | readOnlyHint | yes | no | `4241d6acfa17` |
| `install_helm_chart` | destructiveHint | yes | no | `59d710772f96` |
| `kubectl_apply` | destructiveHint | no | no | `1bf1a99e4579` |
| `kubectl_context` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `57853c8bb2ed` |
| `kubectl_create` | — | no | no | `6f0568be44f5` |
| `kubectl_delete` | destructiveHint | no | no | `93baa1d8fa61` |
| `kubectl_describe` | readOnlyHint | yes | no | `6885509b7119` |
| `kubectl_generic` | destructiveHint | yes | no | `8b6d9b16d422` |
| `kubectl_get` | readOnlyHint | yes | no | `3a83385b9153` |
| `kubectl_logs` | readOnlyHint | yes | no | `69501cdac50b` |
| `kubectl_patch` | destructiveHint | yes | no | `f5982f3e6315` |
| `kubectl_reconnect` | readOnlyHint | no | no | `2ec7769f3d7b` |
| `kubectl_rollout` | destructiveHint | yes | no | `c8e9c17b3d30` |
| `kubectl_scale` | destructiveHint | yes | no | `77be589821a2` |
| `list_api_resources` | readOnlyHint | no | no | `07f2be4942a2` |
| `node_management` | destructiveHint | yes | no | `1408132882dd` |
| `ping` | readOnlyHint | no | no | `db7e94a73761` |
| `port_forward` | — | yes | no | `c1424f92a8a4` |
| `stop_port_forward` | — | yes | no | `98cddfbbd1a3` |
| `uninstall_helm_chart` | destructiveHint | yes | no | `ce652ad18c07` |
| `upgrade_helm_chart` | destructiveHint | yes | no | `baaaf692933e` |



## Change history

No tool-definition changes observed.
