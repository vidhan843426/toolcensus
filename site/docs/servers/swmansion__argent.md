# `@swmansion/argent`

| | |
|---|---|
| Latest observed version | `0.31.0` |
| Status | ok |
| Weekly downloads | 217109 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.software-mansion/argent |
| Surface hash | `sha256:4f3b04b4e5188dce` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 49 of 77 tools.
    - Consider `additionalProperties: false` on the input schema of 72 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 5 |
| `maintainer_count` | 3 |
| `releases_last_90d` | 310 |
| `median_days_between_releases` | 0.04 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (77)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `await-screen-idle` | readOnlyHint | yes | yes | `8f3320205979` |
| `await-ui-element` | readOnlyHint | yes | yes | `f45bbbe738ad` |
| `boot-device` | — | no | no | `6a923ffe8228` |
| `button` | — | yes | no | `e84824f87e27` |
| `chromium-cookies` | — | yes | no | `19377a5dca87` |
| `chromium-storage` | — | yes | no | `61eab312f969` |
| `chromium-tabs` | — | yes | no | `107c36bfdee1` |
| `debugger-component-tree` | readOnlyHint | yes | no | `3a946131aefe` |
| `debugger-connect` | — | yes | no | `19a72b144f9c` |
| `debugger-evaluate` | — | yes | no | `80d369151c8d` |
| `debugger-inspect-element` | readOnlyHint | yes | no | `d44115ffaa57` |
| `debugger-log-registry` | readOnlyHint | yes | no | `e7d977f736f3` |
| `debugger-reload-metro` | — | yes | no | `392ee9a83e60` |
| `debugger-status` | readOnlyHint | yes | no | `839475683947` |
| `describe` | readOnlyHint | yes | no | `5b2fb06aa096` |
| `dismiss-update` | — | yes | no | `f820f2ae6435` |
| `e2e-add-echo` | — | yes | no | `3dc751d55d73` |
| `e2e-add-script` | — | yes | no | `3d9ca9953cc3` |
| `e2e-add-step` | — | yes | no | `dc30b51257ca` |
| `e2e-execute` | — | yes | no | `7003f71fc54f` |
| `e2e-finish-recording` | — | yes | no | `d8b244589950` |
| `e2e-read-prerequisite` | readOnlyHint | yes | no | `78946928659e` |
| `e2e-start-recording` | — | yes | no | `414d86b9c39d` |
| `fold` | — | yes | no | `11269f1161fd` |
| `gather-workspace-data` | readOnlyHint | yes | no | `c08d4f72ad7d` |
| `gesture-custom` | — | yes | no | `f61cad314aa0` |
| `gesture-drag` | — | yes | no | `040273daeb83` |
| `gesture-pinch` | — | yes | no | `bd185674dafd` |
| `gesture-rotate` | — | yes | no | `278048c0d022` |
| `gesture-scroll` | — | yes | no | `449f4346e93d` |
| `gesture-swipe` | — | yes | no | `a516a49ba870` |
| `gesture-tap` | — | yes | no | `fb5b9635cae7` |
| `keyboard` | — | yes | no | `a88b3b6191e9` |
| `launch-app` | — | yes | no | `789a614af458` |
| `list-devices` | readOnlyHint | no | no | `791702831aac` |
| `native-describe-screen` | readOnlyHint | yes | no | `f09a47750e20` |
| `native-devtools-status` | readOnlyHint | yes | no | `e3b4c7c367ce` |
| `native-find-views` | readOnlyHint | yes | no | `22cc8c7bb441` |
| `native-full-hierarchy` | readOnlyHint | yes | no | `0c01afe33014` |
| `native-network-logs` | — | yes | no | `95ef7b7372c4` |
| `native-profiler-analyze` | — | yes | no | `0c67df9879ce` |
| `native-profiler-start` | — | yes | no | `234bbe6de622` |
| `native-profiler-stop` | — | yes | no | `a1dc1d6db512` |
| `native-user-interactable-view-at-point` | readOnlyHint | yes | no | `c61f5955fc4b` |
| `native-view-at-point` | readOnlyHint | yes | no | `b986c912b173` |
| `open-url` | — | yes | no | `d3253cad5eac` |
| `paste` | — | yes | no | `ee507a671528` |
| `profiler-combined-report` | readOnlyHint | yes | no | `fae38d574ae2` |
| `profiler-commit-query` | readOnlyHint | yes | no | `a1fe79848347` |
| `profiler-cpu-query` | readOnlyHint | yes | no | `8daac38219f3` |
| `profiler-load` | — | yes | no | `fa56c5aab872` |
| `profiler-stack-query` | readOnlyHint | yes | no | `7c7c9f8d4614` |
| `react-profiler-analyze` | — | yes | no | `7914568b69d8` |
| `react-profiler-component-source` | readOnlyHint | yes | no | `81af27e79f04` |
| `react-profiler-cpu-summary` | readOnlyHint | yes | no | `5440a2a92c9a` |
| `react-profiler-fiber-tree` | readOnlyHint | yes | no | `024c32a3153a` |
| `react-profiler-renders` | readOnlyHint | yes | no | `c2b09abea93f` |
| `react-profiler-start` | — | yes | no | `748cb0e56131` |
| `react-profiler-status` | readOnlyHint | yes | no | `7767d320a390` |
| `react-profiler-stop` | — | yes | no | `8ff0e62420bf` |
| `reinstall-app` | — | yes | no | `cf723d178a51` |
| `restart-app` | — | yes | no | `4314633a4a04` |
| `rotate` | — | yes | no | `f7e2c0ea723e` |
| `run-sequence` | — | yes | no | `a2e10baa68d3` |
| `screen-recording-start` | — | yes | no | `034cea49e559` |
| `screen-recording-stop` | — | yes | no | `d2ebc2052377` |
| `screenshot` | readOnlyHint | yes | no | `893aefd66910` |
| `screenshot-diff` | — | yes | yes | `c2609a756b08` |
| `settings-permissions` | — | yes | no | `f91a816463e5` |
| `shake` | — | yes | no | `d09c7fc2a867` |
| `stop-all-simulator-servers` | — | no | yes | `ece80a977ae4` |
| `stop-metro` | — | no | no | `ad26dee14ebc` |
| `stop-simulator-server` | — | yes | no | `b06a48b3a6b3` |
| `tv-remote` | — | yes | no | `57756ccca726` |
| `update-argent` | — | no | no | `c25a16ce51f7` |
| `view-network-logs` | readOnlyHint | yes | no | `eadd377c9457` |
| `view-network-request-details` | readOnlyHint | yes | no | `69da19b525fa` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-45 | `0.30.1` → `0.31.0` | `await-screen-idle` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `await-ui-element` | description_changed | length 1977 -&gt; 1977 |
| week 2026-45 | `0.30.1` → `0.31.0` | `await-ui-element` | input_schema_changed (schema_other) | property 'bundleId' changed (annotations/descriptions) |
| week 2026-45 | `0.30.1` → `0.31.0` | `await-ui-element` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `boot-device` | description_changed | length 1281 -&gt; 1288 |
| week 2026-45 | `0.30.1` → `0.31.0` | `boot-device` | input_schema_changed (schema_other) | property 'guestVulkan' added (optional); property 'electronAppPath' changed (annotations/descriptions) |
| week 2026-45 | `0.30.1` → `0.31.0` | `debugger-component-tree` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `debugger-inspect-element` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `debugger-log-registry` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `debugger-status` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `describe` | input_schema_changed (schema_other) | property 'bundleId' changed (annotations/descriptions) |
| week 2026-45 | `0.30.1` → `0.31.0` | `describe` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `e2e-read-prerequisite` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `gather-workspace-data` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `gesture-custom` | input_schema_changed (schema_other) | property 'events' changed (annotations/descriptions) |
| week 2026-45 | `0.30.1` → `0.31.0` | `launch-app` | description_changed | length 1414 -&gt; 1369 |
| week 2026-45 | `0.30.1` → `0.31.0` | `list-devices` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-describe-screen` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-devtools-status` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-find-views` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-full-hierarchy` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-user-interactable-view-at-point` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `native-view-at-point` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `profiler-combined-report` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `profiler-commit-query` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `profiler-cpu-query` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `profiler-stack-query` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `react-profiler-component-source` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `react-profiler-cpu-summary` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `react-profiler-fiber-tree` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `react-profiler-renders` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `react-profiler-status` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `restart-app` | description_changed | length 398 -&gt; 425 |
| week 2026-45 | `0.30.1` → `0.31.0` | `screenshot` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `stop-all-simulator-servers` | description_changed | length 2893 -&gt; 3062 |
| week 2026-45 | `0.30.1` → `0.31.0` | `stop-metro` | description_changed | length 387 -&gt; 478 |
| week 2026-45 | `0.30.1` → `0.31.0` | `stop-simulator-server` | description_changed | length 881 -&gt; 974 |
| week 2026-45 | `0.30.1` → `0.31.0` | `view-network-logs` | annotations_changed |  |
| week 2026-45 | `0.30.1` → `0.31.0` | `view-network-request-details` | annotations_changed |  |


