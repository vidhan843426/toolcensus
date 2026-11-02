# `google-services-mcp`

| | |
|---|---|
| Latest observed version | `0.1.97` |
| Status | ok |
| Weekly downloads | 11334 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:d1b7400f16e2a041` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 134 of 134 tools.
    - Consider `additionalProperties: false` on the input schema of 132 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 3 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 225 |
| `median_days_between_releases` | 0.0 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (134)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `google_account_add` | — | yes | no | `1f66930a682a` |
| `google_account_list` | — | no | no | `081ac3650dc2` |
| `google_account_remove` | — | yes | no | `7be5c5cc446e` |
| `google_account_set_default` | — | yes | no | `4a1053754682` |
| `google_account_status` | — | no | no | `40742cafd9da` |
| `google_calendar_create` | — | yes | no | `7a8bb70acf6e` |
| `google_calendar_create_event` | — | yes | no | `2e6d801cce9a` |
| `google_calendar_create_meet` | — | yes | no | `c0a780cfa0e6` |
| `google_calendar_delete` | — | yes | no | `201fc3c878a5` |
| `google_calendar_delete_event` | — | yes | no | `d76d4d5434ff` |
| `google_calendar_free_busy` | — | yes | no | `50b29c0aec97` |
| `google_calendar_get_event` | — | yes | no | `06a67a767b8f` |
| `google_calendar_list_calendars` | — | no | no | `b3cca082ecd9` |
| `google_calendar_list_events` | — | no | no | `bdb0f08ac5dc` |
| `google_calendar_respond` | — | yes | no | `7324de4d6237` |
| `google_calendar_update` | — | yes | no | `2a24d683dcfe` |
| `google_calendar_update_event` | — | yes | no | `b20dd08cb65c` |
| `google_contacts_create` | — | yes | no | `9367a27a0d51` |
| `google_contacts_delete` | — | yes | no | `834143350c54` |
| `google_contacts_get` | — | yes | no | `a3125a973122` |
| `google_contacts_list` | — | no | no | `7e94ab2dfe00` |
| `google_contacts_search` | — | yes | no | `7b1cd91657a3` |
| `google_contacts_update` | — | yes | no | `381aff033b1b` |
| `google_docs_batch_update` | — | yes | no | `56e1ee13249b` |
| `google_docs_create` | — | yes | no | `9125e6f8bd91` |
| `google_docs_delete_range` | — | yes | no | `bf288b402ac1` |
| `google_docs_get` | — | yes | no | `9015604716a2` |
| `google_docs_insert_inline_image` | — | yes | no | `53026b6957e1` |
| `google_docs_insert_table` | — | yes | no | `1dfcd391794e` |
| `google_docs_insert_text` | — | yes | no | `106b5eea2d76` |
| `google_docs_read` | — | yes | no | `15c6ae52da01` |
| `google_docs_replace_text` | — | yes | no | `5a5da1f8c632` |
| `google_drive_copy` | — | yes | no | `2f4baab7ac91` |
| `google_drive_create_folder` | — | yes | no | `538513083d25` |
| `google_drive_delete` | — | yes | no | `ba9e8bf19353` |
| `google_drive_delete_permission` | — | yes | no | `fbcb22401302` |
| `google_drive_download` | — | yes | no | `bf973ce8ad9f` |
| `google_drive_export` | — | yes | no | `cd88908d2d9e` |
| `google_drive_get` | — | yes | no | `432e4c0b5763` |
| `google_drive_list` | — | no | no | `9e6d85b898cf` |
| `google_drive_list_permissions` | — | yes | no | `81a0ae63e931` |
| `google_drive_move` | — | yes | no | `dcb9e7149af1` |
| `google_drive_restore` | — | yes | no | `6309f33d45a8` |
| `google_drive_share` | — | yes | no | `747ca8a12638` |
| `google_drive_trash` | — | yes | no | `eb0e1d703666` |
| `google_drive_update` | — | yes | no | `51acef59f298` |
| `google_drive_upload` | — | yes | no | `ea7cdd0777ba` |
| `google_forms_add_question` | — | yes | no | `5c13f9f66bb9` |
| `google_forms_create` | — | yes | no | `04a052ea6e51` |
| `google_forms_delete` | — | yes | no | `e8496de98c25` |
| `google_forms_delete_question` | — | yes | no | `bab4104c3719` |
| `google_forms_export_responses` | — | yes | no | `8a306cac7b9b` |
| `google_forms_get` | — | yes | no | `8b5610c283c4` |
| `google_forms_move_question` | — | yes | no | `fa6f439786b0` |
| `google_forms_rename` | — | yes | no | `b293a556b1a5` |
| `google_forms_responses` | — | yes | no | `de799b9c50f5` |
| `google_forms_update_question` | — | yes | no | `202e92006ddb` |
| `google_gmail_delete` | — | yes | no | `ea736f01ee67` |
| `google_gmail_drafts_create` | — | yes | no | `8364b817eeb6` |
| `google_gmail_drafts_delete` | — | yes | no | `ad917fc8f773` |
| `google_gmail_drafts_get` | — | yes | no | `d08b364c5b76` |
| `google_gmail_drafts_list` | — | no | no | `b831fc263d0a` |
| `google_gmail_drafts_send` | — | yes | no | `e69dfb009bfd` |
| `google_gmail_drafts_update` | — | yes | no | `661fcd3a6827` |
| `google_gmail_filters_create` | — | no | no | `7f48dfd09c19` |
| `google_gmail_filters_delete` | — | yes | no | `2ff49170a177` |
| `google_gmail_filters_list` | — | no | no | `88d277dc1e10` |
| `google_gmail_get` | — | yes | no | `0b407e7fbbe6` |
| `google_gmail_get_attachment` | — | yes | no | `74d7b9704711` |
| `google_gmail_labels_create` | — | yes | no | `61fbb7fb3cc8` |
| `google_gmail_labels_delete` | — | yes | no | `526f4d0616be` |
| `google_gmail_labels_list` | — | no | no | `5ad3cc938d6f` |
| `google_gmail_labels_update` | — | yes | no | `8dcae9a51e9e` |
| `google_gmail_list` | — | no | no | `ed9735f777cc` |
| `google_gmail_list_attachments` | — | yes | no | `a367b43fdabe` |
| `google_gmail_modify` | — | yes | no | `e0ac0a263f20` |
| `google_gmail_reply` | — | yes | no | `2d7d9a66af2a` |
| `google_gmail_send` | — | yes | no | `b305a313db40` |
| `google_gmail_sendas_create` | — | yes | no | `fb7b2576c3b7` |
| `google_gmail_sendas_list` | — | no | no | `1933dd416754` |
| `google_gmail_threads_get` | — | yes | no | `78a01e67176c` |
| `google_gmail_threads_list` | — | no | no | `1ff0ff7058b4` |
| `google_gmail_trash` | — | yes | no | `6cb0c4830d33` |
| `google_gmail_untrash` | — | yes | no | `9aaaeb232f11` |
| `google_gmail_vacation_get` | — | no | no | `b78af09413c1` |
| `google_gmail_vacation_update` | — | no | no | `12c663599433` |
| `google_sheets_add_sheet` | — | yes | no | `fc7ee97bb502` |
| `google_sheets_append` | — | yes | no | `b847039b7395` |
| `google_sheets_batch_update` | — | yes | no | `0bf96875fb7a` |
| `google_sheets_create` | — | yes | no | `c7cbcac1f04d` |
| `google_sheets_delete_rows` | — | yes | no | `872af0c7e433` |
| `google_sheets_delete_sheet` | — | yes | no | `538673ced277` |
| `google_sheets_get` | — | yes | no | `d1b03a0e8838` |
| `google_sheets_get_named_ranges` | — | yes | no | `20fc46dc7163` |
| `google_sheets_insert_rows` | — | yes | no | `fd147c72c52c` |
| `google_sheets_read` | — | yes | no | `0ac0d42295eb` |
| `google_sheets_rename_sheet` | — | yes | no | `1d752bd7ef00` |
| `google_sheets_set_named_range` | — | yes | no | `b5f2ffa20966` |
| `google_sheets_write` | — | yes | no | `b8b24183cd02` |
| `google_slides_add_slide` | — | yes | no | `d0f7bcb24631` |
| `google_slides_batch_update` | — | yes | no | `c9b7cf60f3f3` |
| `google_slides_create` | — | yes | no | `470987d4db43` |
| `google_slides_create_image` | — | yes | no | `cfacae5c65d5` |
| `google_slides_create_textbox` | — | yes | no | `666d72303993` |
| `google_slides_delete_slide` | — | yes | no | `7db30a448647` |
| `google_slides_duplicate_slide` | — | yes | no | `0b49adb57b56` |
| `google_slides_get` | — | yes | no | `33a372863bf1` |
| `google_slides_get_page` | — | yes | no | `33ccf858c272` |
| `google_slides_move_slide` | — | yes | no | `ebe9520b78b7` |
| `google_slides_replace_text` | — | yes | no | `0ee790dfe70e` |
| `google_tasks_complete` | — | yes | no | `73a6804edb0b` |
| `google_tasks_create` | — | yes | no | `22602f04522f` |
| `google_tasks_create_list` | — | yes | no | `b58f5bd63bba` |
| `google_tasks_delete` | — | yes | no | `440a5dbc6333` |
| `google_tasks_delete_list` | — | yes | no | `7ed70073e517` |
| `google_tasks_list` | — | no | no | `49ae3e3c1b7f` |
| `google_tasks_list_lists` | — | no | no | `34340f71c559` |
| `google_tasks_update` | — | yes | no | `fca585917a37` |
| `google_tasks_update_list` | — | yes | no | `8220f20ddcba` |
| `google_youtube_add_to_playlist` | — | yes | no | `17e673fafc59` |
| `google_youtube_create_playlist` | — | yes | no | `293cb5acb118` |
| `google_youtube_delete_playlist` | — | yes | no | `b89c036ea66f` |
| `google_youtube_get_video` | — | yes | no | `7d37e73aa00c` |
| `google_youtube_insert_comment` | — | yes | no | `a6b5378296a4` |
| `google_youtube_list_comments` | — | yes | no | `1d6518dbd639` |
| `google_youtube_list_playlists` | — | no | no | `038065f7f16f` |
| `google_youtube_mark_comment_spam` | — | yes | no | `1b94d16e9cb8` |
| `google_youtube_my_videos` | — | no | no | `49f20aab1f51` |
| `google_youtube_remove_from_playlist` | — | yes | no | `6fff2e250684` |
| `google_youtube_search` | — | yes | no | `cf0bbb1edaef` |
| `google_youtube_set_comment_moderation` | — | yes | no | `e57043c4381c` |
| `google_youtube_subscriptions` | — | no | no | `afd96609ea7a` |
| `google_youtube_update_video` | — | yes | no | `f19d13479b08` |
| `google_youtube_upload` | — | yes | no | `cddca2c8a7f2` |



## Change history

No tool-definition changes observed.
