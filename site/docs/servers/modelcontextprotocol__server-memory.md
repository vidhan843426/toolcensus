# `@modelcontextprotocol/server-memory`

| | |
|---|---|
| Latest observed version | `2.1.0` |
| Status | ok |
| Weekly downloads | 300570 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:35ae19cb9777c185` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 9 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 5 |
| `median_days_between_releases` | 9.59 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (9)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_observations` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ec148b004b8c` |
| `create_entities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a54865c31325` |
| `create_relations` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e622df301dab` |
| `delete_entities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `95a62c3141ec` |
| `delete_observations` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7b786a8baf35` |
| `delete_relations` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `47845dc76655` |
| `open_nodes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d7cb69f81228` |
| `read_graph` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `442f341a763a` |
| `search_nodes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `edac315bc1ec` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `2.0.1` → `2.1.0` | `add_observations` | annotations_changed |  |
| week 2026-46 | `2.0.1` → `2.1.0` | `create_entities` | annotations_changed |  |
| week 2026-46 | `2.0.1` → `2.1.0` | `create_relations` | annotations_changed |  |
| week 2026-46 | `2.0.1` → `2.1.0` | `open_nodes` | description_changed | length 57 -&gt; 373 |
| week 2026-46 | `2.0.1` → `2.1.0` | `open_nodes` | input_schema_changed (schema_widened) | property 'observationLimit' added (optional) |
| week 2026-46 | `2.0.1` → `2.1.0` | `open_nodes` | output_schema_changed |  |
| week 2026-46 | `2.0.1` → `2.1.0` | `read_graph` | description_changed | length 31 -&gt; 266 |
| week 2026-46 | `2.0.1` → `2.1.0` | `read_graph` | input_schema_changed (schema_widened) | property 'entityTypes' added (optional); property 'observationLimit' added (optional) |
| week 2026-46 | `2.0.1` → `2.1.0` | `read_graph` | output_schema_changed |  |
| week 2026-46 | `2.0.1` → `2.1.0` | `search_nodes` | description_changed | length 56 -&gt; 389 |
| week 2026-46 | `2.0.1` → `2.1.0` | `search_nodes` | input_schema_changed (schema_widened) | property 'limit' added (optional); property 'observationLimit' added (optional) |
| week 2026-46 | `2.0.1` → `2.1.0` | `search_nodes` | output_schema_changed |  |


