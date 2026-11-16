# `@sap-ux/fiori-mcp-server`

| | |
|---|---|
| Latest observed version | `1.16.3` |
| Status | ok |
| Weekly downloads | 105110 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.SAP/fiori-mcp-server |
| Surface hash | `sha256:d72cb551973a2da3` |

!!! tip "Improvement hints"
    - Consider `additionalProperties: false` on the input schema of 1 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 0 |
| `maintainer_count` | 5 |
| `releases_last_90d` | 49 |
| `median_days_between_releases` | 1.3 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (9)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `download_odata_service_metadata` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `76dface58e0a` |
| `execute_functionality` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `6634b95dda52` |
| `generate_fiori_app_cap` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `5999181e6074` |
| `generate_fiori_app_odata` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `89341ffbe56a` |
| `get_functionality_details` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `104c31715991` |
| `list_fiori_apps` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `c73ad27f099b` |
| `list_functionality` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `682350b7305f` |
| `list_sap_systems` | idempotentHint, openWorldHint, readOnlyHint | no | no | `65f0c7c83645` |
| `search_docs` | idempotentHint, openWorldHint, readOnlyHint | yes | no | `1ad7ca550e21` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `1.15.21` → `1.16.0` | `execute_functionality` | input_schema_changed (schema_other) | property 'functionalityId' changed (annotations/descriptions) |
| week 2026-46 | `1.15.21` → `1.16.0` | `execute_functionality` | output_schema_changed |  |
| week 2026-46 | `1.15.21` → `1.16.0` | `get_functionality_details` | input_schema_changed (schema_other) | property 'functionalityId' changed (annotations/descriptions) |
| week 2026-46 | `1.15.21` → `1.16.0` | `get_functionality_details` | output_schema_changed |  |
| week 2026-46 | `1.15.21` → `1.16.0` | `list_functionality` | output_schema_changed |  |


