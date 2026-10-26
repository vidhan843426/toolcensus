# `scryfall-mcp-server`

| | |
|---|---|
| Latest observed version | `0.1.1` |
| Status | ok |
| Weekly downloads | 29987 |
| Protocol version | 2024-11-05 |
| Registry entry | not listed |
| Surface hash | `sha256:c719a28e4a18000a` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding a `repository` field pointing at the public source repository.
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 7 of 7 tools.
    - Consider `additionalProperties: false` on the input schema of 6 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 4 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 0 |
| `median_days_between_releases` | 14.18 |
| `repo_linked` | False |
| `registry_listed` | False |



## Tools (7)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `get_card_by_id` | — | yes | no | `54a6b10914af` |
| `get_card_by_name` | — | yes | no | `7b2524a534b6` |
| `get_prices_by_id` | — | yes | no | `232675275325` |
| `get_prices_by_name` | — | yes | no | `658d1f64c3cf` |
| `get_rulings` | — | yes | no | `cfc3cab06272` |
| `random_card` | — | no | no | `dc19fd1dfe31` |
| `search_cards` | — | yes | no | `b7f1e584e15e` |



## Change history

No tool-definition changes observed.
