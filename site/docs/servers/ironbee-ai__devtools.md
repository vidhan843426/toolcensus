# `@ironbee-ai/devtools`

| | |
|---|---|
| Latest observed version | `0.52.0` |
| Status | ok |
| Weekly downloads | 11465 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:8345ae403a4c3bed` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 58 of 58 tools.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 33 |
| `maintainer_count` | 3 |
| `releases_last_90d` | 42 |
| `median_days_between_releases` | 1.15 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (58)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `a11y_take-aria-snapshot` | — | no | yes | `9f4c6009c8d8` |
| `a11y_take-ax-tree-snapshot` | — | no | yes | `0119448ebf5c` |
| `content_get-as-html` | — | no | yes | `a6c9154eabbf` |
| `content_get-as-text` | — | no | yes | `46c7007b391e` |
| `content_save-as-pdf` | — | no | yes | `f1b6b82972ef` |
| `content_start-recording` | — | no | yes | `04c77d594aa1` |
| `content_stop-recording` | — | no | no | `b15d38426021` |
| `content_take-screenshot` | — | no | yes | `158c39102bbf` |
| `debug_add-watch` | — | yes | yes | `af7bcdf5aa64` |
| `debug_clear-probe-snapshots` | — | no | yes | `851785f90926` |
| `debug_clear-probes` | — | no | yes | `1dee8a5671a8` |
| `debug_get-probe-snapshots` | — | no | yes | `713bd6f027c4` |
| `debug_list-probes` | — | no | yes | `e3091f4e83b7` |
| `debug_put-exceptionpoint` | — | yes | yes | `2a430fce1fbc` |
| `debug_put-logpoint` | — | yes | yes | `546c0bebad10` |
| `debug_put-tracepoint` | — | yes | yes | `22ca755ca464` |
| `debug_remove-probe` | — | yes | yes | `c887a715f038` |
| `debug_resolve-source-location` | — | yes | yes | `912ab037cc36` |
| `debug_status` | — | no | no | `57cbf99dced9` |
| `execute` | — | yes | yes | `2d78b0b65e2e` |
| `flush` | — | no | yes | `a4145fd39019` |
| `interaction_click` | — | yes | yes | `f1de5a6e8a99` |
| `interaction_drag` | — | yes | yes | `d3dba3eb5a4b` |
| `interaction_fill` | — | yes | yes | `24ff45073a9d` |
| `interaction_hover` | — | yes | yes | `6413f7d3f6a9` |
| `interaction_press-key` | — | yes | yes | `bb1735f88e21` |
| `interaction_resize-viewport` | — | yes | yes | `6d0fa8aff49c` |
| `interaction_resize-window` | — | no | yes | `2c489676f647` |
| `interaction_scroll` | — | no | yes | `68e8ec4f58a0` |
| `interaction_select` | — | yes | yes | `35198eb32da5` |
| `navigation_go-back-or-forward` | — | yes | yes | `22350eea7fa7` |
| `navigation_go-to` | — | yes | yes | `09f0a9ac762b` |
| `navigation_reload` | — | no | yes | `4a07a421ef02` |
| `o11y_get-console-messages` | — | no | yes | `8c51a51a673c` |
| `o11y_get-http-requests` | — | no | yes | `ecf78c993d6f` |
| `o11y_get-session-logs` | — | no | yes | `ff4187a85d74` |
| `o11y_get-session-traces` | — | no | yes | `ad01bb270f98` |
| `o11y_get-trace` | — | no | yes | `cfdbc3e8d404` |
| `o11y_get-trace-context` | — | no | no | `a397fbdf5402` |
| `o11y_get-trace-logs` | — | no | yes | `e2ca265f5d57` |
| `o11y_get-web-vitals` | — | no | yes | `7a3ab268b542` |
| `o11y_new-trace-id` | — | no | no | `64d22c56a783` |
| `o11y_set-trace-context` | — | no | yes | `3e9ce55de363` |
| `react_get-component-for-element` | — | no | yes | `85bc613a2e0e` |
| `react_get-element-for-component` | — | no | yes | `3a7b78a1bbe4` |
| `scenario-add` | — | yes | yes | `6cc4863a99ea` |
| `scenario-delete` | — | yes | yes | `e9c2a8662e4a` |
| `scenario-list` | — | no | yes | `07e37d2c52d0` |
| `scenario-recorded-actions` | — | no | yes | `cb4829dd9195` |
| `scenario-run` | — | yes | yes | `3e86cbd70154` |
| `scenario-search` | — | yes | yes | `00ef2b1bc4ea` |
| `scenario-update` | — | yes | yes | `e700f157ffc9` |
| `secrets_list` | — | no | no | `45d88d281c8e` |
| `stub_clear` | — | no | yes | `af1065677435` |
| `stub_intercept-http-request` | — | yes | yes | `9f23a6762d5d` |
| `stub_list` | — | no | no | `d45181dff217` |
| `stub_mock-http-response` | — | yes | yes | `657bab15955e` |
| `sync_wait-for-network-idle` | — | no | yes | `63df354ca474` |



## Change history

No tool-definition changes observed.
