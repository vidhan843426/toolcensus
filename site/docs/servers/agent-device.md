# `agent-device`

| | |
|---|---|
| Latest observed version | `0.21.37` |
| Status | ok |
| Weekly downloads | 681487 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.callstack/agent-device |
| Surface hash | `sha256:1c039dbc9d51a865` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 62 of 62 tools.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 0 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 68 |
| `median_days_between_releases` | 0.76 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (62)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `action-button` | — | no | yes | `e6e157ff9289` |
| `alert` | — | no | yes | `86088395c6cd` |
| `app-switcher` | — | no | yes | `4da7941c8fbe` |
| `apps` | — | no | yes | `42bd849b5c7a` |
| `appstate` | — | no | yes | `040cd4d039c5` |
| `artifacts` | — | no | yes | `d29cc9956c4c` |
| `audio` | — | no | yes | `7bb4166ce47b` |
| `back` | — | no | yes | `2a598b8cbb1c` |
| `batch` | — | yes | yes | `104b47c994af` |
| `boot` | — | no | yes | `d1ded0b42f95` |
| `capabilities` | — | no | yes | `b208829d87d1` |
| `click` | — | no | yes | `7744df0e6bbe` |
| `clipboard` | — | yes | yes | `1e136ba3f9e3` |
| `close` | — | no | yes | `24913edff210` |
| `debug` | — | yes | yes | `edb6b199b723` |
| `devices` | — | no | yes | `bae9d773fc8a` |
| `diff` | — | yes | yes | `ca12eac6b131` |
| `doctor` | — | no | yes | `439ef955d40f` |
| `events` | — | no | yes | `a0eff79c34e4` |
| `fill` | — | yes | yes | `6334f6ad7968` |
| `find` | — | yes | yes | `d43c0be558e3` |
| `focus` | — | yes | yes | `9595e1f1abb6` |
| `fold` | — | no | yes | `03a77f8622aa` |
| `gesture` | — | yes | yes | `464f96ce79a6` |
| `get` | — | yes | yes | `9925b0d3ca07` |
| `hardware-button` | — | yes | yes | `c85baf0c37de` |
| `help` | — | no | yes | `ad054ddc8698` |
| `home` | — | no | yes | `ec74f8682e03` |
| `hover` | — | no | yes | `ddf6860a9481` |
| `install` | — | yes | yes | `9769cbcf4cbd` |
| `install-from-source` | — | yes | yes | `462bb5828e45` |
| `is` | — | yes | yes | `221ee2b40bd1` |
| `keyboard` | — | no | yes | `6f4e582a181e` |
| `logs` | — | no | yes | `580635f09b7c` |
| `longpress` | — | no | yes | `14f491302ae6` |
| `metro` | — | yes | yes | `caab4dd73fda` |
| `network` | — | no | yes | `f80e31fc1189` |
| `open` | — | no | yes | `87c7c38c7d29` |
| `orientation` | — | yes | yes | `5c979a8c3ca5` |
| `perf` | — | yes | yes | `85bb71eb9419` |
| `press` | — | no | yes | `644167d70988` |
| `push` | — | yes | yes | `e98002a7ef0e` |
| `react-native` | — | yes | yes | `6f551cce8ab6` |
| `record` | — | yes | yes | `819a969839fd` |
| `reinstall` | — | yes | yes | `82e0463094cf` |
| `replay` | — | yes | yes | `08ed640efb45` |
| `screenshot` | — | no | yes | `b218fd746d7c` |
| `scroll` | — | yes | yes | `af30481e5b97` |
| `session` | — | no | yes | `3cdd462e0c68` |
| `settings` | — | yes | yes | `a450ac18f23d` |
| `shutdown` | — | no | yes | `49e727c3f3fa` |
| `snapshot` | — | no | yes | `840d60711468` |
| `swipe` | — | yes | yes | `c6ef4e473a36` |
| `telephony` | — | yes | yes | `a3add2e24b16` |
| `test` | — | yes | yes | `6e6d5d9a1d26` |
| `trace` | — | yes | yes | `e74bdef98f0c` |
| `trigger-app-event` | — | yes | yes | `722737f15479` |
| `tv-remote` | — | yes | yes | `b344b239e5c2` |
| `type` | — | yes | yes | `c5a2ffec3c5c` |
| `uninstall` | — | yes | yes | `9f2e9c33982a` |
| `viewport` | — | yes | yes | `adf86ee49252` |
| `wait` | — | no | yes | `883e1d0c831f` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-44 | `0.21.31` → `0.21.32` | `back` | description_changed | length 369 -&gt; 430 |
| week 2026-44 | `0.21.31` → `0.21.32` | `fold` | description_changed | length 1296 -&gt; 1216 |
| week 2026-44 | `0.21.31` → `0.21.32` | `fold` | output_schema_changed |  |
| week 2026-44 | `0.21.31` → `0.21.32` | `longpress` | description_changed | length 234 -&gt; 234 |
| week 2026-45 | `0.21.32` → `0.21.35` | `alert` | description_changed | length 998 -&gt; 1189 |
| week 2026-45 | `0.21.32` → `0.21.35` | `boot` | input_schema_changed (schema_widened) | property 'pick' added (optional) |
| week 2026-45 | `0.21.32` → `0.21.35` | `boot` | output_schema_changed |  |
| week 2026-45 | `0.21.32` → `0.21.35` | `close` | description_changed | length 310 -&gt; 492 |
| week 2026-45 | `0.21.32` → `0.21.35` | `install` | input_schema_changed (schema_widened) | property 'imageTag' added (optional); property 'osVersion' added (optional); property 'physical' added (optional) |
| week 2026-45 | `0.21.32` → `0.21.35` | `open` | input_schema_changed (schema_other) | property 'imageTag' added (optional); property 'osVersion' added (optional); property 'physical' added (optional); property 'launchConsole' changed (annotations/descriptions) |
| week 2026-45 | `0.21.32` → `0.21.35` | `orientation` | description_changed | length 170 -&gt; 295 |
| week 2026-45 | `0.21.32` → `0.21.35` | `reinstall` | input_schema_changed (schema_widened) | property 'imageTag' added (optional); property 'osVersion' added (optional); property 'physical' added (optional) |
| week 2026-45 | `0.21.32` → `0.21.35` | `uninstall` | input_schema_changed (schema_widened) | property 'imageTag' added (optional); property 'osVersion' added (optional); property 'physical' added (optional) |
| week 2026-46 | `0.21.35` → `0.21.36` | `close` | description_changed | length 492 -&gt; 576 |
| week 2026-46 | `0.21.35` → `0.21.36` | `find` | description_changed | length 301 -&gt; 331 |
| week 2026-46 | `0.21.35` → `0.21.36` | `fold` | description_changed | length 1216 -&gt; 1256 |
| week 2026-46 | `0.21.35` → `0.21.36` | `install` | description_changed | length 199 -&gt; 306 |
| week 2026-46 | `0.21.35` → `0.21.36` | `install-from-source` | description_changed | length 116 -&gt; 238 |
| week 2026-46 | `0.21.35` → `0.21.36` | `reinstall` | description_changed | length 179 -&gt; 300 |
| week 2026-46 | `0.21.35` → `0.21.36` | `uninstall` | description_changed | length 156 -&gt; 206 |
| week 2026-47 | `0.21.36` → `0.21.37` | `action-button` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `action-button` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `alert` | description_changed | length 1189 -&gt; 1167 |
| week 2026-47 | `0.21.36` → `0.21.37` | `alert` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `app-switcher` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `app-switcher` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `apps` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `apps` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `appstate` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `appstate` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `artifacts` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `audio` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `back` | description_changed | length 430 -&gt; 816 |
| week 2026-47 | `0.21.36` → `0.21.37` | `back` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `back` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `batch` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `boot` | description_changed | length 220 -&gt; 321 |
| week 2026-47 | `0.21.36` → `0.21.37` | `boot` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `boot` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `capabilities` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `click` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'x' added (optional); property 'y' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `click` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `clipboard` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `clipboard` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `close` | description_changed | length 576 -&gt; 798 |
| week 2026-47 | `0.21.36` → `0.21.37` | `close` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `debug` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `devices` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `devices` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `diff` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `diff` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `doctor` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `doctor` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `events` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `fill` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'x' added (optional); property 'y' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `fill` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `find` | description_changed | length 331 -&gt; 711 |
| week 2026-47 | `0.21.36` → `0.21.37` | `find` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `find` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `focus` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `fold` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `fold` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `gesture` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `get` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `hardware-button` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `hardware-button` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `home` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `home` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `hover` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'x' added (optional); property 'y' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `hover` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `install` | input_schema_changed (schema_other) | property 'deviceBaseline' added (optional); property 'deviceMode' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `install-from-source` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'retentionMs': minimum added; property 'retentionMs': maximum added; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `is` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `keyboard` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `keyboard` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `logs` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `longpress` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'x' added (optional); property 'y' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `longpress` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `metro` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `network` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `open` | description_changed | length 502 -&gt; 651 |
| week 2026-47 | `0.21.36` → `0.21.37` | `open` | input_schema_changed (schema_other) | property 'deviceBaseline' added (optional); property 'deviceMode' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `orientation` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `orientation` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `perf` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `press` | input_schema_changed (schema_other) | property 'label' added (optional); property 'ref' added (optional); property 'selector' added (optional); property 'x' added (optional); property 'y' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'target' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `press` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `push` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `push` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `react-native` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `record` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `record` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `reinstall` | input_schema_changed (schema_other) | property 'deviceBaseline' added (optional); property 'deviceMode' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `replay` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `replay` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `screenshot` | input_schema_changed (schema_other) | property 'captureBackend' added (optional); property 'screenMask' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `scroll` | description_changed | length 1118 -&gt; 1154 |
| week 2026-47 | `0.21.36` → `0.21.37` | `scroll` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `scroll` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `session` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `settings` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'app' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `shutdown` | description_changed | length 63 -&gt; 310 |
| week 2026-47 | `0.21.36` → `0.21.37` | `shutdown` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `shutdown` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `snapshot` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `swipe` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `telephony` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `telephony` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `test` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `test` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `trace` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `trace` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `trigger-app-event` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `trigger-app-event` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `tv-remote` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `tv-remote` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `type` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `uninstall` | input_schema_changed (schema_other) | property 'deviceBaseline' added (optional); property 'deviceMode' added (optional); property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `viewport` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `viewport` | output_schema_changed |  |
| week 2026-47 | `0.21.36` → `0.21.37` | `wait` | description_changed | length 299 -&gt; 471 |
| week 2026-47 | `0.21.36` → `0.21.37` | `wait` | input_schema_changed (schema_other) | property 'androidDeviceAllowlist' removed; property 'leaseId' removed; property 'runId' removed; property 'tenant' removed; property 'device' changed (annotations/descriptions) |
| week 2026-47 | `0.21.36` → `0.21.37` | `wait` | output_schema_changed |  |


