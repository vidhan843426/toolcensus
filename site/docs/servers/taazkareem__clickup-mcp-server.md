# `@taazkareem/clickup-mcp-server`

| | |
|---|---|
| Latest observed version | `0.14.6` |
| Status | ok |
| Weekly downloads | 22016 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.taazkareem/clickup |
| Surface hash | `sha256:201b6178b3abf5e4` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 21 of 150 tools.
    - Consider `additionalProperties: false` on the input schema of 150 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 12 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 2 |
| `median_days_between_releases` | 0.09 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (150)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_chat_reaction` | openWorldHint | yes | no | `08d05537e090` |
| `add_comment_reaction` | openWorldHint | yes | no | `4225851c32f4` |
| `add_guest_to_folder` | openWorldHint | yes | no | `e65f513a642c` |
| `add_guest_to_list` | openWorldHint | yes | no | `97cdd140bda5` |
| `add_guest_to_task` | openWorldHint | yes | no | `930d7570a7a4` |
| `add_tag_to_task` | openWorldHint | yes | no | `1fba628c3716` |
| `add_task_dependency` | openWorldHint | yes | no | `6320158b0a42` |
| `add_task_link` | openWorldHint | yes | no | `93d576e6098f` |
| `add_task_to_list` | openWorldHint | yes | no | `a64d72e1b74a` |
| `add_time_entry` | — | no | no | `571e6a6d0f1a` |
| `add_time_entry_tags` | — | yes | no | `059b924f662c` |
| `create_bulk_tasks` | openWorldHint | yes | no | `c9177d9920c6` |
| `create_chat_channel` | openWorldHint | yes | no | `f7d00f5ed971` |
| `create_chat_dm` | openWorldHint | yes | no | `3e86688ae807` |
| `create_chat_message` | openWorldHint | yes | no | `8e30fc2738a7` |
| `create_chat_message_reply` | openWorldHint | yes | no | `67999ba1a6f8` |
| `create_checklist` | openWorldHint | yes | no | `32ae3dab6d2b` |
| `create_checklist_item` | openWorldHint | yes | no | `f02a658d78f3` |
| `create_comment` | openWorldHint | no | no | `cce38eb92c70` |
| `create_comment_reply` | openWorldHint | yes | no | `317478f2aa85` |
| `create_custom_field` | — | yes | no | `f535086f6d75` |
| `create_document` | — | yes | no | `f48c094b5f54` |
| `create_document_page` | — | yes | no | `61c6da8dfaa0` |
| `create_folder` | openWorldHint | yes | no | `6860b47b09cd` |
| `create_folder_from_template` | openWorldHint | yes | no | `293420e4b996` |
| `create_goal` | — | yes | no | `2a56a1595e02` |
| `create_key_result` | — | yes | no | `917a38de1dd8` |
| `create_list` | openWorldHint | yes | no | `75d2406ad5ae` |
| `create_list_from_template` | openWorldHint | yes | no | `f59f2e6f6e77` |
| `create_space` | openWorldHint | yes | no | `e31de1fcb8f3` |
| `create_space_tag` | openWorldHint | yes | no | `5e0c205a55d6` |
| `create_task` | openWorldHint | no | no | `b54f08d4b750` |
| `create_task_from_template` | openWorldHint | no | no | `ba111531933a` |
| `create_user_group` | — | yes | no | `51af07ef2f02` |
| `create_view` | — | yes | no | `2532f5fd0a2b` |
| `create_webhook` | — | yes | no | `104d83abd8eb` |
| `delete_bulk_tasks` | destructiveHint, openWorldHint | yes | no | `c511c9388b5f` |
| `delete_chat_channel` | destructiveHint, openWorldHint | yes | no | `ac4961fadc8a` |
| `delete_chat_message` | destructiveHint, openWorldHint | yes | no | `30aa6b717b9c` |
| `delete_checklist` | destructiveHint, openWorldHint | yes | no | `9da1393cf2e7` |
| `delete_checklist_item` | destructiveHint, openWorldHint | yes | no | `5e9898a5eff4` |
| `delete_comment` | destructiveHint, openWorldHint | yes | no | `2eba597dcf83` |
| `delete_folder` | destructiveHint, openWorldHint | no | no | `361b5265ffe8` |
| `delete_goal` | destructiveHint | no | no | `459644d3a5ee` |
| `delete_key_result` | destructiveHint | no | no | `fc0f7f4f4e83` |
| `delete_list` | destructiveHint, openWorldHint | no | no | `c9f0b63ac3bb` |
| `delete_space` | destructiveHint, openWorldHint | no | no | `00363c254f0c` |
| `delete_space_tag` | destructiveHint, openWorldHint | yes | no | `f2e56729fdcd` |
| `delete_task` | destructiveHint, openWorldHint | yes | no | `0a64eca25191` |
| `delete_task_dependency` | destructiveHint, openWorldHint | yes | no | `b9542f54fcd0` |
| `delete_task_link` | destructiveHint, openWorldHint | yes | no | `0987dcd74cf0` |
| `delete_time_entry` | destructiveHint | yes | no | `1a10f2f9ac02` |
| `delete_time_entry_tags` | destructiveHint | yes | no | `f9e5012761cc` |
| `delete_user_group` | destructiveHint | yes | no | `55c77989d5bc` |
| `delete_view` | destructiveHint | no | no | `6b4449f0f42d` |
| `delete_webhook` | destructiveHint | yes | no | `381aeb586946` |
| `duplicate_task` | openWorldHint | yes | no | `e42df4139d56` |
| `edit_checklist` | openWorldHint | yes | no | `0c302316c321` |
| `edit_checklist_item` | openWorldHint | yes | no | `a91f15e33ca1` |
| `edit_guest` | openWorldHint | yes | no | `1fbc170c4c19` |
| `get_active_sprint` | openWorldHint, readOnlyHint | no | no | `6a3a36f703ec` |
| `get_attachment` | openWorldHint, readOnlyHint | no | no | `9329154e4a22` |
| `get_audit_logs` | openWorldHint, readOnlyHint | yes | no | `2ccc8fc3b920` |
| `get_chat_channel` | openWorldHint, readOnlyHint | yes | no | `26eb6cb375d9` |
| `get_chat_channel_followers` | openWorldHint, readOnlyHint | yes | no | `51ab1bbbdbd8` |
| `get_chat_channel_members` | openWorldHint, readOnlyHint | yes | no | `61f5036efb93` |
| `get_chat_message_replies` | openWorldHint, readOnlyHint | yes | no | `94c33c0b9a61` |
| `get_chat_message_subtypes` | openWorldHint, readOnlyHint | no | no | `8aa02a81b901` |
| `get_chat_messages` | openWorldHint, readOnlyHint | yes | no | `5a758e2b6126` |
| `get_chat_reactions` | openWorldHint, readOnlyHint | yes | no | `dc49b1c2cabf` |
| `get_chat_tagged_users` | openWorldHint, readOnlyHint | yes | no | `9b90b9144374` |
| `get_comment_replies` | openWorldHint, readOnlyHint | yes | no | `6eb9122b718f` |
| `get_comment_subtypes` | openWorldHint, readOnlyHint | no | no | `8ae614b22858` |
| `get_comments` | openWorldHint, readOnlyHint | no | no | `799e6e56268a` |
| `get_current_time_entry` | readOnlyHint | no | no | `b3c57980f5cf` |
| `get_document` | openWorldHint, readOnlyHint | no | no | `d26a97eb0ff2` |
| `get_document_page` | readOnlyHint | yes | no | `4aaa4e029543` |
| `get_document_pages` | readOnlyHint | yes | no | `aa754f214144` |
| `get_folder` | readOnlyHint | no | no | `4f02614905c0` |
| `get_goal` | readOnlyHint | no | no | `60b1ff8f43fa` |
| `get_guest` | openWorldHint, readOnlyHint | yes | no | `e810b66462f4` |
| `get_list` | readOnlyHint | no | no | `75b50b846601` |
| `get_space` | readOnlyHint | no | no | `d06f0e1e86e7` |
| `get_sprint_tasks` | openWorldHint, readOnlyHint | no | no | `df229ad136ae` |
| `get_task` | openWorldHint, readOnlyHint | yes | no | `ecc90806b660` |
| `get_task_links` | openWorldHint, readOnlyHint | yes | no | `6eb64e04faa8` |
| `get_task_templates` | openWorldHint, readOnlyHint | no | no | `b9e20c565e2e` |
| `get_time_entries` | readOnlyHint | no | no | `bbc7138b25ce` |
| `get_time_entry_history` | readOnlyHint | yes | no | `d0c1338105ea` |
| `get_time_entry_tags` | readOnlyHint | no | no | `d4b4e7b304e8` |
| `get_time_in_status` | readOnlyHint | yes | no | `6c0ad337b43c` |
| `get_view` | readOnlyHint | no | no | `5cea42089e45` |
| `get_view_tasks` | readOnlyHint | no | no | `a526784d6158` |
| `get_workspace` | openWorldHint, readOnlyHint | no | no | `b39a26453ada` |
| `get_workspace_plan` | openWorldHint, readOnlyHint | no | no | `1b5497dd6764` |
| `get_workspace_seats` | openWorldHint, readOnlyHint | no | no | `3ca14dcc9b7d` |
| `get_workspace_tasks` | openWorldHint, readOnlyHint | no | no | `11f0af800492` |
| `invite_guest` | openWorldHint | yes | no | `c447c317908d` |
| `list_attachments` | openWorldHint, readOnlyHint | no | no | `6d20fdcaaf62` |
| `list_chat_channels` | openWorldHint, readOnlyHint | no | no | `d40ddfe729e9` |
| `list_custom_fields` | readOnlyHint | no | no | `5f7de329207d` |
| `list_document_pages` | readOnlyHint | no | no | `9f304e32174c` |
| `list_documents` | readOnlyHint | no | no | `a44ad80c90b0` |
| `list_folders` | readOnlyHint | no | no | `e01c5a1d0d42` |
| `list_goals` | readOnlyHint | no | no | `b7635d8f4db7` |
| `list_lists` | readOnlyHint | no | no | `21c4b034ec82` |
| `list_space_tags` | readOnlyHint | no | no | `3b97be59b1c5` |
| `list_spaces` | readOnlyHint | no | no | `22b90d838f58` |
| `list_sprints` | openWorldHint, readOnlyHint | no | no | `ca629db4505e` |
| `list_user_groups` | openWorldHint, readOnlyHint | no | no | `0d526eac981b` |
| `list_views` | readOnlyHint | no | no | `9ce3365fbb64` |
| `list_webhooks` | readOnlyHint | no | no | `9d37b098d5d3` |
| `move_bulk_tasks` | openWorldHint | yes | no | `37136ea9355a` |
| `move_folder` | openWorldHint | no | no | `544bbe97291c` |
| `move_list` | openWorldHint | no | no | `e38ee0d199e0` |
| `move_task` | openWorldHint | yes | no | `3848cd0bef33` |
| `remove_chat_reaction` | destructiveHint, openWorldHint | yes | no | `c50e838884fe` |
| `remove_comment_reaction` | destructiveHint, openWorldHint | yes | no | `f66d2f162789` |
| `remove_custom_field_value` | destructiveHint | no | no | `f7d7e51a693f` |
| `remove_guest` | destructiveHint, openWorldHint | yes | no | `2d918c89970d` |
| `remove_guest_from_folder` | destructiveHint, openWorldHint | yes | no | `70bb77aa199b` |
| `remove_guest_from_list` | destructiveHint, openWorldHint | yes | no | `72f605a3681a` |
| `remove_guest_from_task` | destructiveHint, openWorldHint | yes | no | `072f90fa2a94` |
| `remove_tag_from_task` | destructiveHint, openWorldHint | yes | no | `fb9048956232` |
| `remove_task_from_list` | destructiveHint, openWorldHint | yes | no | `645d710a949b` |
| `set_custom_field_value` | — | yes | no | `8915adcf519e` |
| `set_folder_permissions` | openWorldHint | yes | no | `8434f47e2813` |
| `set_list_permissions` | openWorldHint | yes | no | `849c73583a60` |
| `set_space_permissions` | openWorldHint | yes | no | `792c4c0cfb4e` |
| `start_time_entry` | — | no | no | `20e51f7a35b6` |
| `stop_time_entry` | — | no | no | `203faf08c4cb` |
| `submit_feedback` | openWorldHint | yes | no | `0e71116361b9` |
| `update_bulk_tasks` | openWorldHint | yes | no | `22e13ca70432` |
| `update_chat_channel` | openWorldHint | yes | no | `6ca6fba2dbb4` |
| `update_chat_message` | openWorldHint | yes | no | `a88a489e9b3a` |
| `update_comment` | openWorldHint | yes | no | `490c6cbdbf08` |
| `update_document_page` | — | yes | no | `647fb0c3d2e1` |
| `update_folder` | openWorldHint | no | no | `ebac285e895a` |
| `update_goal` | — | no | no | `4023337b26ba` |
| `update_key_result` | — | no | no | `097ae968bcdf` |
| `update_list` | openWorldHint | no | no | `74d6a362680a` |
| `update_space` | openWorldHint | no | no | `eec9cdb9eccb` |
| `update_space_tag` | openWorldHint | yes | no | `010b5beb937b` |
| `update_task` | openWorldHint | yes | no | `29a1f2d985fa` |
| `update_time_entry` | — | yes | no | `019883a70db2` |
| `update_time_entry_tags` | — | yes | no | `6f177d726e94` |
| `update_user_group` | — | yes | no | `868421dfbe38` |
| `update_view` | — | no | no | `5d221964831f` |
| `update_webhook` | — | yes | no | `c3e62da60de2` |
| `upload_attachment` | openWorldHint | no | no | `ee5b5161e8cb` |



## Change history

No tool-definition changes observed.
