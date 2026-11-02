# `@foldkit/devtools-mcp`

| | |
|---|---|
| Latest observed version | `0.26.0` |
| Status | ok |
| Weekly downloads | 12889 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:7521ebaaef1ea0ec` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 15 of 15 tools.
    - Consider `additionalProperties: false` on the input schema of 14 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 300 |
| `median_days_between_releases` | 0.05 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (15)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `foldkit_count_messages_by_tag` | — | no | no | `047814d22629` |
| `foldkit_diff_models` | — | yes | no | `536698471e1d` |
| `foldkit_dispatch_message` | — | yes | no | `f6e1bfa7c91f` |
| `foldkit_dispatch_messages` | — | yes | no | `e8b936a9c402` |
| `foldkit_get_init` | — | no | no | `1a2e690d1c3c` |
| `foldkit_get_message` | — | yes | no | `4c8743d4878e` |
| `foldkit_get_message_schema` | — | no | no | `12d181a7e9bf` |
| `foldkit_get_model` | — | no | no | `481cfb02cc00` |
| `foldkit_get_model_at` | — | yes | no | `d04351bd72b8` |
| `foldkit_get_runtime_state` | — | no | no | `ac110ad7560b` |
| `foldkit_list_keyframes` | — | no | no | `fd647efecf6e` |
| `foldkit_list_messages` | — | no | no | `bdf262911640` |
| `foldkit_list_runtimes` | — | no | yes | `edff7b237ff2` |
| `foldkit_replay_to_keyframe` | — | yes | no | `dd72b0497ff7` |
| `foldkit_resume` | — | no | no | `f7202333cdd8` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_count_messages_by_tag` | input_schema_changed (schema_other) | property 'since_index' changed (annotations/descriptions) |
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_diff_models` | input_schema_changed (schema_narrowed) | property 'from_index': minimum added; property 'from_index': maximum added; property 'to_index': minimum added; property 'to_index': maximum added |
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_get_message` | input_schema_changed (schema_narrowed) | property 'index': minimum added; property 'index': maximum added |
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_get_model_at` | input_schema_changed (schema_narrowed) | property 'index': minimum added; property 'index': maximum added |
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_list_messages` | input_schema_changed (schema_other) | property 'since_index' changed (annotations/descriptions) |
| week 2026-45 | `0.25.0` → `0.26.0` | `foldkit_replay_to_keyframe` | input_schema_changed (schema_narrowed) | property 'keyframe_index': minimum added; property 'keyframe_index': maximum added |


