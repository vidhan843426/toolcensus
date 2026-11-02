# `figma-console-mcp`

| | |
|---|---|
| Latest observed version | `1.46.0` |
| Status | ok |
| Weekly downloads | 55745 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:563dc98209d5c0c3` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 130 of 130 tools.
    - Consider `additionalProperties: false` on the input schema of 121 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 9 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 25 |
| `median_days_between_releases` | 0.71 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (130)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `figjam_auto_arrange` | — | yes | no | `eab625e1fee7` |
| `figjam_create_code_block` | — | yes | no | `160fb3047057` |
| `figjam_create_connector` | — | yes | no | `ff9eb4a2841f` |
| `figjam_create_section` | — | no | no | `b7d88eace32a` |
| `figjam_create_shape_with_text` | — | no | no | `6ce10d86d81c` |
| `figjam_create_stickies` | — | yes | no | `270b69468ba2` |
| `figjam_create_sticky` | — | yes | no | `5faad04b5e56` |
| `figjam_create_table` | — | yes | no | `87515517a747` |
| `figjam_get_board_contents` | — | no | no | `68bc32bb8d76` |
| `figjam_get_connections` | — | no | no | `3f4c07f27331` |
| `figma_add_component_property` | — | yes | no | `e3e7d8349604` |
| `figma_add_mode` | — | yes | no | `b36e6259992b` |
| `figma_add_shape_to_slide` | — | yes | no | `16953bb3f546` |
| `figma_add_slot_property` | — | yes | no | `2274f4054cb8` |
| `figma_add_text_to_slide` | — | yes | no | `4114a40edb3e` |
| `figma_analyze_component_set` | — | yes | no | `d5546c1e2701` |
| `figma_append_to_slot` | — | no | no | `a84b8642ee06` |
| `figma_apply_animation` | — | yes | no | `50f4029a55b4` |
| `figma_apply_shader` | — | yes | no | `db412604f518` |
| `figma_arrange_component_set` | — | no | no | `dbadbbda93ff` |
| `figma_audit_component_accessibility` | — | no | no | `61db696ff1ef` |
| `figma_audit_design_system_report` | — | no | no | `c6a9e7d214e7` |
| `figma_batch_create_variables` | — | yes | no | `02399df624c9` |
| `figma_batch_update_variables` | — | yes | no | `f63aae1e0f77` |
| `figma_blame_node` | — | no | no | `341fd9f9ca2d` |
| `figma_capture_screenshot` | — | no | no | `4c4d79411adb` |
| `figma_check_design_parity` | — | yes | no | `9c7e088a54aa` |
| `figma_clear_console` | — | no | no | `970348c6e347` |
| `figma_clone_node` | — | yes | no | `a67c62ca1e06` |
| `figma_create_child` | — | yes | no | `789e3cf2ca40` |
| `figma_create_component_set` | — | no | no | `6ab8f439dfc0` |
| `figma_create_slide` | — | no | no | `2c685a9d2888` |
| `figma_create_slot` | — | yes | no | `3ea0101132c2` |
| `figma_create_variable` | — | yes | no | `441298f2b11b` |
| `figma_create_variable_collection` | — | yes | no | `cac5b8a695af` |
| `figma_delete_comment` | — | yes | no | `70faa48fe1cb` |
| `figma_delete_component_property` | — | yes | no | `69fbb77ff6c8` |
| `figma_delete_node` | — | yes | no | `153bd56dfe05` |
| `figma_delete_slide` | — | yes | no | `6815a672ed83` |
| `figma_delete_variable` | — | yes | no | `d9c21d9b1624` |
| `figma_delete_variable_collection` | — | yes | no | `b7e696b1ab45` |
| `figma_diagnose` | — | no | no | `1382cec72ba0` |
| `figma_diff_versions` | — | yes | no | `e2eeb527a2e0` |
| `figma_ds_analyze` | — | yes | no | `7ff4d3de2e32` |
| `figma_ds_extract_component` | — | yes | no | `9026d6ab5acf` |
| `figma_ds_extract_tokens` | — | no | no | `062ca9573e4d` |
| `figma_ds_scaffold` | — | yes | no | `bfde000f5d30` |
| `figma_ds_setup_storybook` | — | yes | no | `f970eb80dd2e` |
| `figma_ds_status` | — | yes | no | `18c5946d235a` |
| `figma_ds_verify` | — | yes | no | `0850550e147f` |
| `figma_duplicate_slide` | — | yes | no | `a69e90a3a016` |
| `figma_edit_component_property` | — | yes | no | `9d0719f315a4` |
| `figma_execute` | — | yes | no | `6dbbde162150` |
| `figma_execute_across_files` | — | yes | no | `7f8c9065cfd7` |
| `figma_export_animation` | — | yes | no | `efe8f9495d73` |
| `figma_export_tokens` | — | no | no | `50d235683dd3` |
| `figma_focus_slide` | — | yes | no | `c1447642b197` |
| `figma_generate_changelog` | — | yes | no | `e31b664a76fd` |
| `figma_generate_component_doc` | — | yes | no | `5fe030cb60ec` |
| `figma_get_animations` | — | no | no | `b3293e64c198` |
| `figma_get_annotation_categories` | — | no | no | `2518647c3d7c` |
| `figma_get_annotations` | — | yes | no | `732f69082235` |
| `figma_get_changes_since_version` | — | yes | no | `65b6da0e2414` |
| `figma_get_code_layers` | — | no | no | `45aa583230b6` |
| `figma_get_comments` | — | no | no | `8bf73e8607c9` |
| `figma_get_component` | — | yes | no | `3d4445003712` |
| `figma_get_component_details` | — | no | no | `41edd728a21c` |
| `figma_get_component_for_development` | — | yes | no | `c000ee3b8800` |
| `figma_get_component_for_development_deep` | — | yes | no | `1a80af538275` |
| `figma_get_component_image` | — | yes | no | `ffc743d922f7` |
| `figma_get_console_logs` | — | no | no | `f1574c435c02` |
| `figma_get_design_changes` | — | no | no | `2a627dfb90e9` |
| `figma_get_design_system_kit` | — | no | no | `c29e1f017bef` |
| `figma_get_design_system_summary` | — | no | no | `26c39234b64c` |
| `figma_get_file_at_version` | — | yes | no | `c6d515430228` |
| `figma_get_file_data` | — | no | no | `eda34a831897` |
| `figma_get_file_for_plugin` | — | no | no | `8c9299b89de9` |
| `figma_get_file_versions` | — | no | no | `6d952832cbaf` |
| `figma_get_focused_slide` | — | no | no | `d87dbf2126a1` |
| `figma_get_library_component_by_key` | — | yes | no | `cc3aff7b0c20` |
| `figma_get_library_components` | — | no | no | `4797cc9446d2` |
| `figma_get_library_variables` | — | no | no | `dcf34605cdd0` |
| `figma_get_selection` | — | no | no | `eb5befc39c85` |
| `figma_get_slide_content` | — | yes | no | `663ff5a1bbd5` |
| `figma_get_slide_grid` | — | no | no | `925fb0f09ca5` |
| `figma_get_slide_transition` | — | yes | no | `864707a4abd3` |
| `figma_get_slots` | — | yes | no | `46c031aaf8da` |
| `figma_get_status` | — | no | no | `50be004bb20a` |
| `figma_get_styles` | — | no | no | `f9e39a3a5e60` |
| `figma_get_text_styles` | — | no | no | `a4dda3f03933` |
| `figma_get_token_values` | — | no | no | `87a1d8d49163` |
| `figma_get_variables` | — | no | no | `84b9aa47002e` |
| `figma_import_library_variable` | — | yes | no | `7cdcbe536133` |
| `figma_import_tokens` | — | no | no | `1932be0866b6` |
| `figma_instantiate_component` | — | no | no | `a2ab5c772869` |
| `figma_lint_design` | — | no | no | `157f5cd870d5` |
| `figma_list_open_files` | — | no | no | `1b7f43e5f61f` |
| `figma_list_shaders` | — | no | no | `0c9690e015c4` |
| `figma_list_slides` | — | no | no | `d06f2404f496` |
| `figma_manage_animation_styles` | — | yes | no | `3a625266d1f0` |
| `figma_move_node` | — | yes | no | `a8a33fe0d9f3` |
| `figma_navigate` | — | yes | no | `7a720a7f475d` |
| `figma_post_comment` | — | yes | no | `e2d27bbdecd3` |
| `figma_reconnect` | — | no | no | `17d8992a36fa` |
| `figma_reload_plugin` | — | no | no | `43d184ddd6b7` |
| `figma_remove_animation` | — | yes | no | `c30a0244b8b2` |
| `figma_rename_mode` | — | yes | no | `6e3bf56fd89c` |
| `figma_rename_node` | — | yes | no | `ea60167c48d4` |
| `figma_rename_variable` | — | yes | no | `90d8a7982e18` |
| `figma_reorder_slides` | — | yes | no | `9916ef13658b` |
| `figma_reset_slot` | — | no | no | `06157fc3d711` |
| `figma_resize_node` | — | yes | no | `07bf92a91bef` |
| `figma_scan_code_accessibility` | — | yes | no | `5ad62608aaff` |
| `figma_search_components` | — | no | no | `801d5ffe6f94` |
| `figma_set_annotations` | — | yes | no | `4d9d03ea3d4e` |
| `figma_set_description` | — | yes | no | `c33f83d3b724` |
| `figma_set_fills` | — | yes | no | `717048c4b1b8` |
| `figma_set_image_fill` | — | yes | no | `913df587cb7b` |
| `figma_set_instance_properties` | — | yes | no | `8d14ba53a2eb` |
| `figma_set_layout` | — | yes | no | `3e3c1f7b1236` |
| `figma_set_slide_background` | — | yes | no | `b0e9d694f8d8` |
| `figma_set_slide_transition` | — | yes | no | `4d33ee8cfb0b` |
| `figma_set_slides_view_mode` | — | yes | no | `6209b6ba28d0` |
| `figma_set_strokes` | — | yes | no | `4d4ec5b9a2b5` |
| `figma_set_text` | — | yes | no | `ba815027cb5d` |
| `figma_setup_design_tokens` | — | yes | no | `6255d65a69db` |
| `figma_skip_slide` | — | yes | no | `a78612778702` |
| `figma_take_screenshot` | — | no | no | `64cad01e61f5` |
| `figma_update_variable` | — | yes | no | `b38219078a91` |
| `figma_watch_console` | — | no | no | `b10fc4871208` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_apply_animation` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_apply_shader` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_export_animation` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_animations` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_code_layers` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_list_shaders` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_manage_animation_styles` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_remove_animation` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_layout` | tool_added |  |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_auto_arrange` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_code_block` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_connector` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_section` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_shape_with_text` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_stickies` | input_schema_changed (schema_other) | additionalProperties loosened; property 'stickies' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_sticky` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_create_table` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figjam_get_board_contents` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_add_component_property` | input_schema_changed (schema_other) | additionalProperties loosened; property 'preferredValues' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_add_mode` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_add_shape_to_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_add_slot_property` | input_schema_changed (schema_other) | additionalProperties loosened; property 'preferredValues' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_add_text_to_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_analyze_component_set` | description_changed | length 1153 -&gt; 1333 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_analyze_component_set` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_append_to_slot` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_arrange_component_set` | input_schema_changed (schema_other) | additionalProperties loosened; property 'options' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_audit_component_accessibility` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_audit_design_system_report` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_batch_create_variables` | input_schema_changed (schema_other) | additionalProperties loosened; property 'variables' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_batch_update_variables` | input_schema_changed (schema_other) | additionalProperties loosened; property 'updates' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_blame_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_capture_screenshot` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_check_design_parity` | input_schema_changed (schema_other) | additionalProperties loosened; property 'codeSpec' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_clone_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_child` | input_schema_changed (schema_other) | additionalProperties loosened; property 'properties' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_component_set` | input_schema_changed (schema_other) | additionalProperties loosened; property 'arrangeOptions' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_slide` | input_schema_changed (schema_other) | additionalProperties loosened; property 'col': maximum added; property 'row': maximum added |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_slot` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_variable` | description_changed | length 238 -&gt; 264 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_variable` | input_schema_changed (schema_widened) | additionalProperties loosened; property 'resolvedType': enum values added |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_create_variable_collection` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_comment` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_component_property` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_variable` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_delete_variable_collection` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_diagnose` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_diff_versions` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_analyze` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_extract_component` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_extract_tokens` | input_schema_changed (schema_other) | additionalProperties loosened; property 'dtcgDialect' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_scaffold` | input_schema_changed (schema_other) | additionalProperties loosened; property 'dtcgDialect' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_setup_storybook` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_status` | input_schema_changed (schema_other) | additionalProperties loosened; property 'update' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_ds_verify` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_duplicate_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_edit_component_property` | input_schema_changed (schema_other) | additionalProperties loosened; property 'newValue' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_execute` | input_schema_changed (schema_other) | additionalProperties loosened; property 'timeout' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_execute_across_files` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_export_tokens` | input_schema_changed (schema_other) | additionalProperties loosened; property 'dtcgDialect' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_focus_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_generate_changelog` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_generate_component_doc` | input_schema_changed (schema_other) | additionalProperties loosened; property 'codeInfo' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_annotations` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_changes_since_version` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_comments` | description_changed | length 166 -&gt; 473 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_comments` | input_schema_changed (schema_other) | property 'format' added (optional); property 'include_nested' added (optional); property 'limit' added (optional); property 'node_id' added (optional); property 'offset' added (optional); property 'since' added (optional); property 'thread_id' added (optional); additionalProperties loosened; property 'fileUrl' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_component` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_component_details` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_component_for_development` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_component_for_development_deep` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_component_image` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_console_logs` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_design_changes` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_design_system_kit` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_design_system_summary` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_file_at_version` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_file_data` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_file_for_plugin` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_file_versions` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_library_component_by_key` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_library_components` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_library_variables` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_selection` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_slide_content` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_slide_transition` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_slots` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_status` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_styles` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_token_values` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_get_variables` | input_schema_changed (schema_other) | additionalProperties loosened; property 'page': maximum added |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_import_library_variable` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_import_tokens` | description_changed | length 2774 -&gt; 2872 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_import_tokens` | input_schema_changed (schema_other) | additionalProperties loosened; property 'files' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_instantiate_component` | input_schema_changed (schema_other) | additionalProperties loosened; property 'position' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_lint_design` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_move_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_navigate` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_post_comment` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_reload_plugin` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_rename_mode` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_rename_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_rename_variable` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_reorder_slides` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_reset_slot` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_resize_node` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_scan_code_accessibility` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_search_components` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_annotations` | input_schema_changed (schema_other) | additionalProperties loosened; property 'annotations' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_description` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_fills` | description_changed | length 265 -&gt; 290 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_fills` | input_schema_changed (schema_other) | additionalProperties loosened; property 'fills' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_image_fill` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_instance_properties` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_slide_background` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_slide_transition` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_slides_view_mode` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_strokes` | description_changed | length 213 -&gt; 260 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_strokes` | input_schema_changed (schema_other) | additionalProperties loosened; property 'strokes' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_text` | description_changed | length 298 -&gt; 467 |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_set_text` | input_schema_changed (schema_other) | property 'fontVariations' added (optional); property 'textWrapStyle' added (optional); property 'text' no longer required; additionalProperties loosened; property 'text' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_setup_design_tokens` | input_schema_changed (schema_other) | additionalProperties loosened; property 'tokens' changed (annotations/descriptions) |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_skip_slide` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_take_screenshot` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_update_variable` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-45 | `1.41.4` → `1.46.0` | `figma_watch_console` | input_schema_changed (schema_widened) | additionalProperties loosened |


