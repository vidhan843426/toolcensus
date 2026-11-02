# `@shopify/dev-mcp`

| | |
|---|---|
| Latest observed version | `1.18.0` |
| Status | ok |
| Weekly downloads | 80670 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:72923575196c4328` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 5 of 5 tools.
    - Consider `additionalProperties: false` on the input schema of 5 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 20 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 14 |
| `median_days_between_releases` | 0.24 |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (5)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `feedback` | — | yes | no | `5e863df4eef7` |
| `learn_shopify_api` | — | yes | no | `779e7b91ff27` |
| `search_docs_chunks` | — | yes | no | `987ed2119e8d` |
| `validate` | — | yes | no | `4968347abde5` |
| `validate_theme` | — | yes | no | `71fc3e90e551` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `1.17.0` → `1.18.0` | `learn_shopify_api` | description_changed | length 13146 -&gt; 13562 |
| week 2026-45 | `1.17.0` → `1.18.0` | `learn_shopify_api` | input_schema_changed (schema_other) | property 'api': enum values added; property 'version' changed (annotations/descriptions) |
| week 2026-45 | `1.17.0` → `1.18.0` | `search_docs_chunks` | input_schema_changed (schema_other) | property 'version' changed (annotations/descriptions) |
| week 2026-45 | `1.17.0` → `1.18.0` | `validate` | input_schema_changed (schema_other) | property 'version' changed (annotations/descriptions) |


