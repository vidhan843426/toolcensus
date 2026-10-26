# `@metamask/device-mcp`

| | |
|---|---|
| Latest observed version | `0.5.0` |
| Status | ok |
| Weekly downloads | 20788 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:1669210b7c61ae40` |

!!! tip "Improvement hints"
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 19 of 29 tools.
    - Consider `additionalProperties: false` on the input schema of 22 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 2 |
| `maintainer_count` | 6 |
| `releases_last_90d` | 5 |
| `median_days_between_releases` | 8.07 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (29)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `device_app_state` | readOnlyHint | yes | no | `c88df3fc4a2f` |
| `device_clipboard` | — | yes | no | `99400ec91051` |
| `device_close_app` | — | yes | no | `94cf4eee1864` |
| `device_context` | — | yes | no | `e7ef1b0765ca` |
| `device_dismiss_alert` | — | yes | no | `6df945ef7004` |
| `device_dismiss_keyboard` | — | no | no | `93b01b97a7fe` |
| `device_generate_locators` | readOnlyHint | no | no | `4f811db237da` |
| `device_get_alert_text` | readOnlyHint | no | no | `e130f651bc48` |
| `device_get_element_text` | — | no | no | `e01737cd7c71` |
| `device_get_window_size` | readOnlyHint | no | no | `5b120b344150` |
| `device_info` | readOnlyHint | no | no | `735b85ff4c45` |
| `device_list_devices` | readOnlyHint | no | no | `58138c20663f` |
| `device_logs` | readOnlyHint | no | no | `63b24bbf0c59` |
| `device_long_press` | — | no | no | `2d5937e8be0b` |
| `device_open_app` | — | yes | no | `ecf0431c7535` |
| `device_press_button` | — | yes | no | `4b5a388d6275` |
| `device_screen_recording` | — | yes | no | `5876a46dd012` |
| `device_screenshot` | readOnlyHint | no | no | `e745c4b96536` |
| `device_scroll_to_element` | — | no | no | `5a40553d5a9d` |
| `device_select_device` | — | yes | no | `7efb06bf159a` |
| `device_snapshot` | readOnlyHint | no | no | `5780509fc0c4` |
| `device_swipe` | — | yes | no | `1010d605e45c` |
| `device_tap_coordinates` | — | yes | no | `a3808b757467` |
| `device_tap_element` | — | no | no | `39bf55108765` |
| `device_type` | — | yes | no | `3fc178b92b30` |
| `device_wait_for` | — | no | no | `60aa083978c9` |
| `hermes_cdp` | — | yes | no | `88c82063b94e` |
| `hermes_targets` | readOnlyHint | no | no | `052134ef6746` |
| `webview_cdp` | — | yes | no | `5208abec0736` |



## Change history

No tool-definition changes observed.
