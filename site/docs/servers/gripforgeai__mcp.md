# `@gripforgeai/mcp`

| | |
|---|---|
| Latest observed version | `0.1.164` |
| Status | ok |
| Weekly downloads | 12225 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.gripforgeai/mcp |
| Surface hash | `sha256:c79ae93cb3d9a3e5` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 75 of 288 tools.
    - Consider `additionalProperties: false` on the input schema of 210 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 141 |
| `median_days_between_releases` | 0.1 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (288)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `getAttachmentFrame` | — | yes | yes | `97f27466a67f` |
| `getWearableFrame` | — | yes | yes | `4eabd8656c87` |
| `gripforge_abilities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `228c17a9358a` |
| `gripforge_abilities_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b74850fd95eb` |
| `gripforge_ability_vfx` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `825f7ebb056b` |
| `gripforge_admin_assets` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `5cf61bbe67d8` |
| `gripforge_admin_assets_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bce3ce651399` |
| `gripforge_aim` | — | no | yes | `d03835e688e7` |
| `gripforge_animate` | — | yes | yes | `6aacb78d860a` |
| `gripforge_apply_realism` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fc58ffc372bc` |
| `gripforge_architecture_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f397b98a89fc` |
| `gripforge_armor_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d5ff4ef690b3` |
| `gripforge_armor_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2ba27792a10c` |
| `gripforge_armor_repair` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3e2602668061` |
| `gripforge_asset_clone` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8883f46bbb5c` |
| `gripforge_asset_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `850759c9375c` |
| `gripforge_attach` | — | no | yes | `b12b0d054f26` |
| `gripforge_audio_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `61aafb7c2dd7` |
| `gripforge_audio_kit` | — | no | yes | `b4068c1e91c9` |
| `gripforge_audit_game` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `cba67fd06e28` |
| `gripforge_blender_fabricate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ca40d6ef7226` |
| `gripforge_boss` | — | yes | yes | `415acaff18a8` |
| `gripforge_bot_kit` | — | yes | yes | `f547f913d2ce` |
| `gripforge_build` | — | yes | yes | `84250785f3dd` |
| `gripforge_build_deploy` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6218aae81c8b` |
| `gripforge_build_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fb7b160795fb` |
| `gripforge_build_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `05cda9ed6dcb` |
| `gripforge_build_rollback` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `986ab261b7ad` |
| `gripforge_cancel_render_preview` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1b27da5189b5` |
| `gripforge_cape` | — | no | yes | `d3d7b7bbd4b1` |
| `gripforge_central_apply` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `83192422d247` |
| `gripforge_central_server_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f32ffc5612e5` |
| `gripforge_character_concepts` | — | yes | yes | `e665bf2af10a` |
| `gripforge_collision_build` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `63cdd1843194` |
| `gripforge_collision_check` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e77e174f379a` |
| `gripforge_collision_passport` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f649ae24fb51` |
| `gripforge_complete_game` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c13b3fae0d87` |
| `gripforge_compute_assets` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `2500565f9201` |
| `gripforge_compute_download` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `75828e9f7ee0` |
| `gripforge_compute_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `25bb061594ce` |
| `gripforge_compute_job` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d758d6640352` |
| `gripforge_compute_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `4c43d3234f8d` |
| `gripforge_compute_validate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `12d80d37c115` |
| `gripforge_compute_variant` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5efa0453f94e` |
| `gripforge_concept_correct` | — | no | yes | `c66d4b5d2f6c` |
| `gripforge_configure_render_preview` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c2cc0ca9a759` |
| `gripforge_core_loop_check` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f676fca7e0d2` |
| `gripforge_creature_analyze` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `da819652356c` |
| `gripforge_creature_rig` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b5c0d8fe419f` |
| `gripforge_creature_rig_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `bbb8c1a4305a` |
| `gripforge_debug_sessions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2895d89ab41c` |
| `gripforge_debug_set` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `732da8db7fd5` |
| `gripforge_debug_snapshot` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `399744774eea` |
| `gripforge_define_game` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f57cefdf4c93` |
| `gripforge_docs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0c37917173b9` |
| `gripforge_environment_module` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9cce66658b8b` |
| `gripforge_facial_rig` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6afa7bbd3348` |
| `gripforge_flexible_chain` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2d823180eccc` |
| `gripforge_flexible_chain_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `bb6e23b764ac` |
| `gripforge_flexible_weapon_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `0298374b82cd` |
| `gripforge_font` | — | yes | yes | `408458e9989c` |
| `gripforge_formats` | — | no | no | `e00cd50f2cff` |
| `gripforge_fp_hands_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `9a4534c6105f` |
| `gripforge_fps_animation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f168c8eff7a7` |
| `gripforge_fps_kit` | — | no | yes | `498f75500cd6` |
| `gripforge_game_art_direction` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b82160902c4a` |
| `gripforge_game_asset_plan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c05fdd910888` |
| `gripforge_game_audio` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e4511ad73a72` |
| `gripforge_game_audit` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c55725a2d6f5` |
| `gripforge_game_broadcast` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `359ef5ebef69` |
| `gripforge_game_capabilities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `19e951f3cfb5` |
| `gripforge_game_concepts` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f1ffa58a11e6` |
| `gripforge_game_content` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `81e6aeabd9a0` |
| `gripforge_game_creation` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b065d9be4031` |
| `gripforge_game_engine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `577b50b7235f` |
| `gripforge_game_host_provides` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ee0e198c3ce3` |
| `gripforge_game_import` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `cc7ab005c5c1` |
| `gripforge_game_import_control` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d3a81315130f` |
| `gripforge_game_import_extract` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `63f61b444def` |
| `gripforge_game_import_normalize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `13f94bdeefdd` |
| `gripforge_game_import_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f98705fe9138` |
| `gripforge_game_import_select` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `60cfeb7e8d1e` |
| `gripforge_game_listing_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `011462912d8c` |
| `gripforge_game_mods` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0fad5d130648` |
| `gripforge_game_play_url` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7fff176caf8c` |
| `gripforge_game_project` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d465bbc42a96` |
| `gripforge_game_publish` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a2888893713e` |
| `gripforge_game_scenes` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7596a23db7ca` |
| `gripforge_game_test` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c29f598b57f9` |
| `gripforge_game_theme_from_concept` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `713fa5e0ad2e` |
| `gripforge_game_web_export` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bd482e2135ca` |
| `gripforge_game_world` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4df13ada7eef` |
| `gripforge_game_world_scope` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e4f771f5a8cb` |
| `gripforge_gamekit_anim_layers` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3dbb10b6c0fa` |
| `gripforge_gamekit_api` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `12d5967e905f` |
| `gripforge_gamekit_configure` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5282b54b6135` |
| `gripforge_gamekit_creatures` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7fb76cabb3a7` |
| `gripforge_gamekit_deliver` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ef884c8f2269` |
| `gripforge_gamekit_deliver_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9b6fd4a1dac1` |
| `gripforge_gamekit_dependencies` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `20745a9878b1` |
| `gripforge_gamekit_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ba16cd3f52d7` |
| `gripforge_gamekit_install` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `22f4fbfac543` |
| `gripforge_gamekit_installed` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7c8dabf83b21` |
| `gripforge_gamekit_remove` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3e26d8da6109` |
| `gripforge_gamekit_rollback_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `04400ed01eac` |
| `gripforge_gamekit_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c3d44cbfc568` |
| `gripforge_gamekit_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2e9e90906810` |
| `gripforge_generate_building` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e077a26c4ab3` |
| `gripforge_generate_character` | — | yes | yes | `393a4975965c` |
| `gripforge_generate_creature` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c10c7a8b0b75` |
| `gripforge_generate_district` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `95516bff23c0` |
| `gripforge_generate_flexible_weapon` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `30a4db7dd5e1` |
| `gripforge_generate_fp_hands` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c042720072c0` |
| `gripforge_generate_prop` | — | no | yes | `fa815f5d6315` |
| `gripforge_generate_vehicle` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `838644e79cce` |
| `gripforge_generate_weapon` | — | yes | yes | `d59e2b7f9f9e` |
| `gripforge_generate_weapon_catalog` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `148de74d82e2` |
| `gripforge_generation_cancel` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `51219e358295` |
| `gripforge_generation_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `118ba0abd271` |
| `gripforge_generation_quote` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `28ee5a523f7d` |
| `gripforge_generation_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `67c22503059f` |
| `gripforge_generation_retry` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `887cbd52598c` |
| `gripforge_get_completion_report` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0c5ec9ac884d` |
| `gripforge_get_render_capabilities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c1bf507b46a0` |
| `gripforge_gunfx_kit` | — | yes | yes | `5c22c179acc8` |
| `gripforge_hand_check` | — | yes | yes | `3a3206736654` |
| `gripforge_hand_rig` | — | yes | yes | `293557751863` |
| `gripforge_hitbox` | — | no | yes | `d3e32cba234e` |
| `gripforge_hud` | — | no | yes | `9000462ac79c` |
| `gripforge_hud_bar` | — | yes | yes | `34033cd59c8f` |
| `gripforge_input_kit` | — | yes | yes | `3616c8c1c1cd` |
| `gripforge_joystick_kit` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `94cd36962836` |
| `gripforge_kit` | — | yes | yes | `17ea1bd4126f` |
| `gripforge_level` | — | yes | yes | `9ac8dbf71da7` |
| `gripforge_library_get` | — | yes | yes | `7dbb62fb53c1` |
| `gripforge_library_list` | — | no | yes | `1ca27a1baa0a` |
| `gripforge_library_optimize` | — | yes | yes | `e71c98b6a8a4` |
| `gripforge_library_pull` | — | yes | yes | `3bfef3e08eef` |
| `gripforge_library_push` | — | yes | yes | `90242e397ab4` |
| `gripforge_library_tag` | — | yes | yes | `d4418f68b2f5` |
| `gripforge_light_kit` | — | yes | yes | `c4962ef480ea` |
| `gripforge_loading_page` | — | yes | yes | `440e41cbf6ff` |
| `gripforge_loadout` | — | yes | yes | `c413cbfd811b` |
| `gripforge_lod_build` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `9ca15634c091` |
| `gripforge_map_analyze` | — | yes | yes | `01c6517d16a0` |
| `gripforge_map_concept` | — | yes | yes | `c03d77adeb30` |
| `gripforge_map_decor` | — | no | yes | `173aa91ff59e` |
| `gripforge_map_export` | — | yes | yes | `754b48bc8a80` |
| `gripforge_map_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3cfaa64cb245` |
| `gripforge_map_import` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8d76c8aa5dc2` |
| `gripforge_map_import_unreal` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `128436d7526c` |
| `gripforge_map_import_unreal_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `05e3d95757b7` |
| `gripforge_map_look` | — | yes | yes | `d77c52bef1a4` |
| `gripforge_map_match` | — | yes | yes | `d49dd8d539bd` |
| `gripforge_map_paths` | — | yes | yes | `322bdc9c29a3` |
| `gripforge_map_plan` | — | yes | yes | `9fb7ca31c002` |
| `gripforge_map_props` | — | yes | yes | `51fd053af098` |
| `gripforge_map_reconstruct` | — | yes | yes | `273863c65400` |
| `gripforge_map_refs` | — | yes | yes | `ed35ca370e06` |
| `gripforge_map_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6e9fcd1a5200` |
| `gripforge_map_textures` | — | yes | yes | `3ab9bf0e83ce` |
| `gripforge_map_unreal_export_cancel_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `281b200d3b4d` |
| `gripforge_map_unreal_export_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `830215a3340e` |
| `gripforge_map_unreal_export_status_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `554e4104b97b` |
| `gripforge_map_unreal_import_cancel_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3f85cb9b8a12` |
| `gripforge_map_unreal_import_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `607e33b82898` |
| `gripforge_map_unreal_import_status_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `87a201f1d469` |
| `gripforge_map_unreal_prepare_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a6558f22d420` |
| `gripforge_map_unreal_reference_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9ad62d17fe3e` |
| `gripforge_map_unreal_upload_local` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f8a35ce1a153` |
| `gripforge_map_wires` | — | yes | yes | `0ddba6a15299` |
| `gripforge_match_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fd771681dd39` |
| `gripforge_match_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ad3d38e56d65` |
| `gripforge_match_kit` | — | yes | yes | `d4ea975123b5` |
| `gripforge_match_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6f3d1b089244` |
| `gripforge_match_stop` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d2f423523427` |
| `gripforge_menu_kit` | — | yes | yes | `fc8478bbc188` |
| `gripforge_moba_map` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `98a23683745d` |
| `gripforge_moba_roster` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `844b362832c1` |
| `gripforge_motion_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `5efa12bfaf8c` |
| `gripforge_navmesh` | — | yes | yes | `09c84abd7cfd` |
| `gripforge_net_kit` | — | yes | yes | `8160250e0638` |
| `gripforge_performance` | — | no | yes | `2481d10e75d8` |
| `gripforge_player_ban` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `64cd3f090bc7` |
| `gripforge_player_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `40ada4e8740d` |
| `gripforge_player_kick` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9a070b388425` |
| `gripforge_players_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1b016a46f22b` |
| `gripforge_prepare_vehicle` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `608de01b6ecb` |
| `gripforge_project_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `584041cbd048` |
| `gripforge_projectile_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `aff3c038ee51` |
| `gripforge_realism_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4e19b58abab6` |
| `gripforge_render` | — | yes | yes | `6d9054c63fac` |
| `gripforge_render_preview` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `46e3f1d0e0d7` |
| `gripforge_resolve_requirements` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b5a167a77ad6` |
| `gripforge_rest_pose` | — | yes | yes | `b676b9e40089` |
| `gripforge_retarget` | — | yes | yes | `dca63394f845` |
| `gripforge_reverse_detect_format` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9236b87edca4` |
| `gripforge_reverse_find_asset_system` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e5c39d6cea38` |
| `gripforge_reverse_open` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0cc50aafd6e3` |
| `gripforge_reverse_scan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2f4911a3481f` |
| `gripforge_reverse_trace_function` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5a98bd9e3867` |
| `gripforge_room_close` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `64824edfe46b` |
| `gripforge_room_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `77324ccfc917` |
| `gripforge_rooms_server_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e1252e185b11` |
| `gripforge_runtime_command` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d474c0998ab5` |
| `gripforge_runtime_receipt` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0fe10db79465` |
| `gripforge_runtime_sessions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b1ee55bb0470` |
| `gripforge_scene_asset_pin` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `147ca3fedcab` |
| `gripforge_scene_asset_promote` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e0180b6a77e8` |
| `gripforge_scene_asset_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `34287a2930cc` |
| `gripforge_scene_asset_versions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8bea1e40791d` |
| `gripforge_scene_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `64c6e3efe954` |
| `gripforge_scene_kit` | — | yes | yes | `a8fdf006fcb3` |
| `gripforge_scene_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `269581b85b1c` |
| `gripforge_scene_modify` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `05d032d48aa9` |
| `gripforge_scene_optimize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3116fb93ec3c` |
| `gripforge_scene_patch` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `97b7584a013b` |
| `gripforge_scene_promote` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0af1babe3883` |
| `gripforge_scene_proposal_apply` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `75510a3df419` |
| `gripforge_scene_proposal_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c2ef02a81021` |
| `gripforge_scene_proposals` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7759df5ea353` |
| `gripforge_scene_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ae1e8cf7863c` |
| `gripforge_scene_realism` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `904c344b86ea` |
| `gripforge_scene_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9b8ba2bc0146` |
| `gripforge_scene_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `03ff580ec729` |
| `gripforge_scene_versions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `02aeeb914cca` |
| `gripforge_scene_write` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6af13b3d6cc1` |
| `gripforge_screen_assets` | — | yes | yes | `03dbb88ee39b` |
| `gripforge_screen_background` | — | yes | yes | `bdc6ebfe6c5e` |
| `gripforge_screen_concept` | — | no | yes | `cb51cbecbf50` |
| `gripforge_screen_icons` | — | yes | yes | `9c06b14940e1` |
| `gripforge_server_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7f16c4f30a1b` |
| `gripforge_server_delete` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0505b44f40a0` |
| `gripforge_server_deploy` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fb57f68da61b` |
| `gripforge_server_events` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c1494f4c6048` |
| `gripforge_server_get` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `53cf0a8d346c` |
| `gripforge_server_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `2d6bc896d291` |
| `gripforge_server_logs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4e97be021b23` |
| `gripforge_server_metrics` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `dc0a93cfdd34` |
| `gripforge_server_restart` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4dbd220811ab` |
| `gripforge_server_scale` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `788706b118f7` |
| `gripforge_server_start` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7a16b759c5f8` |
| `gripforge_server_stop` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5067becc4cec` |
| `gripforge_shader_pull` | — | yes | yes | `d5f321a0ed35` |
| `gripforge_shaders` | — | no | yes | `0d1d78839061` |
| `gripforge_shield_export` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `286dc16e22a1` |
| `gripforge_shield_vfx` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `5bbf359b47c8` |
| `gripforge_style_kit` | — | yes | yes | `c1415aae0f51` |
| `gripforge_terrain_concepts` | — | yes | yes | `9f4ef77bdec7` |
| `gripforge_terrain_map_use` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `71d0e7d6678d` |
| `gripforge_test_game` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `15793f998889` |
| `gripforge_texture_prep` | — | no | yes | `a0fa38e87a1b` |
| `gripforge_third_party_kit_add` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `80607b3d5f79` |
| `gripforge_third_party_kit_build` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `555370ac4a6f` |
| `gripforge_third_party_kit_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `8d7ffb28afe8` |
| `gripforge_third_party_kit_remove` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ea64fd7a913c` |
| `gripforge_third_party_kit_socle` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `cfe7aba016a6` |
| `gripforge_third_party_kit_verify` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `59e78e076fce` |
| `gripforge_third_party_kit_verify_build` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b43490b7ff03` |
| `gripforge_ui_screen` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0c103e1ad60f` |
| `gripforge_urban_building` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b904e24a7936` |
| `gripforge_validate_release` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5393a7fd6069` |
| `gripforge_vehicle_doors` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `14cf8cee7925` |
| `gripforge_vehicle_finish` | — | no | yes | `0f74c8ab9624` |
| `gripforge_vehicle_orient` | — | no | yes | `72f2ad678dfb` |
| `gripforge_vehicle_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c594b8037cec` |
| `gripforge_vehicle_segment` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f3924f943047` |
| `gripforge_vehicle_wheels` | — | yes | yes | `8ea93eea3e4e` |
| `gripforge_vfx` | — | no | yes | `4c793191246a` |
| `gripforge_vfx_generate` | — | no | yes | `8e9c91753301` |
| `gripforge_vfx_preview` | — | yes | yes | `8d9229b18ec6` |
| `gripforge_vfx_project_generate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `1603a2e2903d` |
| `gripforge_vfx_project_promote` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f35930fe0266` |
| `gripforge_vfx_project_read` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6bf38fe03b10` |
| `gripforge_vfx_project_render` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `ef0346b6a3e9` |
| `gripforge_vfx_project_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e1d4f845b2bf` |
| `gripforge_vfx_project_schema` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `4809f12b9185` |
| `gripforge_vfx_project_write` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `fabce12dc061` |
| `gripforge_viewmodel_arms` | — | yes | yes | `b2ef50ca316a` |
| `gripforge_viewmodel_kit` | — | yes | yes | `01347d9f9410` |
| `gripforge_voice_profile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `04d40632f04f` |
| `gripforge_weapon_motion` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `987865804b7f` |
| `gripforge_weapon_motion_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7ef60cd98f2a` |
| `gripforge_weapon_profile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f5919383b6ff` |
| `gripforge_world_backup` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b46dfec34405` |
| `gripforge_world_deploy` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4e9270ea0993` |
| `gripforge_world_list` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `95b43fac7b20` |
| `gripforge_world_restore` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `12fcee07b131` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_collision_passport` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_core_loop_check` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_debug_sessions` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_host_provides` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_publish` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_room_close` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_room_list` | tool_added |  |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_abilities` | description_changed | length 500 -&gt; 490 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_abilities` | input_schema_changed (schema_narrowed) | property 'target': enum values removed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_aim` | description_changed | length 421 -&gt; 412 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_animate` | description_changed | length 797 -&gt; 999 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_animate` | input_schema_changed (schema_widened) | property 'actions' added (optional) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_asset_search` | input_schema_changed (schema_widened) | property 'subtype' added (optional); property 'kind': enum values added |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_attach` | description_changed | length 994 -&gt; 1213 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_attach` | input_schema_changed (schema_other) | property 'prop_grip' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_cape` | description_changed | length 193 -&gt; 177 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_compute_generate` | input_schema_changed (schema_other) | property 'description' added (optional); property 'options': maxItems changed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_define_game` | description_changed | length 608 -&gt; 865 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_define_game` | input_schema_changed (schema_widened) | property 'expected_revision': minimum removed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_docs` | description_changed | length 912 -&gt; 4115 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_docs` | input_schema_changed (schema_other) | property 'topic' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_audit` | description_changed | length 2859 -&gt; 3013 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_content` | description_changed | length 1833 -&gt; 2133 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_creation` | description_changed | length 7542 -&gt; 12427 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_creation` | input_schema_changed (schema_widened) | property 'geometry_mode' added (optional); property 'plan_document' added (optional); property 'platforms' added (optional); property 'resume_token' added (optional); property 'suggestions' added (optional); property 'action': enum values added; property 'engine': enum values added |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_engine` | description_changed | length 2439 -&gt; 2694 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_project` | description_changed | length 16172 -&gt; 16468 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_project` | input_schema_changed (schema_widened) | property 'target': enum values added |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_game_web_export` | description_changed | length 957 -&gt; 1556 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_anim_layers` | description_changed | length 1824 -&gt; 1836 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_configure` | description_changed | length 1699 -&gt; 1954 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_configure` | input_schema_changed (schema_other) | property 'patch' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_creatures` | description_changed | length 1975 -&gt; 2049 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_deliver` | description_changed | length 1650 -&gt; 2072 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_deliver_local` | input_schema_changed (schema_other) | property 'target' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_install` | description_changed | length 1578 -&gt; 1833 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_remove` | description_changed | length 1182 -&gt; 1649 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_remove` | input_schema_changed (schema_widened) | property 'host_provides' added (optional) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_search` | description_changed | length 1973 -&gt; 2436 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_gamekit_search` | input_schema_changed (schema_widened) | property 'target': enum values added |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_generate_prop` | input_schema_changed (schema_other) | property 'description' added (optional); property 'options': maxItems changed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_input_kit` | description_changed | length 343 -&gt; 320 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_input_kit` | input_schema_changed (schema_other) | property 'third_person' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_joystick_kit` | description_changed | length 605 -&gt; 549 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_joystick_kit` | input_schema_changed (schema_other) | property 'target': enum values added; property 'target': enum values removed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_light_kit` | description_changed | length 100 -&gt; 97 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_loading_page` | description_changed | length 312 -&gt; 341 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_loadout` | description_changed | length 578 -&gt; 538 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_loadout` | input_schema_changed (schema_other) | property 'sets' changed (annotations/descriptions) |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_net_kit` | description_changed | length 176 -&gt; 565 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_projectile_create` | description_changed | length 1187 -&gt; 1185 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_shader_pull` | description_changed | length 380 -&gt; 391 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_shader_pull` | input_schema_changed (schema_narrowed) | property 'engine': enum values removed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_shield_export` | description_changed | length 495 -&gt; 485 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_shield_export` | input_schema_changed (schema_narrowed) | property 'engine': enum values removed |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_third_party_kit_build` | description_changed | length 1158 -&gt; 1359 |
| week 2026-45 | `0.1.136` → `0.1.164` | `gripforge_validate_release` | description_changed | length 381 -&gt; 424 |


