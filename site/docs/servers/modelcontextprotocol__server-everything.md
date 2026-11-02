# `@modelcontextprotocol/server-everything`

| | |
|---|---|
| Latest observed version | `2.1.0` |
| Status | ok |
| Weekly downloads | 300001 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:7fbe81e57c7a6d75` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 10 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 7 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 6 |
| `median_days_between_releases` | 13.18 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (16)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `echo` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d7f485de086d` |
| `get-annotated-message` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1f3bddfd9934` |
| `get-env` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `36bd36873ff7` |
| `get-header-params` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4e3336b5234a` |
| `get-resource-links` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `9e99959e95b7` |
| `get-resource-reference` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `37d436c35f53` |
| `get-structured-content` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d9caa8434171` |
| `get-sum` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `eea3eeb67416` |
| `get-tiny-image` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c122d095df87` |
| `gzip-file-as-resource` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `df97e0c7d685` |
| `toggle-simulated-logging` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e334d5e9f815` |
| `toggle-subscriber-updates` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `cc6a0e2572f8` |
| `trigger-list-changed` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `832afa369ba6` |
| `trigger-log-messages` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `fbbd43ef879b` |
| `trigger-long-running-operation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c06ac9fb8ce0` |
| `trigger-resource-update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3d63c634c241` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `2.0.1` → `2.1.0` | `get-env` | description_changed | length 81 -&gt; 303 |


