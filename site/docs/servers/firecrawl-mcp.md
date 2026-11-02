# `firecrawl-mcp`

| | |
|---|---|
| Latest observed version | `3.36.0` |
| Status | ok |
| Weekly downloads | 190711 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.firecrawl/firecrawl-mcp-server |
| Surface hash | `sha256:e1b86ce196ce1f0c` |



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 2 |
| `releases_last_90d` | 39 |
| `median_days_between_releases` | 0.28 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (26)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `firecrawl_agent` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `e6289b4ccc99` |
| `firecrawl_agent_status` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `7ac5a1d808df` |
| `firecrawl_check_crawl_status` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `6a1b230b94bd` |
| `firecrawl_crawl` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `cc21c1181bad` |
| `firecrawl_credit_usage` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `bfa91294f0c6` |
| `firecrawl_developer_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `69920f95a81b` |
| `firecrawl_find_tools` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `18c1822b00fb` |
| `firecrawl_gov_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `863fa5d9a010` |
| `firecrawl_interact` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `0b4f0b82c82f` |
| `firecrawl_interact_stop` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `dc51b0e79e2a` |
| `firecrawl_map` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `ad18b3935d80` |
| `firecrawl_monitor_check` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `1325f266ae02` |
| `firecrawl_monitor_checks` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `d32a8c8b2c70` |
| `firecrawl_monitor_create` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `991882d4a865` |
| `firecrawl_monitor_delete` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `d7fe9d5238f6` |
| `firecrawl_monitor_get` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `466d2c4cd7ff` |
| `firecrawl_monitor_list` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `492f5707875c` |
| `firecrawl_monitor_run` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `798bcc488a61` |
| `firecrawl_monitor_update` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `f345b6386a8c` |
| `firecrawl_parse` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `c23b3252fccf` |
| `firecrawl_research_inspect_paper` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `92b807207c10` |
| `firecrawl_research_read_paper` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `a4bc3545a39c` |
| `firecrawl_research_related_papers` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `9e22f6c20d55` |
| `firecrawl_research_search_papers` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `22e634910f45` |
| `firecrawl_scrape` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `a0e4f7a9a4d1` |
| `firecrawl_search` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `8085194982e2` |



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


