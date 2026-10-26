# `nexus-agents`

| | |
|---|---|
| Latest observed version | `14.0.1` |
| Status | ok |
| Weekly downloads | 7164 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:c145054fdc8eebd4` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider `additionalProperties: false` on the input schema of 47 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 20 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 700 |
| `median_days_between_releases` | 0.03 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (47)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `cancel_job` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9a75b7ef888d` |
| `ci_health_check` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f160b1d8d610` |
| `compare_data_feeds` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3ea55b1c5c0a` |
| `consensus_vote` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e079a9beb94d` |
| `create_expert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c53782cedc38` |
| `delegate_to_model` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `22b6e0420f84` |
| `execute_expert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2461301785dd` |
| `execute_spec` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ad1a47142d8c` |
| `extract_symbols` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ef8ca7311df0` |
| `get_job_result` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b138d49cf887` |
| `improvement_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d6010929521c` |
| `issue_triage` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7bd6e566ea43` |
| `list_available_models` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `592933b8c817` |
| `list_experts` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `acfedc864b44` |
| `list_jobs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `d74c10010fdd` |
| `list_workflows` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `85ae4762a715` |
| `memory_query` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `de625ff373be` |
| `memory_stats` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e25b43a3cddc` |
| `memory_write` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b83171c513fa` |
| `orchestrate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `09387a0c396a` |
| `pr_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `39bee6bdfc4c` |
| `query_task_state` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `26a1c178569c` |
| `query_trace` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e395e0f0e760` |
| `registry_import` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7c08aedad912` |
| `repo_analyze` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `768f6977bcd7` |
| `repo_security_plan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `cf53083c9f6f` |
| `research_add` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `77efa4cbc40f` |
| `research_add_source` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a24bffcefe51` |
| `research_analyze` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `34336dbb8d31` |
| `research_catalog_review` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bec9483921b9` |
| `research_discover` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bd56600b614c` |
| `research_query` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `801e20af3e52` |
| `research_synthesize` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `a373e43612f4` |
| `run` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b34739100b03` |
| `run_dev_pipeline` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `c29a76541baa` |
| `run_graph_workflow` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6ef3797e6ca6` |
| `run_pipeline` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9a10ce95e364` |
| `run_quality_gate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `7d40c4982bea` |
| `run_workflow` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `aa89be60de67` |
| `search_codebase` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ced0dad272ab` |
| `search_usages` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `dbbf7835a4b3` |
| `suggest_research_tasks` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `65699676f535` |
| `supply_chain_tradeoff_panel` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `406d46b84f11` |
| `survey_oss_landscape` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0d5e7c27b90b` |
| `vendor_publishing_audit` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5898fdc1f863` |
| `verify_audit_chain` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f894e0509010` |
| `weather_report` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `cc3650a76546` |



## Change history

No tool-definition changes observed.
