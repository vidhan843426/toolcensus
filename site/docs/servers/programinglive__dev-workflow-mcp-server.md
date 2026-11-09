# `@programinglive/dev-workflow-mcp-server`

| | |
|---|---|
| Latest observed version | `1.24.0` |
| Status | ok |
| Weekly downloads | 18220 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.programinglive/dev-workflow-mcp-server |
| Surface hash | `sha256:b13dec78bb504d6b` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 39 of 39 tools.
    - Consider `additionalProperties: false` on the input schema of 26 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 6 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 78 |
| `median_days_between_releases` | 0.02 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (39)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `check_ready_to_commit` | — | no | no | `7982bdce83b5` |
| `claim_factory_task` | — | yes | no | `c3025c87f4a8` |
| `commit_and_push` | — | no | no | `89deb3a9de5b` |
| `complete_task` | — | yes | no | `78fb57741546` |
| `continue_workflow` | — | no | no | `d0e3a2a753ac` |
| `create_documentation` | — | yes | no | `f18836906e42` |
| `create_factory_task` | — | yes | no | `f8c50d68c286` |
| `create_feature_flow` | — | yes | no | `53594f0fc3d2` |
| `create_tests` | — | no | no | `52c5abbf5d7b` |
| `drop_task` | — | no | no | `8889c286f014` |
| `force_complete_task` | — | no | no | `4d9d061d9d2a` |
| `get_workflow_status` | — | no | no | `60b24fd26739` |
| `list_active_sessions` | — | no | no | `0aeddcd59eab` |
| `list_factory_projects` | — | no | no | `6baca6a25855` |
| `list_factory_tasks` | — | no | no | `b09dd3a963ee` |
| `mark_bug_fixed` | — | yes | no | `59e973a8d5f2` |
| `mark_dod_item` | — | yes | no | `cbb76cf77ea2` |
| `mark_plan_step` | — | yes | no | `efe1a07a2dd2` |
| `next_steps` | — | no | no | `85edc1c83a62` |
| `perform_release` | — | yes | no | `68b40f2caed1` |
| `project_summary` | — | no | no | `5aa4f51b30eb` |
| `project_summary_data` | — | no | no | `92b54cd12757` |
| `project_summary_db` | — | no | no | `5d9c5883c21d` |
| `rerun_workflow` | — | no | no | `f608824c00c2` |
| `resume_session` | — | no | no | `e803d5f43315` |
| `run_full_workflow` | — | yes | no | `e2885ff6d0af` |
| `run_tests` | — | yes | no | `b4544c6d1dd7` |
| `search_project` | — | yes | yes | `64a05930204c` |
| `security_audit` | — | no | yes | `0b29c7ffa76c` |
| `set_definition_of_done` | — | yes | no | `425c3af13a0b` |
| `set_plan` | — | yes | no | `c266c90aa74e` |
| `skip_release` | — | yes | no | `79e60f34314c` |
| `skip_tests` | — | yes | no | `731ac7e71eab` |
| `start_task` | — | yes | no | `d19d92315ac9` |
| `sync_task_status` | — | yes | no | `2097330be064` |
| `update_factory_task` | — | yes | no | `d33fa989e246` |
| `view_history` | — | no | no | `3a2f7adefffe` |
| `waive_documentation` | — | yes | no | `89d1a9a85045` |
| `waive_dod_item` | — | yes | no | `681f96022c6b` |



## Change history

No tool-definition changes observed.
