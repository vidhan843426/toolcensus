# `@brightdata/mcp`

| | |
|---|---|
| Latest observed version | `4.8.0` |
| Status | ok |
| Weekly downloads | 16905 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.brightdata/brightdata-mcp |
| Surface hash | `sha256:2ced05aebd3f4499` |



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 7 |
| `releases_last_90d` | 15 |
| `median_days_between_releases` | 3.54 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (30)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `ask_brightdata_assistant` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `a94b545c7734` |
| `chatgpt_ai_insights` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `7096dc0634ab` |
| `get_scraper_details` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `2a2aa39da3c7` |
| `get_scraper_progress` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `151780141115` |
| `get_scraper_results` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `e725331354cc` |
| `list_dataset_fields` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `2b717842fe7d` |
| `perplexity_ai_insights` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `96204e9a7d0b` |
| `refresh_scrapers` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `df6c865ed4d1` |
| `run_scraper` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `50757fa2f8ed` |
| `scrape_as_markdown` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `d3336813272b` |
| `scrape_batch` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `ab69e432184b` |
| `scraping_browser_click_ref` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `b1f757365ffc` |
| `scraping_browser_fill_form` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `f78842df8636` |
| `scraping_browser_get_html` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `98b944add1de` |
| `scraping_browser_get_text` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `4e67ec4ed3bf` |
| `scraping_browser_go_back` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `b40f98bf3597` |
| `scraping_browser_go_forward` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `2ec812f45947` |
| `scraping_browser_navigate` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `9b5fc9770109` |
| `scraping_browser_network_requests` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `d0a4872a1d77` |
| `scraping_browser_screenshot` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `65b2bf1f58c1` |
| `scraping_browser_scroll` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `ec7f0ab34047` |
| `scraping_browser_scroll_to_ref` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `234012e62003` |
| `scraping_browser_snapshot` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `d05688dcec37` |
| `scraping_browser_type_ref` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `91b789f82a21` |
| `scraping_browser_wait_for_ref` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `d0384b211788` |
| `search_dataset` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `66017b4d2786` |
| `search_engine` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `bf3c31765cce` |
| `search_engine_batch` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `1303a0a91716` |
| `search_scrapers` | destructiveHint, openWorldHint, readOnlyHint | yes | yes | `261a824a2b80` |
| `session_stats` | destructiveHint, openWorldHint, readOnlyHint | no | yes | `378dc8ebe04b` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `4.3.0` → `4.7.0` | `extract` | tool_removed |  |
| week 2026-46 | `4.3.0` → `4.7.0` | `scrape_as_html` | tool_removed |  |
| week 2026-46 | `4.3.0` → `4.7.0` | `scrape_as_markdown` | description_changed | length 465 -&gt; 492 |
| week 2026-46 | `4.3.0` → `4.7.0` | `scrape_batch` | description_changed | length 555 -&gt; 615 |
| week 2026-46 | `4.3.0` → `4.7.0` | `scraping_browser_navigate` | input_schema_changed (schema_narrowed) | property 'url': pattern added; property 'url': format added |
| week 2026-46 | `4.3.0` → `4.7.0` | `search_engine` | description_changed | length 185 -&gt; 150 |
| week 2026-46 | `4.3.0` → `4.7.0` | `search_engine` | input_schema_changed (schema_other) | property 'query': minLength added; property 'page' changed (annotations/descriptions) |
| week 2026-46 | `4.3.0` → `4.7.0` | `search_engine_batch` | description_changed | length 220 -&gt; 220 |
| week 2026-46 | `4.3.0` → `4.7.0` | `search_engine_batch` | input_schema_changed (schema_other) | property 'queries' changed (annotations/descriptions) |
| week 2026-47 | `4.7.0` → `4.8.0` | `scrape_as_markdown` | description_changed | length 492 -&gt; 636 |
| week 2026-47 | `4.7.0` → `4.8.0` | `scrape_as_markdown` | input_schema_changed (schema_widened) | property 'snapshot_id' added (optional); property 'start' added (optional) |
| week 2026-47 | `4.7.0` → `4.8.0` | `scrape_batch` | description_changed | length 615 -&gt; 827 |


