# `fallow`

| | |
|---|---|
| Latest observed version | `3.43.1` |
| Status | ok |
| Weekly downloads | 2514301 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.fallow-rs/fallow |
| Surface hash | `sha256:4cdc61d58d365739` |

!!! tip "Improvement hints"
    - Consider `additionalProperties: false` on the input schema of 43 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 1 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 31 |
| `median_days_between_releases` | 0.44 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (44)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `analyze` | destructiveHint, openWorldHint, readOnlyHint | no | no | `29069aa3fbbf` |
| `audit` | openWorldHint, readOnlyHint | no | no | `899bbdb87d56` |
| `check_architecture` | openWorldHint, readOnlyHint | no | no | `1bf5de8670f0` |
| `check_changed` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b4e8aa28e6c9` |
| `check_health` | destructiveHint, openWorldHint, readOnlyHint | no | no | `5152d6790ef6` |
| `check_runtime_coverage` | openWorldHint, readOnlyHint | yes | no | `1e5f544cd9ab` |
| `code_execute` | openWorldHint, readOnlyHint | yes | no | `326cfb170420` |
| `decision_surface` | openWorldHint, readOnlyHint | no | no | `598907d4b1b7` |
| `fallow_explain` | openWorldHint, readOnlyHint | yes | no | `1751e13cd2dc` |
| `feature_flags` | openWorldHint, readOnlyHint | no | no | `c9a0ae83f518` |
| `find_dupes` | destructiveHint, openWorldHint, readOnlyHint | no | no | `f4d21ed47ff5` |
| `find_similar_code` | openWorldHint, readOnlyHint | no | no | `d12d8b9317b9` |
| `fix_apply` | destructiveHint, readOnlyHint | no | no | `a31002630802` |
| `fix_preview` | openWorldHint, readOnlyHint | no | no | `0629035c5367` |
| `get_blast_radius` | openWorldHint, readOnlyHint | yes | no | `50d27454985d` |
| `get_cleanup_candidates` | openWorldHint, readOnlyHint | yes | no | `5159a919a514` |
| `get_cloud_deployment_changes` | openWorldHint, readOnlyHint | yes | no | `36bb766bfd93` |
| `get_cloud_review_packet` | openWorldHint, readOnlyHint | yes | no | `b624ec87b488` |
| `get_cloud_runtime_context` | openWorldHint, readOnlyHint | yes | no | `8b0aa66e4c69` |
| `get_hot_paths` | openWorldHint, readOnlyHint | yes | no | `5dab183f67a3` |
| `get_importance` | openWorldHint, readOnlyHint | yes | no | `105c1224a56a` |
| `get_token_blast_radius` | idempotentHint, openWorldHint, readOnlyHint | no | no | `e115b7e94719` |
| `guard` | openWorldHint, readOnlyHint | yes | no | `9776777e3ceb` |
| `impact` | idempotentHint, openWorldHint, readOnlyHint | no | no | `d632d8250d6b` |
| `impact_all` | idempotentHint, openWorldHint, readOnlyHint | no | no | `946dcdaf90b7` |
| `impact_closure` | openWorldHint, readOnlyHint | yes | no | `4616ba9a6c63` |
| `inspect_similar_code` | openWorldHint, readOnlyHint | yes | no | `662e060dd04e` |
| `inspect_target` | openWorldHint, readOnlyHint | yes | no | `0c344b81fc9c` |
| `list_boundaries` | openWorldHint, readOnlyHint | no | no | `d7b860457fe1` |
| `list_suppressions` | openWorldHint, readOnlyHint | no | no | `c2395a4de89a` |
| `mutation_inspect` | openWorldHint, readOnlyHint | yes | no | `44da87be5b33` |
| `mutation_plan` | openWorldHint, readOnlyHint | no | no | `b6666894e128` |
| `mutation_tasks` | openWorldHint, readOnlyHint | no | no | `13461f8a31f8` |
| `project_info` | openWorldHint, readOnlyHint | no | no | `6cae61909180` |
| `recommend` | openWorldHint, readOnlyHint | no | no | `6793789389c0` |
| `security_candidates` | openWorldHint, readOnlyHint | no | no | `216f6d89e8d9` |
| `symbol_impact` | openWorldHint, readOnlyHint | yes | yes | `e25522680b49` |
| `trace_clone` | openWorldHint, readOnlyHint | no | no | `9ecf5020e250` |
| `trace_dependency` | openWorldHint, readOnlyHint | yes | no | `b0ec8660f6af` |
| `trace_error` | openWorldHint, readOnlyHint | yes | no | `0242ccee60b3` |
| `trace_export` | openWorldHint, readOnlyHint | yes | no | `090fc0eeea1f` |
| `trace_file` | openWorldHint, readOnlyHint | yes | no | `bb4f89a6134e` |
| `trace_import_path` | openWorldHint, readOnlyHint | yes | no | `a7e70a81b477` |
| `trace_symbol` | openWorldHint, readOnlyHint | yes | no | `6e63d107fd6b` |



## Change history

No tool-definition changes observed.
