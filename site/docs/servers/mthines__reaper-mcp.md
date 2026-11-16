# `@mthines/reaper-mcp`

| | |
|---|---|
| Latest observed version | `0.98.0` |
| Status | ok |
| Weekly downloads | 10945 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:cb9706abfa10f9e6` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 190 of 190 tools.
    - Consider `additionalProperties: false` on the input schema of 171 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 11 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 100 |
| `median_days_between_releases` | 0.01 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (190)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_fx` | — | yes | no | `570ef53b82ef` |
| `add_hardware_output` | — | yes | no | `1c515a8838f6` |
| `add_marker` | — | yes | no | `dcb639b23b35` |
| `add_monitoring_fx` | — | yes | no | `9601213a5a5f` |
| `add_region` | — | yes | no | `0a759faa8e46` |
| `add_send` | — | yes | no | `c7adfcd76f05` |
| `add_stretch_marker` | — | yes | no | `ca5f196738dd` |
| `add_stretch_markers` | — | yes | no | `4b246f135ead` |
| `add_take_fx` | — | yes | no | `2093b8095b09` |
| `add_tempo_marker` | — | yes | no | `dabd8115aec5` |
| `add_track` | — | no | no | `6bfc2de023be` |
| `align_audio_to_guide` | — | yes | no | `26527c684e0c` |
| `analyze_audio_file` | — | yes | no | `de8a3d95a14d` |
| `analyze_fx` | — | yes | no | `efd1aeff6ddf` |
| `analyze_loudness_curve` | — | no | no | `1708c2b7fd56` |
| `analyze_midi` | — | yes | no | `632647820531` |
| `analyze_stereo_bands` | — | no | no | `7facdc339fbd` |
| `analyze_track_aesthetics` | — | yes | no | `b5472e81653c` |
| `analyze_track_offline` | — | yes | no | `eba41e1e7687` |
| `apply_fx_to_items` | — | yes | no | `812b22379827` |
| `clear_envelope` | — | yes | no | `a8b8ebee3a9c` |
| `comp_lanes` | — | yes | no | `ce4306b7c176` |
| `copy_fx` | — | yes | no | `fe2d9134434d` |
| `copy_media_items` | — | yes | no | `b5aecace69a3` |
| `copy_section` | — | yes | no | `a029208ae3b6` |
| `create_midi_item` | — | yes | no | `f0abc2b2fad8` |
| `create_track_envelope` | — | yes | no | `007fcc703151` |
| `create_transient_automation` | — | yes | no | `c4aba3936ab0` |
| `delete_automation_item` | — | yes | no | `f10a3bf00a87` |
| `delete_envelope_point` | — | yes | no | `ca5e7b1071ac` |
| `delete_marker` | — | yes | no | `e99274988382` |
| `delete_media_item` | — | yes | no | `f59466f997a0` |
| `delete_midi_cc` | — | yes | no | `798596667186` |
| `delete_midi_note` | — | yes | no | `c8aed587ab65` |
| `delete_region` | — | yes | no | `55d9c9420c0d` |
| `delete_stretch_marker` | — | yes | no | `736e3baa0fd8` |
| `delete_tempo_marker` | — | yes | no | `ba6bc2cdc5f1` |
| `delete_track` | — | yes | no | `7bf241bcdaa8` |
| `detect_chords` | — | no | no | `bc6b30628f44` |
| `detect_key` | — | no | no | `e2e8abb3ab83` |
| `detect_transients` | — | no | no | `2d225e3239c8` |
| `disable_tool_category` | — | yes | no | `7aecd2e547cd` |
| `edit_envelope_points` | — | yes | no | `281d4242b1f1` |
| `edit_marker` | — | yes | no | `044b232c614a` |
| `edit_midi_note` | — | yes | no | `82cc63ab3aec` |
| `edit_midi_notes` | — | yes | no | `33cdff97070c` |
| `edit_region` | — | yes | no | `58521998cdcf` |
| `edit_stretch_markers` | — | yes | no | `cab6af33f18d` |
| `edit_tempo_marker` | — | yes | no | `cb14d64b258a` |
| `enable_tool_category` | — | yes | no | `a8e5dbc53e5c` |
| `freeze_tracks` | — | yes | no | `284748775e3d` |
| `get_action` | — | yes | no | `c98131e90bf8` |
| `get_builtin_knowledge` | — | yes | no | `d98f6ea757b8` |
| `get_envelope_points` | — | yes | no | `45f7de6869c7` |
| `get_fx_param_modulation` | — | yes | no | `96b29cc70bed` |
| `get_fx_parameters` | — | yes | no | `62724778a57c` |
| `get_fx_pins` | — | yes | no | `47b859eb89f2` |
| `get_fx_preset_list` | — | yes | no | `223fc60f24b2` |
| `get_item_appearance` | — | yes | no | `789b8e11c51a` |
| `get_media_item_properties` | — | yes | no | `92f66df1d335` |
| `get_midi_cc` | — | yes | no | `57288724a59b` |
| `get_midi_item_properties` | — | yes | no | `e1dd529e81ad` |
| `get_midi_notes` | — | yes | no | `d73f43ac07ea` |
| `get_project_info` | — | no | no | `47c8fca92fb2` |
| `get_project_settings` | — | no | no | `6e1e159f0bdc` |
| `get_record_setup` | — | no | no | `5af1903882ee` |
| `get_render_settings` | — | no | no | `bf3cf13deb37` |
| `get_selected_items` | — | no | no | `76e7145c6472` |
| `get_selected_tracks` | — | no | no | `6a7dd63693b9` |
| `get_stretch_markers` | — | yes | no | `af676adde4e6` |
| `get_take_fx` | — | yes | no | `4599be7b5ab1` |
| `get_tempo_map` | — | no | no | `0a84f7297e06` |
| `get_time_selection` | — | no | no | `20304b7c5e31` |
| `get_track_envelopes` | — | yes | no | `123482978973` |
| `get_track_lanes` | — | yes | no | `e577cfc47ea1` |
| `get_track_properties` | — | yes | no | `2c0720e0774f` |
| `get_track_routing` | — | yes | no | `cfb560701686` |
| `get_transport_state` | — | no | no | `83f1763538f1` |
| `import_midi_file` | — | yes | no | `18b66992287b` |
| `insert_audio_file` | — | yes | no | `19f72b43a3eb` |
| `insert_automation_item` | — | yes | no | `5d7eb415e4a4` |
| `insert_envelope_point` | — | yes | no | `4598fc315b15` |
| `insert_envelope_points` | — | yes | no | `290e7ab250f1` |
| `insert_midi_cc` | — | yes | no | `4dcac3259d63` |
| `insert_midi_note` | — | yes | no | `5735945a1c07` |
| `insert_midi_notes` | — | yes | no | `b890b7132054` |
| `insert_time` | — | yes | no | `b6383a56ccc6` |
| `insert_track_template` | — | yes | no | `31f3791b2047` |
| `list_automation_items` | — | yes | no | `d26d350be65a` |
| `list_available_fx` | — | no | no | `a7a95153df8a` |
| `list_builtin_knowledge` | — | no | no | `4a35f91a62a6` |
| `list_fx_chains` | — | no | no | `5deb4d212547` |
| `list_markers` | — | no | no | `4a33cb4fa8a2` |
| `list_media_items` | — | yes | no | `53f19c2a5b51` |
| `list_midi_items` | — | yes | no | `eb5448701b02` |
| `list_monitoring_fx` | — | no | no | `213008d56236` |
| `list_regions` | — | no | no | `d745d645d9a0` |
| `list_takes` | — | yes | no | `adb72ebc53bf` |
| `list_tool_categories` | — | no | no | `7bc4744c8f5f` |
| `list_track_templates` | — | no | no | `de7bb44ce161` |
| `list_tracks` | — | no | no | `507175f6f0e6` |
| `load_fx_chain` | — | yes | no | `eadbbe9f3dd0` |
| `measure_masking` | — | yes | no | `ca0ebd6fca00` |
| `measure_track_alignment` | — | yes | no | `c43083595fe4` |
| `measure_tracks` | — | yes | no | `171ab9342b6b` |
| `move_fx` | — | yes | no | `33879529c384` |
| `move_media_item` | — | yes | no | `44856a81b7c6` |
| `move_track` | — | yes | no | `c7ae38abcf5e` |
| `play` | — | no | no | `cb836dc229a4` |
| `process_items` | — | yes | no | `781b8ba7bd2d` |
| `quantize_audio` | — | yes | no | `77bb3ab553c1` |
| `quantize_midi` | — | yes | no | `0bfb288bf0b1` |
| `read_track_correlation` | — | yes | no | `b536943d8291` |
| `read_track_crest` | — | yes | no | `2372011947f1` |
| `read_track_lufs` | — | yes | no | `29b5effc3ea4` |
| `read_track_meters` | — | yes | no | `48b2dfc382e0` |
| `read_track_spectrum` | — | yes | no | `2dc57789be9f` |
| `record` | — | no | no | `0cf5ed45e6d9` |
| `redo_project` | — | no | no | `d873e08b348c` |
| `remove_envelope_points` | — | yes | no | `893a5a3ba708` |
| `remove_fx` | — | yes | no | `87aca10816e7` |
| `remove_monitoring_fx` | — | yes | no | `2b20ba7f7f33` |
| `remove_send` | — | yes | no | `99f8650d3786` |
| `remove_take_fx` | — | yes | no | `c6ab70d3e95e` |
| `remove_time` | — | yes | no | `b55333b5119b` |
| `rename_fx` | — | yes | no | `d48040736af4` |
| `render_project` | — | no | no | `95c06eaad29f` |
| `render_versions` | — | yes | no | `a3878d78e265` |
| `report_plugin_build` | — | yes | no | `252c6443b7be` |
| `report_plugin_research` | — | yes | no | `2768e4f28466` |
| `run_action` | — | yes | no | `1e6db1f0c7b9` |
| `run_plan` | — | yes | no | `d96930d93f1f` |
| `save_fx_chain` | — | yes | no | `a9b6886f7785` |
| `save_project` | — | no | no | `501e95837031` |
| `save_track_template` | — | yes | no | `a79e19ee290d` |
| `search_actions` | — | yes | no | `7462a2454f1c` |
| `search_fx` | — | yes | no | `64f5889ad89b` |
| `send_midi_cc` | — | yes | no | `cebc23c64d5c` |
| `send_midi_note` | — | yes | no | `e754e99dadbd` |
| `send_midi_pc` | — | yes | no | `cb5005b3502e` |
| `separate_stems` | — | no | no | `711de53d75b1` |
| `set_active_take` | — | yes | no | `a5057f1d9d31` |
| `set_automation_item` | — | yes | no | `fd5f7f4425d6` |
| `set_automation_mode` | — | no | no | `20c2ac43ed59` |
| `set_cursor_position` | — | yes | no | `819eafab2f72` |
| `set_envelope_properties` | — | yes | no | `9e5aaa239d13` |
| `set_fx_enabled` | — | yes | no | `ab33367f9664` |
| `set_fx_offline` | — | yes | no | `104d5a9fa406` |
| `set_fx_param_modulation` | — | yes | no | `ec2c3a5ff151` |
| `set_fx_parameter` | — | yes | no | `85f76aae76fa` |
| `set_fx_pins` | — | yes | no | `7390be64b4d4` |
| `set_fx_preset` | — | yes | no | `14b8777c7c94` |
| `set_item_color` | — | yes | no | `1321e13dacf3` |
| `set_item_fades` | — | yes | no | `b883b5f57cde` |
| `set_media_item_properties` | — | yes | no | `ab59a9cbab33` |
| `set_media_items_properties` | — | yes | no | `e0892632e0d9` |
| `set_midi_item_properties` | — | yes | no | `a9277fcb2053` |
| `set_monitoring_fx` | — | yes | no | `1900b0fe543a` |
| `set_multiple_fx_parameters` | — | yes | no | `4f0bd4754831` |
| `set_multiple_track_properties` | — | yes | no | `441b43de959d` |
| `set_project_settings` | — | no | no | `e6a25e87048b` |
| `set_project_tempo` | — | yes | no | `ff6aaad7432b` |
| `set_record_mode` | — | no | no | `cefcc26039d1` |
| `set_render_settings` | — | no | no | `f7d044441336` |
| `set_selected_items` | — | yes | no | `962645920d83` |
| `set_selected_tracks` | — | yes | no | `96bf821eaee8` |
| `set_send` | — | yes | no | `83f7bacff96d` |
| `set_take_fx_parameter` | — | yes | no | `765a96f11f68` |
| `set_time_selection` | — | yes | no | `bc7815ea6378` |
| `set_track_folder` | — | yes | no | `68d1a648b7e9` |
| `set_track_group` | — | yes | no | `4288aa8c394a` |
| `set_track_info` | — | yes | no | `887f7e0c8288` |
| `set_track_lanes` | — | yes | no | `f0909781e1d9` |
| `set_track_property` | — | yes | no | `8acfa7516c8a` |
| `set_track_record` | — | yes | no | `6c0e9f53d5d0` |
| `setup_fx_chain` | — | yes | no | `a122ba2feba6` |
| `snapshot_delete` | — | yes | no | `4a4a39dd7500` |
| `snapshot_edit` | — | yes | no | `4577b93cb0e9` |
| `snapshot_list` | — | no | no | `6ca453a170e8` |
| `snapshot_restore` | — | yes | no | `7f17560b55e6` |
| `snapshot_save` | — | yes | no | `05b0b32bcadf` |
| `split_media_item` | — | yes | no | `07e4791a9ff7` |
| `stop` | — | no | no | `9a2e212618e2` |
| `transcribe_voice_sketch` | — | yes | no | `bc7a9b3e0855` |
| `transform_midi` | — | yes | no | `778c8bd7b02f` |
| `trim_media_item` | — | yes | no | `51ed824d092f` |
| `undo_project` | — | no | no | `d4b7b3669014` |
| `unfreeze_tracks` | — | yes | no | `25cb4348a3a5` |
| `verify_edit` | — | yes | no | `269bbfc13f28` |
| `write_jsfx` | — | yes | no | `3fab9cbdb0ee` |



## Change history

No tool-definition changes observed.
