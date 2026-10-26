# `ssh-mcp`

| | |
|---|---|
| Latest observed version | `2.22.0` |
| Status | ok |
| Weekly downloads | 8761 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.tufantunc/ssh-mcp |
| Surface hash | `sha256:6d40369ad1d85ce3` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 1 of 15 tools.
    - Consider `additionalProperties: false` on the input schema of 14 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 9 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 48 |
| `median_days_between_releases` | 1.05 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (15)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `close-session` | destructiveHint | yes | no | `a78ba6e9da61` |
| `list-connections` | readOnlyHint | no | no | `fc9c5b77d9ee` |
| `list-sessions` | readOnlyHint | no | no | `c092d6f94585` |
| `open-session` | — | yes | no | `875ec6804b0f` |
| `privileged-command` | destructiveHint | yes | no | `f832e0781dbf` |
| `read-command` | readOnlyHint | yes | no | `c1b2859faadb` |
| `read-session-output` | readOnlyHint | yes | no | `e0197ad018e7` |
| `reload-config` | destructiveHint | no | no | `8ff96ebebc1f` |
| `run-command` | destructiveHint | yes | no | `579e74bf2391` |
| `sftp-download` | readOnlyHint | yes | no | `9879e4081f06` |
| `sftp-download-file` | destructiveHint | yes | no | `fbee320ba295` |
| `sftp-list` | readOnlyHint | yes | no | `c167f5eaa480` |
| `sftp-upload` | destructiveHint | yes | no | `5ecd8b5eff7a` |
| `sftp-upload-file` | destructiveHint | yes | no | `7989e12e0e82` |
| `signal-process` | destructiveHint | yes | no | `9a867fc710ea` |



## Change history

No tool-definition changes observed.
