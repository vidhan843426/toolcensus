# `dynoxide`

| | |
|---|---|
| Latest observed version | `1.6.0` |
| Status | ok |
| Weekly downloads | 20484 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.nubo-db/dynoxide |
| Surface hash | `sha256:3ae5ea538816844d` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 35 of 35 tools.
    - Consider `additionalProperties: false` on the input schema of 31 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 0 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 8 |
| `median_days_between_releases` | 7.33 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (35)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `batch_execute_partiql` | — | yes | no | `aa82d7c809fb` |
| `batch_get_item` | — | yes | no | `82663c890723` |
| `batch_write_item` | — | yes | no | `59c9fd2388fe` |
| `bulk_put_items` | — | yes | no | `7e8a64a41d70` |
| `create_snapshot` | — | no | no | `09bd4b226869` |
| `create_table` | — | yes | no | `fea309a743a5` |
| `delete_item` | — | yes | no | `05a7b240a7ea` |
| `delete_snapshot` | — | yes | no | `d6a51818ce6e` |
| `delete_table` | — | yes | no | `6a5bc4eaf78d` |
| `describe_stream` | — | yes | no | `82c5c2ac94e9` |
| `describe_table` | — | yes | no | `672783d27f6b` |
| `describe_time_to_live` | — | yes | no | `adeab687818f` |
| `execute_partiql` | — | yes | no | `a3fab487a4b9` |
| `execute_transaction_partiql` | — | yes | no | `0c23a1e5b0d6` |
| `get_database_info` | — | no | no | `10e0839dd923` |
| `get_item` | — | yes | no | `46ed56992f10` |
| `get_records` | — | yes | no | `726a2e990a37` |
| `get_shard_iterator` | — | yes | no | `4417fa22b862` |
| `list_snapshots` | — | no | no | `070386f7dfb2` |
| `list_streams` | — | no | no | `4ab7fa1e14d4` |
| `list_tables` | — | no | no | `08d10dd9a6f6` |
| `list_tags_of_resource` | — | yes | no | `59f80148c43e` |
| `put_item` | — | yes | no | `3ef55a734193` |
| `query` | — | yes | no | `400d80f563f4` |
| `restore_snapshot` | — | yes | no | `4964b410bbc8` |
| `scan` | — | yes | no | `ae06b9407739` |
| `search_vectors` | — | yes | no | `3bc6a947bfc7` |
| `sweep_ttl` | — | no | no | `c2944aee3821` |
| `tag_resource` | — | yes | no | `218b4b01b012` |
| `transact_get_items` | — | yes | no | `f2fa5fcfc78d` |
| `transact_write_items` | — | yes | no | `86b6718e2715` |
| `untag_resource` | — | yes | no | `4ba2e5ebdc2f` |
| `update_item` | — | yes | no | `9f7f7f5d2dd3` |
| `update_table` | — | yes | no | `916f12bfd2a8` |
| `update_time_to_live` | — | yes | no | `56931bf9de59` |



## Change history

No tool-definition changes observed.
