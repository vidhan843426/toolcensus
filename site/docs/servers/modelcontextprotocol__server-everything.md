# `@modelcontextprotocol/server-everything`

| | |
|---|---|
| Latest observed version | `2.3.0` |
| Status | ok |
| Weekly downloads | 326122 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:5461af62472fa6d8` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 10 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 6 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 8 |
| `median_days_between_releases` | 12.72 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (16)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `echo` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b00b5993bf61` |
| `get-annotated-message` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0f6b4cbc644d` |
| `get-env` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `1bfe300a1c6d` |
| `get-header-params` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `81004e0be698` |
| `get-resource-links` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b1a37f5759af` |
| `get-resource-reference` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `a676304f5156` |
| `get-structured-content` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e01899dbf0e0` |
| `get-sum` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c0bfe393aeb2` |
| `get-tiny-image` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d167988219fd` |
| `gzip-file-as-resource` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `165dece2e0d5` |
| `toggle-simulated-logging` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c23b2942da14` |
| `toggle-subscriber-updates` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `8d6b133c6f02` |
| `trigger-list-changed` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `06e1ba36b229` |
| `trigger-log-messages` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0c4b5a5560fb` |
| `trigger-long-running-operation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `91d7e076f1f0` |
| `trigger-resource-update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e96c75aa963e` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `2.0.1` → `2.1.0` | `get-env` | description_changed | length 81 -&gt; 303 |
| week 2026-46 | `2.1.0` → `2.2.1` | `echo` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-annotated-message` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-env` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-header-params` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-resource-links` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-resource-reference` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-structured-content` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-sum` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `get-tiny-image` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `gzip-file-as-resource` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `toggle-simulated-logging` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `toggle-subscriber-updates` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `trigger-list-changed` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `trigger-log-messages` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `trigger-long-running-operation` | other_changed | title or other top-level field changed |
| week 2026-46 | `2.1.0` → `2.2.1` | `trigger-resource-update` | other_changed | title or other top-level field changed |
| week 2026-47 | `2.2.1` → `2.3.0` | `get-resource-reference` | input_schema_changed (schema_other) | property 'resourceId' changed (annotations/descriptions) |


