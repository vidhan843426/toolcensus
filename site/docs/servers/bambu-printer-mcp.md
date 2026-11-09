# `bambu-printer-mcp`

| | |
|---|---|
| Latest observed version | `1.1.79` |
| Status | ok |
| Weekly downloads | 12481 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:1c05858f91fe1eaa` |

!!! tip "Improvement hints"
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 45 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 10 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 72 |
| `median_days_between_releases` | 0.12 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (63)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `bambu_connect_import_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3f9784facd5c` |
| `bambu_network_bridge_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3cf16465482b` |
| `bambu_network_call` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `58231897e53f` |
| `blender_mcp_call` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `148419483f25` |
| `blender_mcp_edit_model` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `452f3f3d53e8` |
| `blender_mcp_setup` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `8b3182889119` |
| `blender_mcp_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `761bde2271c9` |
| `camera_frame` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `8b8a46314e8a` |
| `camera_snapshot` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `98e9e6d0c7dd` |
| `camera_stream_start` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `ec84973d2566` |
| `camera_stream_stop` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `fda61b2cefa0` |
| `cancel_print` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3ac21fceb2e6` |
| `center_model` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e4090bdc9763` |
| `clear_hms_errors` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `b9cd1dc27d12` |
| `counterpart_discover_printers` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `56e5715cf2ef` |
| `counterpart_make_3mf` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `7f1faf07bb66` |
| `counterpart_print_progress` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `3a0e374a9616` |
| `counterpart_print_route` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `adf89fc9d86e` |
| `counterpart_printer_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `420fd06650dc` |
| `counterpart_propose_filaments` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `7262eab705d8` |
| `counterpart_setup_fields` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `cd5848d81f6d` |
| `delete_printer_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6b4d8d92a2bd` |
| `extend_stl_base` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `06fb024be928` |
| `fusion_mcp_call` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `10e01b3a727b` |
| `fusion_mcp_export` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `d97b076c8179` |
| `fusion_mcp_new_design` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `9ca462dd976a` |
| `fusion_mcp_setup` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `1fc8d17b4514` |
| `fusion_mcp_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `6ab079259479` |
| `get_printer_filaments` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `86f7c9402f7d` |
| `get_printer_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `2107e9db73d2` |
| `get_slice_settings` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d7b55695d69c` |
| `get_stl_info` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f8e3141b7949` |
| `inspect_print_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8423cf5d28de` |
| `lay_flat` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ea14a03d0052` |
| `list_3mf_plate_objects` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `affbae023c0b` |
| `list_3mf_plates` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4bcd5d1b8f2e` |
| `list_printer_files` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7a9197a1b802` |
| `list_templates` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `65acd86fd29c` |
| `merge_vertices` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `625e7437bc9f` |
| `pause_print` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `af4c297c5abf` |
| `print_3mf` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `72850cdf137f` |
| `print_3mf_bambu_network` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7aaae52604b7` |
| `print_collar_charm` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `44494883c928` |
| `reread_ams_rfid` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `281d4a341f50` |
| `resolve_3mf_ams_slots` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `116942c52746` |
| `resume_print` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `ea94eb0abe84` |
| `rotate_stl` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `912e3ea42dd3` |
| `save_template` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e234f7c22abb` |
| `scale_stl` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2b8f7bd7f374` |
| `set_airduct_mode` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `852468cfb4e2` |
| `set_ams_drying` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1f3fa44109fb` |
| `set_fan_speed` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e4e124eeb3a3` |
| `set_light` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `076f767295e4` |
| `set_print_speed` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `34412c6a2bfd` |
| `set_temperature` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6e9a4d34fb78` |
| `skip_objects` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e7033aa35652` |
| `slice_stl` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ca71cd074fb3` |
| `slice_with_template` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `cf8162375c2d` |
| `start_print` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7156f34f1a2b` |
| `start_print_job` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bcbcbf31ba32` |
| `upload_file` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c2fe0e35db8d` |
| `upload_gcode` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f752d9f58292` |
| `x2d_native_control` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `75903392e109` |



## Change history

No tool-definition changes observed.
