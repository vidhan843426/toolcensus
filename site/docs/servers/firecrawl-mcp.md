# `firecrawl-mcp`

| | |
|---|---|
| Latest observed version | `3.40.0` |
| Status | ok |
| Weekly downloads | 181916 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.firecrawl/firecrawl-mcp-server |
| Surface hash | `sha256:b4d96620261e46b5` |



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 2 |
| `releases_last_90d` | 37 |
| `median_days_between_releases` | 0.33 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (28)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `alexandria_library_read` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `0b81877d006b` |
| `alexandria_library_search` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `9a11f33c2abd` |
| `firecrawl_agent` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4aedaa0fe2a1` |
| `firecrawl_agent_status` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `7ac5a1d808df` |
| `firecrawl_check_crawl_status` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `6a1b230b94bd` |
| `firecrawl_crawl` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `2d0ab3d6eb91` |
| `firecrawl_credit_usage` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `bfa91294f0c6` |
| `firecrawl_developer_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `69920f95a81b` |
| `firecrawl_find_tools` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `7f14a9a85d56` |
| `firecrawl_gov_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `863fa5d9a010` |
| `firecrawl_interact` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `14635da376cb` |
| `firecrawl_interact_stop` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `dc51b0e79e2a` |
| `firecrawl_map` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `127e48e1c7fe` |
| `firecrawl_monitor_check` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `1325f266ae02` |
| `firecrawl_monitor_checks` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `d32a8c8b2c70` |
| `firecrawl_monitor_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `356bec67bd94` |
| `firecrawl_monitor_delete` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `d7fe9d5238f6` |
| `firecrawl_monitor_get` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `466d2c4cd7ff` |
| `firecrawl_monitor_list` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `492f5707875c` |
| `firecrawl_monitor_run` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `798bcc488a61` |
| `firecrawl_monitor_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ae7fbf8a07d1` |
| `firecrawl_parse` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `7601fa4be366` |
| `firecrawl_research_inspect_paper` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `b8172dd70056` |
| `firecrawl_research_read_paper` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `a4bc3545a39c` |
| `firecrawl_research_related_papers` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `f345334ff404` |
| `firecrawl_research_search_papers` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `154819657205` |
| `firecrawl_scrape` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `bc4765675eed` |
| `firecrawl_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `f197af08eefb` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_agent` | input_schema_changed (schema_other) | property 'schema' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_agent` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_crawl` | input_schema_changed (schema_other) | property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_crawl` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_find_tools` | input_schema_changed (schema_other) | property 'level' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_interact` | input_schema_changed (schema_other) | property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_interact` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_interact_stop` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_create` | input_schema_changed (schema_other) | property 'body' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_create` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_delete` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_run` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_update` | input_schema_changed (schema_other) | property 'body' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_monitor_update` | annotations_changed |  |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_parse` | input_schema_changed (schema_other) | property 'jsonOptions' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_scrape` | input_schema_changed (schema_other) | property 'alexandria' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_search` | input_schema_changed (schema_other) | property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-45 | `3.34.1` → `3.36.0` | `firecrawl_search` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_agent` | input_schema_changed (schema_other) | property 'schema' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_crawl` | input_schema_changed (schema_other) | property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_find_tools` | input_schema_changed (schema_other) | property 'urls' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_find_tools` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_interact` | description_changed | length 456 -&gt; 751 |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_interact` | input_schema_changed (schema_other) | property 'url': format removed; property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_map` | description_changed | length 601 -&gt; 665 |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_map` | input_schema_changed (schema_widened) | property 'url': format removed |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_monitor_create` | input_schema_changed (schema_other) | property 'body' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_monitor_update` | input_schema_changed (schema_other) | property 'body' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_parse` | input_schema_changed (schema_other) | property 'jsonOptions' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_research_inspect_paper` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_research_related_papers` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_research_search_papers` | description_changed | length 466 -&gt; 483 |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_research_search_papers` | input_schema_changed (schema_widened) | property 'sort' added (optional) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_research_search_papers` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_scrape` | description_changed | length 1378 -&gt; 1447 |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_scrape` | input_schema_changed (schema_other) | property 'url': format removed; property 'alexandria' changed (annotations/descriptions) |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_scrape` | output_schema_changed |  |
| week 2026-46 | `3.36.0` → `3.38.0` | `firecrawl_search` | input_schema_changed (schema_other) | property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-47 | `3.38.0` → `3.40.0` | `alexandria_library_read` | tool_added |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `alexandria_library_search` | tool_added |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_agent` | description_changed | length 1955 -&gt; 1981 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_agent` | input_schema_changed (schema_widened) | property 'zeroDataRetention' added (optional) |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_agent` | annotations_changed |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_crawl` | description_changed | length 476 -&gt; 584 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_crawl` | input_schema_changed (schema_other) | property 'zeroDataRetention' added (optional); property 'scrapeOptions' changed (annotations/descriptions) |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_find_tools` | description_changed | length 992 -&gt; 905 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_find_tools` | output_schema_changed |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_interact` | description_changed | length 751 -&gt; 874 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_interact` | output_schema_changed |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_monitor_update` | description_changed | length 234 -&gt; 666 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_monitor_update` | input_schema_changed (schema_widened) | property 'cron' added (optional); property 'scheduleText' added (optional); property 'status' added (optional); property 'timezone' added (optional); property 'body' no longer required |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_scrape` | description_changed | length 1447 -&gt; 1414 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_scrape` | input_schema_changed (schema_other) | property 'jsonOptions' removed; property 'formats' changed (annotations/descriptions) |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_scrape` | output_schema_changed |  |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_search` | description_changed | length 2047 -&gt; 1977 |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_search` | input_schema_changed (schema_other) | property 'query' changed (annotations/descriptions) |
| week 2026-47 | `3.38.0` → `3.40.0` | `firecrawl_search` | output_schema_changed |  |


