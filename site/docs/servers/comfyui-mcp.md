# `comfyui-mcp`

| | |
|---|---|
| Latest observed version | `0.52.206` |
| Status | ok |
| Weekly downloads | 19173 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.artokun/comfyui-mcp |
| Surface hash | `sha256:8bf1f4cb722e090c` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 38 of 41 tools.
    - Consider `additionalProperties: false` on the input schema of 41 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 10 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 382 |
| `median_days_between_releases` | 0.04 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (41)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `apply_manifest` | — | no | no | `30883c8250ae` |
| `apps` | — | yes | no | `aed640a51689` |
| `batch` | — | yes | no | `f6bf93ce434f` |
| `bisect` | — | yes | no | `2d7588947071` |
| `calculate` | — | yes | no | `adc8ae7a4867` |
| `call_tool` | — | no | no | `fcb8b3107bd4` |
| `clear_vram` | — | no | no | `3a9f1731fbcf` |
| `comfy_cli` | — | yes | no | `d085084b7e1d` |
| `create_workflow` | — | yes | no | `4b5ba602d738` |
| `describe_tool` | — | no | no | `dc92d894996b` |
| `download_model` | destructiveHint, idempotentHint, openWorldHint | yes | no | `aeff22079210` |
| `enqueue_workflow` | — | yes | no | `024ca07aa808` |
| `generate_image` | — | yes | no | `7bc99a6505e0` |
| `get_defaults` | — | yes | no | `58bc5ff571c3` |
| `get_history` | — | yes | no | `ecca52ca87f5` |
| `get_image` | — | yes | no | `8d381b90b8f1` |
| `get_system_stats` | — | yes | no | `35aa016c7bf3` |
| `get_workflow` | — | yes | no | `53fd81b51e5f` |
| `install_comfyui` | destructiveHint, idempotentHint, openWorldHint | yes | no | `bac5d33b1270` |
| `install_custom_node` | — | yes | no | `a1981c08a7c4` |
| `kitchen` | — | yes | no | `ba8f1008c459` |
| `list_api_nodes` | — | yes | no | `5642cfd50a53` |
| `list_local_models` | — | yes | no | `ae2102a8ec8a` |
| `list_packs` | — | yes | no | `6154a5f28e79` |
| `list_tools` | — | no | no | `7f60c20e8f03` |
| `model_metadata` | — | yes | no | `2806897cb32c` |
| `node_pack` | — | yes | no | `153c48992297` |
| `node_snapshot` | — | yes | no | `904eac33bcd1` |
| `queue` | — | yes | no | `4103079910f7` |
| `report_issue` | — | yes | no | `f2184023eb59` |
| `restart_comfyui` | — | yes | no | `827d9d58b498` |
| `runpod` | destructiveHint, idempotentHint, openWorldHint | yes | no | `41019f356692` |
| `runpod_watch` | — | yes | no | `3f543ae39b1a` |
| `save_workflow` | — | yes | no | `e156c8fb7fa7` |
| `search_custom_nodes` | — | yes | no | `e666874b48b4` |
| `train_doctor` | — | yes | no | `ba61a88ff8ed` |
| `train_prepare_dataset` | — | yes | no | `2dd772c2957e` |
| `train_start` | — | yes | no | `34fd689dc3ba` |
| `upload_image` | — | yes | no | `e2f63571a45f` |
| `visualize_workflow` | — | yes | no | `dc6fb2d4b3d2` |
| `workspace` | — | yes | no | `b242ca524720` |



## Change history

No tool-definition changes observed.
