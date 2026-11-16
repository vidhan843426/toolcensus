# `@meshy-ai/meshy-mcp-server`

| | |
|---|---|
| Latest observed version | `0.6.11` |
| Status | ok |
| Weekly downloads | 33735 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:85130e88c7fd89be` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 4 |
| `releases_last_90d` | 14 |
| `median_days_between_releases` | 4.01 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (28)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `meshy_analyze_printability` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `779ca2397b36` |
| `meshy_animate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `6afca9995053` |
| `meshy_auto_split` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `6257f735f901` |
| `meshy_cancel_task` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `c106efc94b6a` |
| `meshy_check_balance` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `34979cfea20f` |
| `meshy_convert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8ab5b7f5d341` |
| `meshy_creative_lab` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `c954b91bca02` |
| `meshy_download_model` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `b573115f09bb` |
| `meshy_get_task_status` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `672d88f035b0` |
| `meshy_image_to_3d` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `db9c14c941e1` |
| `meshy_image_to_image` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4ca663814a66` |
| `meshy_list_animations` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `1c276742f78d` |
| `meshy_list_models` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `c974bbeb0d5d` |
| `meshy_list_tasks` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `030057d2719a` |
| `meshy_list_usage` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `9782ee2594b2` |
| `meshy_multi_image_to_3d` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `7d721b787cce` |
| `meshy_process_multicolor` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `930963cb487a` |
| `meshy_remesh` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `c7f635438ef7` |
| `meshy_repair_printability` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `7f753f5544af` |
| `meshy_resize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `eeca659a86e5` |
| `meshy_retexture` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `3bce150efd23` |
| `meshy_rig` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `4ff7c1b4decf` |
| `meshy_send_to_slicer` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `bb41bc9e1728` |
| `meshy_text_to_3d` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `5b29ff6a68f4` |
| `meshy_text_to_3d_refine` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `52e5793f0ee5` |
| `meshy_text_to_image` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `9e49ccae3b14` |
| `meshy_text_to_motion` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `0e29f59a72c4` |
| `meshy_uv_unwrap` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `2a1b8837af17` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `0.6.6` → `0.6.7` | `meshy_image_to_3d` | input_schema_changed (schema_other) | property 'model_type': enum values removed; property 'ai_model' changed (annotations/descriptions) |
| week 2026-45 | `0.6.6` → `0.6.7` | `meshy_text_to_3d` | input_schema_changed (schema_narrowed) | property 'model_type': enum values removed |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_creative_lab` | input_schema_changed (schema_other) | property 'build_options' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_image_to_3d` | description_changed | length 630 -&gt; 1451 |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_image_to_3d` | input_schema_changed (schema_other) | property 'texture_model' added (optional); property 'ai_model' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_image_to_image` | input_schema_changed (schema_other) | property 'aspect_ratio' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_multi_image_to_3d` | description_changed | length 531 -&gt; 1374 |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_multi_image_to_3d` | input_schema_changed (schema_other) | property 'texture_model' added (optional); property 'enable_pbr' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_retexture` | description_changed | length 447 -&gt; 884 |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_retexture` | input_schema_changed (schema_other) | property 'ai_model': enum values added; property 'enable_pbr' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_text_to_3d` | description_changed | length 843 -&gt; 1154 |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_text_to_3d` | input_schema_changed (schema_other) | property 'ai_model' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_text_to_3d_refine` | input_schema_changed (schema_other) | property 'texture_resolution' changed (annotations/descriptions) |
| week 2026-46 | `0.6.7` → `0.6.10` | `meshy_text_to_image` | input_schema_changed (schema_other) | property 'aspect_ratio' changed (annotations/descriptions) |
| week 2026-47 | `0.6.10` → `0.6.11` | `meshy_image_to_3d` | input_schema_changed (schema_other) | property 'texture_image_url' changed (annotations/descriptions) |
| week 2026-47 | `0.6.10` → `0.6.11` | `meshy_multi_image_to_3d` | input_schema_changed (schema_other) | property 'texture_image_url' changed (annotations/descriptions) |
| week 2026-47 | `0.6.10` → `0.6.11` | `meshy_text_to_3d_refine` | input_schema_changed (schema_other) | property 'texture_image_url' changed (annotations/descriptions) |


