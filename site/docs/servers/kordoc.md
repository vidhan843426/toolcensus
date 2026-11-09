# `kordoc`

| | |
|---|---|
| Latest observed version | `4.24.57` |
| Status | ok |
| Weekly downloads | 62863 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.chrisryugj/kordoc |
| Surface hash | `sha256:963b1eb6997d5168` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 22 of 22 tools.
    - Consider `additionalProperties: false` on the input schema of 22 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 7 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 169 |
| `median_days_between_releases` | 0.24 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (22)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `add_memo` | — | yes | no | `09ccffb1411f` |
| `agency_pack_info` | — | yes | no | `9ba790116f55` |
| `build_agency_pack` | — | yes | no | `9267f64f5fcf` |
| `compare_documents` | — | yes | no | `ecc7a56f5b3c` |
| `convert_to_hwpx` | — | yes | no | `f94f48ea313f` |
| `crop_regions` | — | yes | no | `2cac515f87f9` |
| `detect_format` | — | yes | no | `8836db5f1082` |
| `extract_profile` | — | yes | no | `b5a8a4f9bfbe` |
| `extract_tables` | — | yes | no | `fd1e8551b417` |
| `fill_form` | — | no | no | `a395e9c60318` |
| `generate_document` | — | yes | no | `ccb7807407e6` |
| `lint_document` | — | no | no | `5301f3ff43f2` |
| `parse_chunks` | — | yes | no | `9e3e96c6f80e` |
| `parse_document` | — | yes | no | `b88385c8d591` |
| `parse_form` | — | yes | no | `70c8b5e46ec8` |
| `parse_metadata` | — | yes | no | `7712aa3b01df` |
| `parse_pages` | — | yes | no | `d118c1741afc` |
| `parse_table` | — | yes | no | `71db4d02e532` |
| `patch_document` | — | yes | no | `f4abe20888e2` |
| `place_seal` | — | yes | no | `e5c3b2684e84` |
| `redact_document` | — | yes | no | `56eab03f0abc` |
| `render_document` | — | yes | no | `dd59fdee55a1` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `4.24.38` → `4.24.57` | `convert_to_hwpx` | description_changed | length 270 -&gt; 267 |
| week 2026-46 | `4.24.38` → `4.24.57` | `parse_document` | input_schema_changed (schema_widened) | property 'ocr_rec': enum values added |


