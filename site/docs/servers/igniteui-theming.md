# `igniteui-theming`

| | |
|---|---|
| Latest observed version | `30.2.0` |
| Status | ok |
| Weekly downloads | 11928 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.IgniteUI/igniteui-theming |
| Surface hash | `sha256:7a928fdcf8d518fb` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 15 of 15 tools.
    - Consider `additionalProperties: false` on the input schema of 15 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 3 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 16 |
| `median_days_between_releases` | 1.25 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (15)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `create_component_theme` | — | yes | no | `5df91361726e` |
| `create_custom_palette` | — | yes | no | `72f72dd994ff` |
| `create_elevations` | — | no | no | `aaefa6dba75d` |
| `create_palette` | — | yes | no | `82c95576b3fd` |
| `create_theme` | — | yes | no | `6697e39d7a75` |
| `create_typography` | — | yes | no | `6f16d608a7bc` |
| `detect_platform` | — | no | no | `3e1ef6c5a93e` |
| `fit_color_scale` | — | yes | no | `a181481ae4bc` |
| `get_chart_series_colors` | — | no | no | `1ce45923ed67` |
| `get_color` | — | yes | no | `ae55404206b7` |
| `get_component_design_tokens` | — | yes | no | `e3424c12267b` |
| `read_resource` | — | yes | no | `209707e963d1` |
| `set_roundness` | — | yes | no | `edd98b25d4c8` |
| `set_size` | — | yes | no | `56bac120551e` |
| `set_spacing` | — | yes | no | `bf7f1af3cab7` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `30.0.0` → `30.1.0` | `create_component_theme` | input_schema_changed (schema_other) | additionalProperties loosened; property 'tokens' changed (annotations/descriptions) |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_custom_palette` | input_schema_changed (schema_other) | additionalProperties loosened; property 'error' changed (annotations/descriptions) |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_elevations` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_palette` | input_schema_changed (schema_other) | additionalProperties loosened; property 'error': pattern added; property 'info': pattern added; property 'success': pattern added; property 'warn': pattern added; property 'error': type changed; property 'info': type changed; property 'success': type changed; property 'warn': type changed |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_theme` | description_changed | length 4167 -&gt; 4380 |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_theme` | input_schema_changed (schema_other) | additionalProperties loosened; property 'scales' changed (annotations/descriptions) |
| week 2026-46 | `30.0.0` → `30.1.0` | `create_typography` | input_schema_changed (schema_other) | additionalProperties loosened; property 'customScale' changed (annotations/descriptions) |
| week 2026-46 | `30.0.0` → `30.1.0` | `detect_platform` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `fit_color_scale` | description_changed | length 1050 -&gt; 1188 |
| week 2026-46 | `30.0.0` → `30.1.0` | `fit_color_scale` | input_schema_changed (schema_other) | property 'family' added (optional); additionalProperties loosened; property 'name' changed (annotations/descriptions) |
| week 2026-46 | `30.0.0` → `30.1.0` | `get_chart_series_colors` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `get_color` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `get_component_design_tokens` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `read_resource` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `set_roundness` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `set_size` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `30.0.0` → `30.1.0` | `set_spacing` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-47 | `30.1.0` → `30.2.0` | `create_component_theme` | description_changed | length 6841 -&gt; 7784 |


