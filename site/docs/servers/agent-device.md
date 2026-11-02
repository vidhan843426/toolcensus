# `agent-device`

| | |
|---|---|
| Latest observed version | `0.21.35` |
| Status | ok |
| Weekly downloads | 574283 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.callstack/agent-device |
| Surface hash | `sha256:d0f3dacd981e38a0` |

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
| `releases_last_90d` | 62 |
| `median_days_between_releases` | 0.76 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (62)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `action-button` | — | no | yes | `18e5f2426817` |
| `alert` | — | no | yes | `0e59186c7f39` |
| `app-switcher` | — | no | yes | `24804c524f4a` |
| `apps` | — | no | yes | `585dec352c58` |
| `appstate` | — | no | yes | `6c7ba800fdd1` |
| `artifacts` | — | no | yes | `17b5155cbfa0` |
| `audio` | — | no | yes | `184f7574977d` |
| `back` | — | no | yes | `19e2838a6fd1` |
| `batch` | — | yes | yes | `49b4b0c44bed` |
| `boot` | — | no | yes | `b46e3c47d499` |
| `capabilities` | — | no | yes | `01545c0d85f0` |
| `click` | — | yes | yes | `c4c93433dd43` |
| `clipboard` | — | yes | yes | `084632946368` |
| `close` | — | no | yes | `f8e300cc7a4d` |
| `debug` | — | yes | yes | `e9d222e342a2` |
| `devices` | — | no | yes | `fdc715c9184e` |
| `diff` | — | yes | yes | `5f5809df57c9` |
| `doctor` | — | no | yes | `dd84365459ca` |
| `events` | — | no | yes | `8fdb87f6e823` |
| `fill` | — | yes | yes | `72bd4e98c111` |
| `find` | — | yes | yes | `90589c356a02` |
| `focus` | — | yes | yes | `c40955656652` |
| `fold` | — | no | yes | `4b3e58b62170` |
| `gesture` | — | yes | yes | `d1f517610c10` |
| `get` | — | yes | yes | `c099ad5b13e4` |
| `hardware-button` | — | yes | yes | `54d74836e565` |
| `help` | — | no | yes | `ad054ddc8698` |
| `home` | — | no | yes | `b219c72e22ae` |
| `hover` | — | yes | yes | `367575e72878` |
| `install` | — | yes | yes | `a16c96b1c695` |
| `install-from-source` | — | yes | yes | `5cb77e1c8bed` |
| `is` | — | yes | yes | `bff65cf780de` |
| `keyboard` | — | no | yes | `1279b295999a` |
| `logs` | — | no | yes | `ab1c5f263e7f` |
| `longpress` | — | yes | yes | `197e343b93ab` |
| `metro` | — | yes | yes | `996bce610f0d` |
| `network` | — | no | yes | `aa4ca2dcc5b6` |
| `open` | — | no | yes | `e3f26c483310` |
| `orientation` | — | yes | yes | `89f67541af74` |
| `perf` | — | yes | yes | `2c305be861c5` |
| `press` | — | yes | yes | `dd46cc7f6e9b` |
| `push` | — | yes | yes | `0f201cb53faf` |
| `react-native` | — | yes | yes | `ce33d8ab280b` |
| `record` | — | yes | yes | `471892aa3154` |
| `reinstall` | — | yes | yes | `7fe9707d7e7f` |
| `replay` | — | yes | yes | `f53735b837d6` |
| `screenshot` | — | no | yes | `e865b5f7f24e` |
| `scroll` | — | yes | yes | `4a6a2026b9e8` |
| `session` | — | no | yes | `1d89600fedca` |
| `settings` | — | yes | yes | `e32460352493` |
| `shutdown` | — | no | yes | `35349d9cd64d` |
| `snapshot` | — | no | yes | `450b4c11aec9` |
| `swipe` | — | yes | yes | `6d82d4cb2a02` |
| `telephony` | — | yes | yes | `001f094cb843` |
| `test` | — | yes | yes | `10ea664a491c` |
| `trace` | — | yes | yes | `e06b99161953` |
| `trigger-app-event` | — | yes | yes | `3d68733fdd54` |
| `tv-remote` | — | yes | yes | `bff91cbdf2ca` |
| `type` | — | yes | yes | `a9a457f56adc` |
| `uninstall` | — | yes | yes | `cdb1cd4734ce` |
| `viewport` | — | yes | yes | `b203e58d0177` |
| `wait` | — | no | yes | `a3103a463517` |



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


