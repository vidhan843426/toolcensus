# `opencode-mcp`

| | |
|---|---|
| Latest observed version | `3.0.0` |
| Status | ok |
| Weekly downloads | 13983 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:d7e4fe2aefb69b7e` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 87 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 4 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 2 |
| `median_days_between_releases` | 0.23 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (87)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `opencode_agent_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7683d964b7ac` |
| `opencode_ask` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b99248cd66f5` |
| `opencode_auth_set` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f63c7ef9fedd` |
| `opencode_check` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0ba774d64e48` |
| `opencode_command_execute` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ec832e190425` |
| `opencode_command_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6726dfc3b5e7` |
| `opencode_config_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f59490ee63d1` |
| `opencode_config_providers` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `43d7477171c6` |
| `opencode_config_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e47016edd6a5` |
| `opencode_context` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `56d9b4fa37e4` |
| `opencode_conversation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0fd336d46d46` |
| `opencode_events_poll` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `4300c7b1592c` |
| `opencode_file_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d3fd5b2ef00c` |
| `opencode_file_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `940a9c136288` |
| `opencode_file_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `58c8f2a66bc1` |
| `opencode_find_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f8d19505f697` |
| `opencode_find_symbol` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3ba360979524` |
| `opencode_find_text` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f32fbeaa3154` |
| `opencode_fire` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `366be5bd5d6d` |
| `opencode_formatter_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `727bce6a64de` |
| `opencode_health` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `62692b557a6a` |
| `opencode_instance_dispose` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `a36ba91f7c69` |
| `opencode_job_cancel` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `31e855d812c7` |
| `opencode_job_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `165881572e6d` |
| `opencode_job_input` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e51d085f4b9c` |
| `opencode_job_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b39cdb1e54e1` |
| `opencode_log` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4ae360792f58` |
| `opencode_lsp_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0f8fcf9cca22` |
| `opencode_mcp_add` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `101a17617de0` |
| `opencode_mcp_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6a5e94b42f55` |
| `opencode_message_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `477c6287027f` |
| `opencode_message_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `00709084074a` |
| `opencode_message_send` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8bc029f4d1df` |
| `opencode_message_send_async` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b3ccd3a0bad5` |
| `opencode_path_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c8b2391ce777` |
| `opencode_permission_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c9cb701c5af2` |
| `opencode_project_current` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7e2fb602506e` |
| `opencode_project_init` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7d65cfdef5f8` |
| `opencode_project_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7a4c86525a54` |
| `opencode_provider_auth_methods` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `a55fcfb3b66e` |
| `opencode_provider_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `a34d0285da6a` |
| `opencode_provider_models` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `40157bf18457` |
| `opencode_provider_oauth_authorize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e2184d6daef4` |
| `opencode_provider_oauth_callback` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `87ac7bc5eab7` |
| `opencode_provider_test` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ba0883fa456e` |
| `opencode_question_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0671591a5739` |
| `opencode_question_reject` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5eabf60094f0` |
| `opencode_question_reply` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f9f66d9a84e2` |
| `opencode_reply` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fdb2e4be3c02` |
| `opencode_review_changes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0aa12e8c7d94` |
| `opencode_run` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `21e92e26fc4e` |
| `opencode_session_abort` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `56c620bb738c` |
| `opencode_session_children` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e27e53529738` |
| `opencode_session_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `619e9ceb043c` |
| `opencode_session_delete` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1c1878398505` |
| `opencode_session_diff` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ec9d1b53436e` |
| `opencode_session_fork` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7de22d3cdfb6` |
| `opencode_session_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a0f0ec980527` |
| `opencode_session_init` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `81381b167423` |
| `opencode_session_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `ee6bf78a2f35` |
| `opencode_session_permission` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0e1af330a37a` |
| `opencode_session_revert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0ff53e93fd87` |
| `opencode_session_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `56bfd02e52d9` |
| `opencode_session_share` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `51e9a8710837` |
| `opencode_session_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7eec97e3a827` |
| `opencode_session_summarize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4490eb732e05` |
| `opencode_session_todo` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `cab24037e21b` |
| `opencode_session_unrevert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `af055e7ab2f6` |
| `opencode_session_unshare` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c3b82b18e78d` |
| `opencode_session_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f59e42f19878` |
| `opencode_sessions_overview` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `9cf7be826d09` |
| `opencode_setup` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `82dad8b8f132` |
| `opencode_shell_execute` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8688a9e7d2b1` |
| `opencode_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `32a5aa18e5b2` |
| `opencode_tool_ids` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `374614ea1ef0` |
| `opencode_tool_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2438fa406199` |
| `opencode_tui_append_prompt` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c4b000fa0726` |
| `opencode_tui_clear_prompt` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `866706468e03` |
| `opencode_tui_execute_command` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5f0788a871a0` |
| `opencode_tui_open_help` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e0f995fe7de7` |
| `opencode_tui_open_models` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d14a67042c90` |
| `opencode_tui_open_sessions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3d05626dfe2c` |
| `opencode_tui_open_themes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `af28ebd2c60e` |
| `opencode_tui_show_toast` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `72f16f5007da` |
| `opencode_tui_submit_prompt` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3e82be34d06f` |
| `opencode_vcs_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `80d11757e004` |
| `opencode_wait` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `5164a4270f59` |



## Change history

No tool-definition changes observed.
