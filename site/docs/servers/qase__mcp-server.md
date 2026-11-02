# `@qase/mcp-server`

| | |
|---|---|
| Latest observed version | `3.0.4` |
| Status | ok |
| Weekly downloads | 10456 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:00b49f2c61cd0129` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 42 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 13 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 27 |
| `median_days_between_releases` | 2.0 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (42)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `qase_api` | destructiveHint | yes | no | `1285cdc7a0ee` |
| `qase_attachment_delete` | idempotentHint | yes | no | `97ce6155b930` |
| `qase_attachment_upload` | destructiveHint | yes | no | `e916bedb39d4` |
| `qase_case_bulk_create` | destructiveHint | yes | no | `740c46f92129` |
| `qase_case_delete` | idempotentHint | yes | no | `12ad8285f65f` |
| `qase_case_upsert` | destructiveHint | yes | no | `4208f6767d0c` |
| `qase_ci_report` | destructiveHint | yes | no | `26fdaee06b85` |
| `qase_custom_field_delete` | idempotentHint | yes | no | `c7576d4cd3c3` |
| `qase_custom_field_upsert` | destructiveHint | yes | no | `92ffc98c218b` |
| `qase_defect_delete` | idempotentHint | yes | no | `cb71799fdf64` |
| `qase_defect_upsert` | destructiveHint | yes | no | `ca6a31bf0778` |
| `qase_discover_tools` | destructiveHint, idempotentHint, readOnlyHint | no | no | `00cdbc7bea49` |
| `qase_environment_delete` | idempotentHint | yes | no | `be8e90f60966` |
| `qase_environment_upsert` | destructiveHint | yes | no | `a63f12faae0d` |
| `qase_external_issue_link` | destructiveHint, idempotentHint | yes | no | `49d809208ea7` |
| `qase_get` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `559764f8ea5a` |
| `qase_milestone_delete` | idempotentHint | yes | no | `ff403a20e14f` |
| `qase_milestone_upsert` | destructiveHint | yes | no | `ae2c71e8e60a` |
| `qase_plan_delete` | idempotentHint | yes | no | `dac5a418f3d9` |
| `qase_plan_upsert` | destructiveHint | yes | no | `bc72a3466f39` |
| `qase_project_context` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `5e5905649079` |
| `qase_project_create` | destructiveHint | yes | no | `0c7d023e94fb` |
| `qase_project_delete` | idempotentHint | yes | no | `09d0eec280d5` |
| `qase_regression_run` | destructiveHint | yes | no | `7602013ad784` |
| `qase_result_delete` | idempotentHint | yes | no | `d0c9f36b5b73` |
| `qase_result_record` | destructiveHint | yes | no | `0a13a4c74aa8` |
| `qase_review_bulk_create` | destructiveHint | yes | no | `9adb29abe271` |
| `qase_review_create` | destructiveHint | yes | no | `49c4ba832201` |
| `qase_review_delete` | idempotentHint | yes | no | `547d038500a8` |
| `qase_review_list` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `4d27ce5e8593` |
| `qase_review_update` | destructiveHint, idempotentHint | yes | no | `7428737a757b` |
| `qase_run_complete` | destructiveHint, idempotentHint | yes | no | `775ac3fae7a6` |
| `qase_run_delete` | idempotentHint | yes | no | `a5d69538b3bc` |
| `qase_run_upsert` | destructiveHint | yes | no | `a13587da5522` |
| `qase_shared_step_delete` | idempotentHint | yes | no | `64fe82d0f3df` |
| `qase_shared_step_upsert` | destructiveHint | yes | no | `9edda8ac2614` |
| `qase_suite_delete` | idempotentHint | yes | no | `7313aa2e3c3f` |
| `qase_suite_upsert` | destructiveHint | yes | no | `e7826f28dc49` |
| `qase_tool_help` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `28e46f1bda26` |
| `qase_triage_defect` | destructiveHint | yes | no | `66e0094866c3` |
| `qql_help` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `803caf6baea8` |
| `qql_search` | destructiveHint, idempotentHint, readOnlyHint | yes | no | `6573d5dafa46` |



## Change history

No tool-definition changes observed.
