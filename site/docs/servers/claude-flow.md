# `claude-flow`

| | |
|---|---|
| Latest observed version | `3.63.4` |
| Status | ok |
| Weekly downloads | 20292 |
| Protocol version | 2024-11-05 |
| Registry entry | io.github.ruvnet/claude-flow |
| Surface hash | `sha256:ad410f43d48a6f10` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 379 of 379 tools.
    - Consider `additionalProperties: false` on the input schema of 343 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 26 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 117 |
| `median_days_between_releases` | 0.03 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (379)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `agent_execute` | — | yes | no | `f1fffd296a18` |
| `agent_health` | — | no | no | `00c4c48daf4b` |
| `agent_list` | — | no | no | `54be2096a648` |
| `agent_logs` | — | yes | no | `e5157232a266` |
| `agent_pool` | — | yes | no | `304c34e0fe1d` |
| `agent_spawn` | — | yes | no | `b152813bfd53` |
| `agent_status` | — | yes | no | `cb7dab715c67` |
| `agent_terminate` | — | yes | no | `c578667c7cef` |
| `agent_update` | — | yes | no | `e6d2e98ad4ad` |
| `agentdb_batch` | — | yes | no | `569f06c4778f` |
| `agentdb_causal-edge` | — | yes | no | `4c0625fde991` |
| `agentdb_causal-edge-delete` | — | yes | no | `b36a6efac220` |
| `agentdb_causal-node-delete` | — | yes | no | `a27d12f64ba7` |
| `agentdb_consolidate` | — | no | no | `0c23943625b3` |
| `agentdb_context-synthesize` | — | yes | no | `47052287acf1` |
| `agentdb_controllers` | — | no | no | `c158217c9fca` |
| `agentdb_feedback` | — | yes | no | `76b4e7914893` |
| `agentdb_graph-pathfinder` | — | yes | no | `900340fe42d4` |
| `agentdb_graph-query` | — | yes | no | `b87ec47f43e4` |
| `agentdb_health` | — | no | no | `81cdf03e1395` |
| `agentdb_hierarchical-delete` | — | yes | no | `09b1846e7631` |
| `agentdb_hierarchical-recall` | — | yes | no | `130096faba5d` |
| `agentdb_hierarchical-store` | — | yes | no | `af02fe8d55b7` |
| `agentdb_pattern-search` | — | yes | no | `b1f3f9967ad6` |
| `agentdb_pattern-store` | — | yes | no | `cf491d919923` |
| `agentdb_route` | — | yes | no | `6e25e177be1a` |
| `agentdb_semantic-route` | — | yes | no | `c312519a9834` |
| `agentdb_session-end` | — | yes | no | `0539bf836afc` |
| `agentdb_session-start` | — | yes | no | `482175d27b83` |
| `agenticow_branch` | — | yes | no | `7753636810e1` |
| `agenticow_checkpoint` | — | yes | no | `238ba2de57f7` |
| `agenticow_diff` | — | yes | no | `e4bb6a823e49` |
| `agenticow_ingest` | — | yes | no | `5a0948ac16f4` |
| `agenticow_lineage` | — | yes | no | `b98093f87072` |
| `agenticow_promote` | — | yes | no | `bc6c951dc4f6` |
| `agenticow_query` | — | yes | no | `baa8fdab694d` |
| `agenticow_rollback` | — | yes | no | `17ad5f6f15ca` |
| `agenticow_speculate` | — | yes | no | `9c1387c9435e` |
| `agenticow_status` | — | yes | no | `828799499e3f` |
| `aidefence_analyze` | — | yes | no | `741df50768c6` |
| `aidefence_has_pii` | — | yes | no | `9d76933328bd` |
| `aidefence_is_safe` | — | yes | no | `2eef16ae1839` |
| `aidefence_learn` | — | yes | no | `4aec06c4e667` |
| `aidefence_scan` | — | yes | no | `5a4ba7e3acc5` |
| `aidefence_stats` | — | no | no | `421e0ad68d0b` |
| `analyze_diff` | — | no | no | `902251670477` |
| `analyze_diff-classify` | — | no | no | `a8e7f41563e6` |
| `analyze_diff-reviewers` | — | no | no | `9217279e40fb` |
| `analyze_diff-risk` | — | no | no | `34fe190320c9` |
| `analyze_diff-stats` | — | no | no | `4662491322a6` |
| `analyze_file-risk` | — | yes | no | `f8473c1ff9c9` |
| `autopilot_config` | — | no | no | `8d21591030bf` |
| `autopilot_disable` | — | no | no | `1df1f4cd1f5d` |
| `autopilot_enable` | — | no | no | `c8ceaed52666` |
| `autopilot_history` | — | yes | no | `bb9f859fff7d` |
| `autopilot_learn` | — | no | no | `a505a674b283` |
| `autopilot_log` | — | no | no | `7d65ff0a4002` |
| `autopilot_predict` | — | no | no | `f4088b10347c` |
| `autopilot_progress` | — | no | no | `f6de25f0475c` |
| `autopilot_reset` | — | no | no | `1bd1813408b3` |
| `autopilot_status` | — | no | no | `db7b78224ff7` |
| `browser_act` | — | yes | no | `2ddaacefcfe2` |
| `browser_cookie_use` | — | yes | no | `7407d86a9fc3` |
| `browser_session_end` | — | yes | no | `d3aaa69f677b` |
| `browser_session_record` | — | yes | no | `8d1b21a00000` |
| `browser_session_replay` | — | yes | no | `dfb992fe1f4d` |
| `browser_template_apply` | — | yes | no | `810cd288c762` |
| `business_pod_route_backend` | — | no | no | `0005f96ed9a4` |
| `business_pod_validate` | — | yes | no | `5471305b481a` |
| `claims_accept-handoff` | — | yes | no | `372bd163645e` |
| `claims_board` | — | no | no | `6675adffa5c8` |
| `claims_claim` | — | yes | no | `890ddf0e1981` |
| `claims_handoff` | — | yes | no | `44d232ea0fd4` |
| `claims_list` | — | no | no | `a7ea1695cc5b` |
| `claims_load` | — | no | no | `cf8c5e349494` |
| `claims_mark-stealable` | — | yes | no | `b02a49b4055a` |
| `claims_rebalance` | — | no | no | `e8dd085bfcb7` |
| `claims_release` | — | yes | no | `a01ae52621e1` |
| `claims_status` | — | yes | no | `f4dac8abf0c8` |
| `claims_steal` | — | yes | no | `88d2e10a4f8d` |
| `claims_stealable` | — | no | no | `cc504e0ac0db` |
| `config_export` | — | no | no | `c3809659e60e` |
| `config_get` | — | yes | no | `eccac0b977ff` |
| `config_import` | — | yes | no | `42a03c327d7d` |
| `config_list` | — | no | no | `4dc5b75c95e4` |
| `config_reset` | — | no | no | `4c35583bf4d2` |
| `config_set` | — | yes | no | `b9202a023835` |
| `coordination_consensus` | — | no | no | `2c721f5231a0` |
| `coordination_load_balance` | — | no | no | `a95d3fc422da` |
| `coordination_metrics` | — | no | no | `56864e94ab52` |
| `coordination_node` | — | no | no | `f2310588d344` |
| `coordination_orchestrate` | — | yes | no | `ed8926aceb9b` |
| `coordination_sync` | — | no | no | `bf1acdb2dff5` |
| `coordination_topology` | — | no | no | `da4b4ef8d6fb` |
| `daa_agent_adapt` | — | yes | no | `8cd18975ca54` |
| `daa_agent_create` | — | yes | no | `bda12db1a0cf` |
| `daa_cognitive_pattern` | — | no | no | `96b56795e704` |
| `daa_knowledge_share` | — | yes | no | `79ae99c29537` |
| `daa_learning_status` | — | no | no | `9c33d9122c0e` |
| `daa_performance_metrics` | — | no | no | `694a14515a88` |
| `daa_workflow_create` | — | yes | no | `c5bdf4356190` |
| `daa_workflow_execute` | — | yes | no | `d5984b1c1864` |
| `embeddings_compare` | — | yes | no | `1ac9bab32aee` |
| `embeddings_generate` | — | yes | no | `013078017615` |
| `embeddings_hyperbolic` | — | no | no | `8290026b3e28` |
| `embeddings_init` | — | no | no | `9abebff47001` |
| `embeddings_neural` | — | no | no | `42ed8174ee54` |
| `embeddings_rabitq_build` | — | no | no | `017697158c0e` |
| `embeddings_rabitq_search` | — | yes | no | `6e0dd883c1d9` |
| `embeddings_rabitq_status` | — | no | no | `e166d937b412` |
| `embeddings_search` | — | yes | no | `4b1da4d8113a` |
| `embeddings_status` | — | no | no | `27588a6b1224` |
| `federation_bbs_human_join` | — | yes | no | `d82b9fb1894d` |
| `federation_bbs_identity` | — | no | no | `b748bea2bb76` |
| `federation_bbs_peer_add` | — | yes | no | `7369ad1e91a7` |
| `federation_bbs_peers` | — | no | no | `d14529927179` |
| `federation_bbs_publish` | — | yes | no | `9cf3a9f52da0` |
| `federation_bbs_register` | — | yes | no | `3e4f7c327470` |
| `federation_bbs_serve` | — | no | no | `7e0dfa10f204` |
| `federation_bbs_sync` | — | yes | no | `25843a5d1741` |
| `federation_bbs_watch` | — | yes | no | `8e3f05b67641` |
| `github_issue_track` | — | no | no | `8ae0c63716a5` |
| `github_metrics` | — | no | no | `ff192126b23a` |
| `github_pr_manage` | — | no | no | `006a42fc5eec` |
| `github_repo_analyze` | — | no | no | `81e2b26ec23d` |
| `github_workflow` | — | no | no | `bbf8236fa566` |
| `guidance_brain` | — | no | no | `d953228ba550` |
| `guidance_capabilities` | — | no | no | `e85c01648c5b` |
| `guidance_discover` | — | no | no | `3268204287b0` |
| `guidance_quickref` | — | yes | no | `5197fb4b48c5` |
| `guidance_recommend` | — | yes | no | `ebfbe4b20824` |
| `guidance_workflow` | — | yes | no | `ff95f9979b2c` |
| `hive-mind_broadcast` | — | yes | no | `4456ffdcb850` |
| `hive-mind_consensus` | — | yes | no | `91d5919413e6` |
| `hive-mind_init` | — | no | no | `1ce130bd230c` |
| `hive-mind_join` | — | yes | no | `e90264d87e08` |
| `hive-mind_leave` | — | yes | no | `e8113c869396` |
| `hive-mind_memory` | — | yes | no | `22748b9aaac2` |
| `hive-mind_optimize-memory` | — | no | no | `200a952fcd0e` |
| `hive-mind_shutdown` | — | no | no | `f1939d60c06e` |
| `hive-mind_spawn` | — | no | no | `f72eba2cdf21` |
| `hive-mind_status` | — | no | no | `4507c4738604` |
| `hooks_build-agents` | — | no | no | `f0056541a033` |
| `hooks_codemod` | — | yes | no | `5109a05657e5` |
| `hooks_coverage-gaps` | — | no | no | `62071f548e45` |
| `hooks_coverage-route` | — | yes | no | `b44f02b5f0f6` |
| `hooks_coverage-suggest` | — | yes | no | `064b26ed442d` |
| `hooks_explain` | — | yes | no | `e35f837a1444` |
| `hooks_init` | — | no | no | `a763c1dbc699` |
| `hooks_intelligence` | — | no | no | `8a771e64135c` |
| `hooks_intelligence-reset` | — | no | no | `8ad7e2fcc074` |
| `hooks_intelligence_attention` | — | yes | no | `3d4e65b145e8` |
| `hooks_intelligence_learn` | — | no | no | `f7248794d3e1` |
| `hooks_intelligence_pattern-search` | — | yes | no | `3d81cf176add` |
| `hooks_intelligence_pattern-store` | — | yes | no | `a900ae596860` |
| `hooks_intelligence_stats` | — | no | no | `ec8fadf19dc2` |
| `hooks_intelligence_trajectory-end` | — | yes | no | `f89de72f92d8` |
| `hooks_intelligence_trajectory-start` | — | yes | no | `a5f23a458cfb` |
| `hooks_intelligence_trajectory-step` | — | yes | no | `735fd6a40ced` |
| `hooks_intelligence_unified-stats` | — | no | no | `acef04127418` |
| `hooks_list` | — | no | no | `0cf73f1fbecc` |
| `hooks_metrics` | — | no | no | `aae1dff4139c` |
| `hooks_model-outcome` | — | yes | no | `1c7fc8e5bca5` |
| `hooks_model-route` | — | yes | no | `33ec8c0306e1` |
| `hooks_model-stats` | — | no | no | `223687c37610` |
| `hooks_model-verify` | — | yes | no | `12962fa88277` |
| `hooks_notify` | — | yes | no | `bfefecff0a62` |
| `hooks_post-command` | — | yes | no | `af3a30c12bc5` |
| `hooks_post-edit` | — | yes | no | `390acf59f019` |
| `hooks_post-task` | — | yes | no | `65061b2826d9` |
| `hooks_pre-command` | — | yes | no | `9112fca1377f` |
| `hooks_pre-edit` | — | yes | no | `44b38b06be8f` |
| `hooks_pre-task` | — | yes | no | `b7f975fd9140` |
| `hooks_pretrain` | — | no | no | `90a8a0fedb4f` |
| `hooks_route` | — | yes | no | `ac47b418d406` |
| `hooks_session-end` | — | no | no | `bb9070ed9ff4` |
| `hooks_session-restore` | — | no | no | `198bbc7298ac` |
| `hooks_session-start` | — | no | no | `c9a09af7ddb9` |
| `hooks_task-completed` | — | yes | no | `7f3b919f50cd` |
| `hooks_teammate-idle` | — | no | no | `2fdf4b9479fe` |
| `hooks_transfer` | — | yes | no | `da29d22d7132` |
| `hooks_worker-cancel` | — | yes | no | `f697afdcdc6c` |
| `hooks_worker-detect` | — | yes | no | `e91d3ca66dae` |
| `hooks_worker-dispatch` | — | yes | no | `23278aa03aa8` |
| `hooks_worker-list` | — | no | no | `38ff8e8bb786` |
| `hooks_worker-status` | — | no | no | `946053e858fd` |
| `http_fetch` | — | yes | no | `49dda0fc62af` |
| `managed_agent_capabilities` | — | no | no | `b65b7fca70df` |
| `managed_agent_control` | — | yes | no | `f81edce14b0c` |
| `managed_agent_create` | — | no | no | `0381eca2e91c` |
| `managed_agent_events` | — | yes | no | `a75bd622c878` |
| `managed_agent_interrupt` | — | yes | no | `ca8e4097adea` |
| `managed_agent_learning` | — | yes | no | `15b8a3d60b0a` |
| `managed_agent_list` | — | no | no | `44cd2048389f` |
| `managed_agent_prompt` | — | yes | no | `4b6e07b134da` |
| `managed_agent_status` | — | yes | no | `3d79f31f02d4` |
| `managed_agent_terminate` | — | yes | no | `c068c4907159` |
| `mcp_start` | — | no | no | `0a1db2ba7b68` |
| `mcp_status` | — | no | no | `ff5860ec510e` |
| `mcp_stop` | — | no | no | `6c127e3e7a08` |
| `memory_bridge_status` | — | no | no | `982430194597` |
| `memory_cleanup` | — | no | no | `45f23983e634` |
| `memory_compress` | — | no | no | `92e3977e5e11` |
| `memory_delete` | — | yes | no | `399c35edc064` |
| `memory_detailed-stats` | — | no | no | `dcfab0f25b1e` |
| `memory_export` | — | yes | no | `eab3cf257934` |
| `memory_import` | — | yes | no | `818aa836971d` |
| `memory_import_claude` | — | no | no | `c092bb108c8b` |
| `memory_list` | — | no | no | `b133e45ca277` |
| `memory_migrate` | — | no | no | `da88cd110c85` |
| `memory_retrieve` | — | yes | no | `6c437db863a7` |
| `memory_search` | — | yes | no | `e1d0ccedfaa0` |
| `memory_search_unified` | — | yes | no | `47974d9d07dd` |
| `memory_stats` | — | no | no | `4870fa95fc5b` |
| `memory_store` | — | yes | no | `9044cc1dd028` |
| `metaharness_audit_list` | — | no | no | `5eba7264711a` |
| `metaharness_audit_trend` | — | no | no | `877dbcb4f2da` |
| `metaharness_bench` | — | yes | no | `9dcf33321f6a` |
| `metaharness_drift_from_history` | — | no | no | `c8c2f43be5d1` |
| `metaharness_evolve` | — | no | no | `7ca8bef0e2a5` |
| `metaharness_flywheel` | — | yes | no | `9f8d2c6e9b80` |
| `metaharness_genome` | — | no | no | `b6f436211641` |
| `metaharness_gepa` | — | yes | no | `ce45f09ce26c` |
| `metaharness_learn` | — | no | no | `a7406ba552dc` |
| `metaharness_mcp_scan` | — | no | no | `347d289f4417` |
| `metaharness_oia_audit` | — | no | no | `00d217df77a7` |
| `metaharness_redblue` | — | no | no | `d2d9b783d5f7` |
| `metaharness_score` | — | no | no | `0121545fe93d` |
| `metaharness_security_bench` | — | no | no | `e32bfa68c10a` |
| `metaharness_similarity` | — | no | no | `4a0eb3e0ae67` |
| `metaharness_threat_model` | — | no | no | `bc38e6052b96` |
| `mission_create` | — | yes | no | `0707379778cc` |
| `mission_events` | — | yes | no | `c4f5b5a8631a` |
| `mission_get` | — | no | no | `a76faa04c1a6` |
| `mission_plan` | — | yes | no | `c24fd30bbff4` |
| `mission_request_action` | — | yes | no | `4560be6d595a` |
| `neural_compress` | — | no | no | `363754b0af19` |
| `neural_optimize` | — | no | no | `3774a039edf4` |
| `neural_patterns` | — | no | no | `452ca6aaf6b4` |
| `neural_predict` | — | yes | no | `a3827ab8c88b` |
| `neural_status` | — | no | no | `483e677c9ad0` |
| `neural_train` | — | yes | no | `eaff8aa9c480` |
| `performance_benchmark` | — | no | no | `b768278dbe73` |
| `performance_bottleneck` | — | no | no | `88c7022c1966` |
| `performance_metrics` | — | no | no | `326638794609` |
| `performance_optimize` | — | no | no | `dae3ec52ff5e` |
| `performance_profile` | — | no | no | `63edefd19268` |
| `performance_report` | — | no | no | `08d6e9036900` |
| `policy_evaluate` | — | yes | no | `73b4732410f8` |
| `policy_status` | — | no | no | `ccbf76606008` |
| `progress_check` | — | no | no | `d3c4de10a552` |
| `progress_summary` | — | no | no | `5ef1fefd54ef` |
| `progress_sync` | — | no | no | `e61f0c0c22e0` |
| `progress_watch` | — | no | no | `429a8d8d8661` |
| `rure_analyze_binary` | — | yes | no | `5b69a0e91be0` |
| `rure_analyze_cuda` | — | yes | no | `bd3450a94ed6` |
| `rure_analyze_dotnet` | — | yes | no | `f11c29c035b7` |
| `rure_analyze_evm` | — | no | no | `8c1090893b40` |
| `rure_analyze_js_app` | — | yes | no | `98c3c1a9653c` |
| `rure_cuda_launch_plan` | — | yes | no | `e512bcd9a6af` |
| `rure_extract_asar` | — | yes | no | `d95ec5249225` |
| `rure_find_feature` | — | yes | no | `cf4f709c6277` |
| `ruvllm_chat_format` | — | yes | no | `115f76dcf8cb` |
| `ruvllm_generate_config` | — | no | no | `88eb8d43cb0f` |
| `ruvllm_hnsw_add` | — | yes | no | `5a021efa6f6c` |
| `ruvllm_hnsw_create` | — | yes | no | `0138520abfeb` |
| `ruvllm_hnsw_route` | — | yes | no | `df95d9368d51` |
| `ruvllm_microlora_adapt` | — | yes | no | `de8196e9653d` |
| `ruvllm_microlora_create` | — | yes | no | `6a9e0639c271` |
| `ruvllm_sona_adapt` | — | yes | no | `527985bf0ae7` |
| `ruvllm_sona_create` | — | no | no | `16c2e9a45b90` |
| `ruvllm_status` | — | no | no | `be399f28508f` |
| `seraphina_guidance` | — | yes | no | `6e462542a31d` |
| `session_current` | — | no | no | `cf716f6762f9` |
| `session_delete` | — | yes | no | `221755eac4e7` |
| `session_export` | — | yes | no | `eeaf67a8bfeb` |
| `session_import` | — | no | no | `1e701314d5a1` |
| `session_info` | — | yes | no | `29db23a8c49a` |
| `session_list` | — | no | no | `bf7c0ccd1723` |
| `session_restore` | — | no | no | `5a7fdd2d0b2e` |
| `session_save` | — | yes | no | `35a720bebbc1` |
| `swarm_health` | — | no | no | `d7af71b365fe` |
| `swarm_init` | — | no | no | `dcde976d408b` |
| `swarm_pheromone_status` | — | no | no | `38d208f89fcd` |
| `swarm_pheromone_update` | — | yes | no | `0a2035280a8e` |
| `swarm_shutdown` | — | no | no | `f15e3f36b763` |
| `swarm_status` | — | no | no | `9fdf3fd5f643` |
| `system_health` | — | no | no | `4c66b8cc050a` |
| `system_info` | — | no | no | `d700cd5cf7b1` |
| `system_metrics` | — | no | no | `2d3663171bd9` |
| `system_reset` | — | yes | no | `5409d5dcceb9` |
| `system_status` | — | no | no | `a3ee44c8a33a` |
| `task_assign` | — | yes | no | `d00203fefc2d` |
| `task_cancel` | — | yes | no | `4d72d6383389` |
| `task_complete` | — | yes | no | `497cc63a367a` |
| `task_create` | — | yes | no | `2a38bd624bfe` |
| `task_list` | — | no | no | `535d9d23791c` |
| `task_retry` | — | yes | no | `b4fcac2e7dff` |
| `task_status` | — | yes | no | `530d03f8773c` |
| `task_summary` | — | no | no | `2016f5221b30` |
| `task_update` | — | yes | no | `95ecb3275ade` |
| `team_broadcast` | — | yes | no | `ea3ad0b0027c` |
| `team_create` | — | yes | no | `4ae1b3849ea2` |
| `team_inbox` | — | yes | no | `8eae8ef81147` |
| `team_on_stop` | — | yes | no | `047291113dbc` |
| `team_plan` | — | yes | no | `4f529ab692c4` |
| `team_send` | — | yes | no | `6465d3ba6183` |
| `team_shutdown` | — | yes | no | `e80f4e0fa0a9` |
| `team_spawn` | — | yes | no | `98d90f0aae0e` |
| `team_status` | — | yes | no | `6a8f6b745c9a` |
| `terminal_close` | — | yes | no | `7d834984919b` |
| `terminal_create` | — | no | no | `d5733fe10a08` |
| `terminal_execute` | — | yes | no | `9bf66dbfac38` |
| `terminal_history` | — | no | no | `902561591bb1` |
| `terminal_list` | — | no | no | `dbcc2238f923` |
| `transfer_detect-pii` | — | yes | no | `489950ae8264` |
| `transfer_ipfs-resolve` | — | yes | no | `078bc92df16f` |
| `transfer_plugin-featured` | — | no | no | `6b7a006cac32` |
| `transfer_plugin-info` | — | yes | no | `1b5635eb2b9d` |
| `transfer_plugin-official` | — | no | no | `65f2b4b03116` |
| `transfer_plugin-search` | — | no | no | `79525c08d773` |
| `transfer_store-download` | — | yes | no | `a781fd09d76d` |
| `transfer_store-featured` | — | no | no | `063335f1d4d8` |
| `transfer_store-info` | — | yes | no | `0b2ad0a5ba60` |
| `transfer_store-search` | — | no | no | `b615653a3c09` |
| `transfer_store-trending` | — | no | no | `dd2ce7cda8bf` |
| `wasm_agent_compose` | — | no | no | `8efdd6b4a28a` |
| `wasm_agent_create` | — | no | no | `4a67e5309f6b` |
| `wasm_agent_export` | — | yes | no | `3c1907a01fd3` |
| `wasm_agent_files` | — | yes | no | `4191aea4c8b7` |
| `wasm_agent_is_stopped` | — | yes | no | `7f62210e030e` |
| `wasm_agent_list` | — | no | no | `1346917b31d0` |
| `wasm_agent_prompt` | — | yes | no | `839cd9e8de53` |
| `wasm_agent_reset` | — | yes | no | `efb967e04910` |
| `wasm_agent_state` | — | yes | no | `c0bd0ede92c2` |
| `wasm_agent_terminate` | — | yes | no | `35c084c6663d` |
| `wasm_agent_todos` | — | yes | no | `e67a41bbd693` |
| `wasm_agent_tool` | — | yes | no | `9d3253e14e71` |
| `wasm_agent_tools` | — | yes | no | `a3baac2fcbe8` |
| `wasm_agent_turn_count` | — | yes | no | `13d8055444ad` |
| `wasm_gallery_active` | — | no | no | `eb8a01e24bbd` |
| `wasm_gallery_add_custom` | — | yes | no | `6ccc9ae744d7` |
| `wasm_gallery_categories` | — | no | no | `9d6b5f5510c4` |
| `wasm_gallery_config` | — | no | no | `84d37c7996eb` |
| `wasm_gallery_configure` | — | yes | no | `0626fc72809a` |
| `wasm_gallery_create` | — | yes | no | `c96b6fb89da2` |
| `wasm_gallery_export` | — | no | no | `2eeac683d914` |
| `wasm_gallery_import` | — | yes | no | `e8978a92bd1c` |
| `wasm_gallery_list` | — | no | no | `812b3f0ae987` |
| `wasm_gallery_list_by_category` | — | yes | no | `0acfc8b42a92` |
| `wasm_gallery_load_rvf` | — | yes | no | `e023c9012833` |
| `wasm_gallery_remove_custom` | — | yes | no | `b246d0f5c977` |
| `wasm_gallery_search` | — | yes | no | `6f8985424421` |
| `workflow_cancel` | — | yes | no | `84a3dab8c29f` |
| `workflow_create` | — | yes | no | `5c9cafd7a4e1` |
| `workflow_delete` | — | yes | no | `bd7ac0d96402` |
| `workflow_execute` | — | yes | no | `f495fab813ed` |
| `workflow_list` | — | no | no | `56df36ddd336` |
| `workflow_pause` | — | yes | no | `ae31386f0839` |
| `workflow_resume` | — | yes | no | `a05859743cff` |
| `workflow_run` | — | no | no | `9f3e6a7ded4e` |
| `workflow_status` | — | yes | no | `af5c30643b2e` |
| `workflow_stop` | — | yes | no | `642026d053de` |
| `workflow_template` | — | yes | no | `c8dac2efa11b` |
| `workflow_validate` | — | yes | no | `ef34634b3a83` |
| `x_federation_admit` | — | yes | no | `047fd7a64dca` |
| `x_federation_channel_accept` | — | no | no | `9716daf06d64` |
| `x_federation_channel_create` | — | yes | no | `1daafd34d32b` |
| `x_federation_channel_grant` | — | yes | no | `12f6cd7a4b89` |
| `x_federation_channel_list` | — | no | no | `8d68969a53ca` |
| `x_federation_channel_publish` | — | yes | no | `e9bbfc4fb427` |
| `x_federation_channel_read` | — | yes | no | `d3d08c193471` |
| `x_federation_claims` | — | no | no | `4e87535ab776` |
| `x_federation_invite_mint` | — | no | no | `800e5724f7ff` |
| `x_federation_join` | — | no | no | `c3239e82bd8e` |
| `x_federation_publish` | — | yes | no | `e934951d0344` |
| `x_federation_registry` | — | no | no | `7b666a13abd5` |
| `x_federation_roster` | — | no | no | `4809450732bc` |
| `x_federation_sync` | — | no | no | `82083aed2bb6` |



## Change history

No tool-definition changes observed.
