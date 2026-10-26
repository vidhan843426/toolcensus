# `@transcend-io/mcp`

| | |
|---|---|
| Latest observed version | `1.7.0` |
| Status | ok |
| Weekly downloads | 77563 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:2b3dcbd25bf40609` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 82 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 14 |
| `maintainer_count` | 9 |
| `releases_last_90d` | 59 |
| `median_days_between_releases` | 0.8 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (91)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `admin_get_current_user` | destructiveHint, idempotentHint, readOnlyHint | no | no | `291178b63dfd` |
| `admin_get_organization` | destructiveHint, idempotentHint, readOnlyHint | no | no | `bc1abe13f59f` |
| `admin_get_privacy_center` | destructiveHint, idempotentHint, readOnlyHint | no | no | `78cacc92b18b` |
| `admin_list_api_keys` | destructiveHint, idempotentHint, readOnlyHint | no | no | `2b2198809343` |
| `admin_list_scopes` | destructiveHint, idempotentHint, readOnlyHint | no | no | `4a731408312a` |
| `admin_list_teams` | destructiveHint, idempotentHint, readOnlyHint | no | no | `c3fa853b230d` |
| `admin_list_users` | destructiveHint, idempotentHint, readOnlyHint | no | no | `ce4b48665f05` |
| `admin_test_connection` | destructiveHint, idempotentHint, readOnlyHint | no | no | `5073f5742da0` |
| `assessments_add_section` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `97db41b96270` |
| `assessments_answer_question` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `b6e7ba6f1552` |
| `assessments_create` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `41afd3170e12` |
| `assessments_create_group` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `0f108ae3e60e` |
| `assessments_create_template` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `2b11b2fd52e0` |
| `assessments_export_template` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `03e705846bc6` |
| `assessments_get` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `d0f2df6a6623` |
| `assessments_list` | destructiveHint, idempotentHint, readOnlyHint | no | no | `d365adbceb23` |
| `assessments_list_comments` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `29fa3916bf34` |
| `assessments_list_groups` | destructiveHint, idempotentHint, readOnlyHint | no | no | `de940b36ca5a` |
| `assessments_list_templates` | destructiveHint, idempotentHint, readOnlyHint | no | no | `9a80c4eeec65` |
| `assessments_prefill` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `f7fcbf990986` |
| `assessments_submit_response` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `67f0d1445397` |
| `assessments_update` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `351e4e34fdc5` |
| `assessments_update_assignees` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `506c407fe053` |
| `assessments_write_comment` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `57c3a1cef48a` |
| `consent_bulk_triage` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `4d2f57fb9c80` |
| `consent_cookie_triage_review_app` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `fe37630d031b` |
| `consent_get_aggregate_analytics` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `26a96900c972` |
| `consent_get_analytics_data` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `c71053a1b25e` |
| `consent_get_inventory_stats` | destructiveHint, idempotentHint, readOnlyHint | no | no | `473ff1482f76` |
| `consent_get_preferences` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `334812560045` |
| `consent_get_timeseries_analytics` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `f3270133a4bc` |
| `consent_list_airgap_bundles` | destructiveHint, idempotentHint, readOnlyHint | no | no | `0e55c0b5fc30` |
| `consent_list_cookies` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `1a53806cd7e2` |
| `consent_list_data_flows` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `c119b57cd49a` |
| `consent_list_purposes` | destructiveHint, idempotentHint, readOnlyHint | no | no | `8c88a248fdbe` |
| `consent_list_regimes` | destructiveHint, idempotentHint, readOnlyHint | no | no | `69748326505b` |
| `consent_list_roc_records` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `ac28d3473f55` |
| `consent_update_cookies` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `3cc0e366841c` |
| `consent_update_data_flows` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `26801bbe7a0b` |
| `custom_functions_get_code` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `f5f59dc93de8` |
| `custom_functions_list` | destructiveHint, idempotentHint, readOnlyHint | no | no | `c40b6d346d28` |
| `custom_functions_promote_version` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `5cad0a4caf0a` |
| `custom_functions_test_run` | destructiveHint, idempotentHint, readOnlyHint | no | no | `c379ea93ebc8` |
| `custom_functions_upsert` | destructiveHint, idempotentHint, readOnlyHint | no | no | `277360e04a21` |
| `discovery_classify_text` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `d366767fd547` |
| `discovery_list_plugins` | destructiveHint, idempotentHint, readOnlyHint | no | no | `2f409c0d5c10` |
| `discovery_list_scans` | destructiveHint, idempotentHint, readOnlyHint | no | no | `f15e8f3ec57e` |
| `discovery_ner_extract` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `a83897fcf2eb` |
| `docs_fetch` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `255e1d17a9b1` |
| `docs_list` | destructiveHint, idempotentHint, readOnlyHint | no | no | `140d2611cb92` |
| `dsr_analyze` | destructiveHint, idempotentHint, readOnlyHint | no | no | `9cfaa78fc13b` |
| `dsr_cancel` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `f6f0e6f84fe8` |
| `dsr_enrich_identifiers` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `e795a28adb2c` |
| `dsr_get_details` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `547027b63f18` |
| `dsr_list` | destructiveHint, idempotentHint, readOnlyHint | no | no | `3abf93d24e73` |
| `dsr_list_identifiers` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `ccbd1f205fb4` |
| `dsr_list_pending_requests` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `6dfcc5f6d38d` |
| `dsr_list_request_data_silos` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `7b84b7268ec7` |
| `dsr_poll_status` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `d85cb424a47c` |
| `dsr_submit` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `49ba51404677` |
| `inventory_analyze` | destructiveHint, idempotentHint, readOnlyHint | no | no | `13a58a763410` |
| `inventory_get_data_silo` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `383f3d54eaf5` |
| `inventory_list_business_entities` | destructiveHint, idempotentHint, readOnlyHint | no | no | `434414394e59` |
| `inventory_list_catalog_integrations` | destructiveHint, idempotentHint, readOnlyHint | no | no | `8b91057a6cdf` |
| `inventory_list_categories` | destructiveHint, idempotentHint, readOnlyHint | no | no | `faad198aaf47` |
| `inventory_list_data_points` | destructiveHint, idempotentHint, readOnlyHint | no | no | `4f52425ba1cb` |
| `inventory_list_data_silos` | destructiveHint, idempotentHint, readOnlyHint | no | no | `f8eb27be284b` |
| `inventory_list_data_subjects` | destructiveHint, idempotentHint, readOnlyHint | no | no | `efdb5f52ee18` |
| `inventory_list_identifiers` | destructiveHint, idempotentHint, readOnlyHint | no | no | `56bea17816c1` |
| `inventory_list_processing_purposes` | destructiveHint, idempotentHint, readOnlyHint | no | no | `65021b2fb3bd` |
| `inventory_list_sub_data_points` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `e561eed9dbef` |
| `inventory_list_vendors` | destructiveHint, idempotentHint, readOnlyHint | no | no | `864c7caae684` |
| `inventory_update_or_create_data_point` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `7d9aaf5f637b` |
| `inventory_write_category` | destructiveHint, idempotentHint, readOnlyHint | no | no | `30450eddb978` |
| `inventory_write_data_silo` | destructiveHint, idempotentHint, readOnlyHint | no | no | `6fd9069a2d6a` |
| `inventory_write_processing_purpose` | destructiveHint, idempotentHint, readOnlyHint | no | no | `bdf669faef44` |
| `inventory_write_vendor` | destructiveHint, idempotentHint, readOnlyHint | no | no | `622c268e1863` |
| `policy_get_templates` | destructiveHint, idempotentHint, readOnlyHint | no | no | `91079da2e8eb` |
| `policy_list_bundles` | destructiveHint, idempotentHint, readOnlyHint | no | no | `60f2c39ee16b` |
| `policy_publish` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `e9d3dabb0e5a` |
| `policy_set_live` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `b38361b5463f` |
| `preferences_append_identifiers` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `d4cd5b62a887` |
| `preferences_delete` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `adef4a07939a` |
| `preferences_delete_identifiers` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `226c8e47cc40` |
| `preferences_list_partitions` | destructiveHint, idempotentHint, readOnlyHint | no | no | `3e0df0ed69a1` |
| `preferences_query` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `8ead362dbfe2` |
| `preferences_update_identifiers` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `a443f0de69bd` |
| `preferences_upsert` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `4cb1776b2451` |
| `workflows_list` | destructiveHint, idempotentHint, readOnlyHint | no | no | `cc0abb2493dd` |
| `workflows_list_email_templates` | destructiveHint, idempotentHint, readOnlyHint | no | no | `45232035030a` |
| `workflows_update_config` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `fb94fad95135` |



## Change history

No tool-definition changes observed.
