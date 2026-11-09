# `mongodb-mcp-server`

| | |
|---|---|
| Latest observed version | `3.3.0` |
| Status | ok |
| Weekly downloads | 153673 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.mongodb-js/mongodb-mcp-server |
| Surface hash | `sha256:8b67bdc6273caaa2` |



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 16 |
| `maintainer_count` | 9 |
| `releases_last_90d` | 20 |
| `median_days_between_releases` | 2.67 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (27)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `aggregate` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `75c771c42ebc` |
| `aggregate-db` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `131fbc686e1a` |
| `collection-indexes` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `a68473b7fa66` |
| `collection-schema` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `37aec76f84ec` |
| `collection-storage-size` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `e5da5defd1cb` |
| `connect` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `2d6c66a41ad2` |
| `count` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `6f18ab5dc823` |
| `create-collection` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `9ca1701eb79b` |
| `create-index` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `0aa926a63612` |
| `db-stats` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `9e043f985b12` |
| `delete-many` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `2893cbd83281` |
| `disconnect` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `cc1a2ac67213` |
| `drop-collection` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `ee9481c76e51` |
| `drop-database` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `4b83dae823b2` |
| `drop-index` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `560381fa04ed` |
| `explain` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `31460f02beff` |
| `export` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `e9ab44525e26` |
| `find` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `cc5b6c11b752` |
| `insert-many` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `95849eb40e22` |
| `list-collections` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `4b19340c10f7` |
| `list-connections` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `b4ab2e5b5e8e` |
| `list-databases` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `efa92def411a` |
| `list-knowledge-sources` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `6112cdfd203d` |
| `mongodb-logs` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `96b9ea46145b` |
| `rename-collection` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `3c6893557c07` |
| `search-knowledge` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `a590e7f292be` |
| `update-many` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `100e0c7c3f2f` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `3.2.2` → `3.3.0` | `aggregate` | input_schema_changed (schema_other) | property 'pipeline' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `aggregate` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `aggregate-db` | input_schema_changed (schema_other) | property 'pipeline' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `aggregate-db` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `collection-indexes` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `collection-schema` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `count` | input_schema_changed (schema_other) | property 'query' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `create-index` | input_schema_changed (schema_other) | property 'definition' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `db-stats` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `delete-many` | input_schema_changed (schema_other) | property 'filter' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `explain` | input_schema_changed (schema_other) | property 'method' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `explain` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `export` | input_schema_changed (schema_other) | property 'exportTarget' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `find` | input_schema_changed (schema_other) | property 'filter' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `find` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `insert-many` | input_schema_changed (schema_other) | property 'documents' changed (annotations/descriptions) |
| week 2026-46 | `3.2.2` → `3.3.0` | `insert-many` | output_schema_changed |  |
| week 2026-46 | `3.2.2` → `3.3.0` | `update-many` | input_schema_changed (schema_other) | property 'filter' changed (annotations/descriptions) |


