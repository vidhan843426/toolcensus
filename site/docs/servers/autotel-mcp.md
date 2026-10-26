# `autotel-mcp`

| | |
|---|---|
| Latest observed version | `0.14.2` |
| Status | ok |
| Weekly downloads | 6982 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:5a84343a2e7fce6f` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 11 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 23 |
| `median_days_between_releases` | 3.07 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (51)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `agent_usage` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `693f6e40ac21` |
| `aggregate_logs` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `68fce6a187f5` |
| `aggregate_spans` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `c49da11861a7` |
| `backend_capabilities` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `8137cd3cab5f` |
| `backend_health` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `5a4e767b62d5` |
| `check_slos` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `895c356ef80c` |
| `collector_component_readme` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `e5e685439bf9` |
| `collector_component_schema` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `47f965fb9479` |
| `collector_get_versions` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `bdeb9bff95fd` |
| `collector_list_components` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `6eaa3dd75b87` |
| `collector_refresh_catalog` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `a1e627b1dc4d` |
| `collector_validate_component_config` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8d287b29d297` |
| `correlate` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `d75c4db28aa7` |
| `discover_log_fields` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `f626f960d082` |
| `discover_services` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `9db4ac885d3a` |
| `discover_trace_fields` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `cf1ce882ff05` |
| `estimate_telemetry_cost` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `510c8ea94f94` |
| `explain_collector_config` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `7b7667b241b7` |
| `explain_instrumentation_score` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `846e8baec5e4` |
| `explain_slowdown` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ad7d2d7b7214` |
| `find_anomalies` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `3ed8fe79399b` |
| `find_errors` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `f8c64f3996eb` |
| `find_repeated_queries` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `65fb01f25516` |
| `find_root_cause` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `804d24c1b6d6` |
| `get_issue` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `74dd97c61d22` |
| `get_llm_expensive_traces` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `6d4df9b5c9d5` |
| `get_llm_model_stats` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `91af3ed69554` |
| `get_llm_slow_traces` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `b41764a0b63d` |
| `get_llm_usage` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `73993ce7e8eb` |
| `get_metric_series` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `a89b6baab84b` |
| `get_trace` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `fffb14690d13` |
| `list_capabilities` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `11e50905f3a9` |
| `list_issues` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `cbe613ac25a0` |
| `list_llm_models` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `67513a4a6055` |
| `list_llm_tools` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `9c0ae55fdcd0` |
| `list_metrics` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `bf791463a2f7` |
| `list_operations` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `51421b88da0e` |
| `list_services` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `ce894e11a8ac` |
| `score_span_instrumentation` | idempotentHint, openWorldHint, readOnlyHint | no | no | `a55401ce19b8` |
| `search_logs` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `20d67a066d86` |
| `search_spans` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `3802d4c91eb7` |
| `search_traces` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `05696e2dbe1f` |
| `semconv_get_namespace` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `11bc002515d6` |
| `semconv_list_namespaces` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `d88bfaf728b9` |
| `semconv_refresh_cache` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `050cbe6d9ef0` |
| `semconv_validate` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `c04b32014734` |
| `service_map` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `9fb7d5bb8747` |
| `suggest_collector_config` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `fcb56d010dd1` |
| `summarize_trace` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ca63cd88eae0` |
| `validate_collector_config` | idempotentHint, openWorldHint, readOnlyHint | yes | yes | `40c20ba2c2c4` |
| `what_changed` | idempotentHint, openWorldHint, readOnlyHint | no | yes | `001774ae7aef` |



## Change history

No tool-definition changes observed.
