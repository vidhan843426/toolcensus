# `@cloudbase/cloudbase-mcp`

| | |
|---|---|
| Latest observed version | `2.37.7` |
| Status | ok |
| Weekly downloads | 37568 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.TencentCloudBase/cloudbase-mcp |
| Surface hash | `sha256:24422fe7ad37720a` |

!!! tip "Improvement hints"
    - Consider `additionalProperties: false` on the input schema of 42 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 0 |
| `maintainer_count` | 16 |
| `releases_last_90d` | 35 |
| `median_days_between_releases` | 1.05 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (42)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `auth` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `1adf82384d3b` |
| `callCloudApi` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5f5747fd51cc` |
| `deployApply` | destructiveHint, openWorldHint, readOnlyHint | no | no | `9a6c25bbee69` |
| `deployBuild` | destructiveHint, openWorldHint, readOnlyHint | no | no | `8b9c232cfa87` |
| `deployPlan` | destructiveHint, openWorldHint, readOnlyHint | no | no | `875943fe12d8` |
| `downloadTemplate` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `959663bb7224` |
| `envDomainManagement` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `bb66fefce02a` |
| `manageAgents` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `90fbd45ba797` |
| `manageAppAuth` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `90d502206e2f` |
| `manageApps` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f8f004cb28e1` |
| `manageCloudRun` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6ec7f2d25d76` |
| `manageDataModel` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6665454c4f61` |
| `manageEnv` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e86d3550b1ca` |
| `manageFunctions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7d94d57f56e4` |
| `manageGateway` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2ccdfae6087b` |
| `manageHosting` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `552930f6e5c1` |
| `manageLogs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e088f6d5b2e7` |
| `manageMysqlDatabase` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fe9c647334e8` |
| `managePermissions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e97144abe876` |
| `managePgDatabase` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `0c919286fbe0` |
| `manageStorage` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6e9d4d568e26` |
| `modifyDataModel` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `207153c9c3dd` |
| `prepareFeedback` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1ecebec2aaea` |
| `queryAgents` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f484f85bb9a4` |
| `queryAppAuth` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1b8e54c273f1` |
| `queryApps` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1004a472d329` |
| `queryCloudRun` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8ae74afd3607` |
| `queryEnv` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b9101acca8e8` |
| `queryFunctions` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c98d5a8b7621` |
| `queryGateway` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ff60933a5878` |
| `queryHosting` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ccb8a93dbd0b` |
| `queryLogs` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ddc7920b7675` |
| `queryMysqlDatabase` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `315cb72980c7` |
| `queryPermissions` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `023bf9bd1dec` |
| `queryPgDatabase` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a03f03793a21` |
| `queryPgStorage` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a65882dc5bb8` |
| `queryStorage` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `7d397a6100a1` |
| `readNoSqlDatabaseContent` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b3959320cb2b` |
| `readNoSqlDatabaseStructure` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `9f2a71d3584a` |
| `searchKnowledgeBase` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5e21b6ab7d8d` |
| `writeNoSqlDatabaseContent` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7d830a20bf9c` |
| `writeNoSqlDatabaseStructure` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `001700bce624` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-46 | `2.36.2` → `2.37.5` | `auth` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `callCloudApi` | input_schema_changed (schema_other) | additionalProperties loosened; property 'params' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `deployApply` | input_schema_changed (schema_other) | additionalProperties loosened; property 'concurrency': maximum added; property 'only': maxItems added; property 'skip': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `deployBuild` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `deployPlan` | input_schema_changed (schema_other) | additionalProperties loosened; property 'only': maxItems added; property 'skip': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `downloadTemplate` | description_changed | length 1073 -&gt; 1053 |
| week 2026-46 | `2.36.2` → `2.37.5` | `downloadTemplate` | input_schema_changed (schema_other) | additionalProperties loosened; property 'ide': enum values removed |
| week 2026-46 | `2.36.2` → `2.37.5` | `envDomainManagement` | input_schema_changed (schema_other) | additionalProperties loosened; property 'domains': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageAgents` | input_schema_changed (schema_other) | additionalProperties loosened; property 'params' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageAppAuth` | input_schema_changed (schema_other) | additionalProperties loosened; property 'expireIn': maximum added; property 'config' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageApps` | input_schema_changed (schema_other) | additionalProperties loosened; property 'ignore': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageCloudRun` | input_schema_changed (schema_other) | additionalProperties loosened; property 'subnetIds': maxItems added; property 'agentConfig' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageDataModel` | input_schema_changed (schema_other) | additionalProperties loosened; property 'names': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageEnv` | input_schema_changed (schema_other) | additionalProperties loosened; property 'domains': maxItems added; property 'resources': maxItems added; property 'externalStorage' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageFunctions` | input_schema_changed (schema_other) | additionalProperties loosened; property 'layers': maxItems added; property 'runtimes': maxItems added; property 'triggers': maxItems added; property 'contentPath' changed (annotations/descriptions); property 'vpc': type changed |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageGateway` | input_schema_changed (schema_other) | additionalProperties loosened; property 'targets': maxItems added; property 'domainExtension': type changed |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageHosting` | input_schema_changed (schema_other) | additionalProperties loosened; property 'files': maxItems added; property 'routingRules': maxItems added; property 'domainConfig' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageLogs` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageMysqlDatabase` | input_schema_changed (schema_other) | additionalProperties loosened; property 'statements': maxItems added; property 'dbInstance' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `managePermissions` | input_schema_changed (schema_other) | additionalProperties loosened; property 'memberUids': maxItems added; property 'policies': maxItems added; property 'policyIds': maxItems added; property 'roleIds': maxItems added; property 'uids': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `managePgDatabase` | description_changed | length 252 -&gt; 561 |
| week 2026-46 | `2.36.2` → `2.37.5` | `managePgDatabase` | input_schema_changed (schema_other) | property 'connectionPool' added (optional); property 'maxBytesPerSecond' added (optional); property 'maxChannelsPerClient' added (optional); property 'maxConcurrentUsers' added (optional); property 'maxEventsPerSecond' added (optional); property 'maxJoinsPerSecond' added (optional); property 'maxPayloadSizeInKB' added (optional); property 'maxPresenceEventsPerSecond' added (optional); property 'p… |
| week 2026-46 | `2.36.2` → `2.37.5` | `manageStorage` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `modifyDataModel` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `prepareFeedback` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryAgents` | input_schema_changed (schema_other) | additionalProperties loosened; property 'params' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryAppAuth` | input_schema_changed (schema_other) | additionalProperties loosened; property 'pageNumber': maximum added; property 'pageSize': maximum added |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryApps` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryCloudRun` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryEnv` | description_changed | length 2373 -&gt; 2567 |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryEnv` | input_schema_changed (schema_other) | additionalProperties loosened; property 'period': enum constraint removed; property 'fields': maxItems added; property 'limit': maximum added; property 'offset': maximum added; property 'type': maxItems added; property 'needUsageDetails' changed (annotations/descriptions); property 'period': type changed |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryFunctions` | input_schema_changed (schema_other) | additionalProperties loosened; property 'order': enum constraint added; property 'orderBy': enum constraint added |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryGateway` | input_schema_changed (schema_other) | additionalProperties loosened; property 'limit': maximum added; property 'offset': maximum added |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryHosting` | input_schema_changed (schema_other) | additionalProperties loosened; property 'domains': maxItems added; property 'maxKeys': maximum added; property 'prefix' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryLogs` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryMysqlDatabase` | input_schema_changed (schema_other) | additionalProperties loosened; property 'keyWords': maxItems added; property 'logLevels': maxItems added; property 'dbInstance' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryPermissions` | input_schema_changed (schema_other) | additionalProperties loosened; property 'resourceIds': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryPgDatabase` | description_changed | length 88 -&gt; 351 |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryPgDatabase` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryPgStorage` | input_schema_changed (schema_other) | additionalProperties loosened; property 'objectKeys': maxItems added; property 'objects': maxItems added |
| week 2026-46 | `2.36.2` → `2.37.5` | `queryStorage` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `readNoSqlDatabaseContent` | input_schema_changed (schema_other) | additionalProperties loosened; property 'projection' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `readNoSqlDatabaseStructure` | input_schema_changed (schema_widened) | additionalProperties loosened |
| week 2026-46 | `2.36.2` → `2.37.5` | `searchKnowledgeBase` | input_schema_changed (schema_other) | additionalProperties loosened; property 'apiName' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `writeNoSqlDatabaseContent` | input_schema_changed (schema_other) | additionalProperties loosened; property 'documents': maxItems added; property 'query' changed (annotations/descriptions) |
| week 2026-46 | `2.36.2` → `2.37.5` | `writeNoSqlDatabaseStructure` | input_schema_changed (schema_other) | additionalProperties loosened; property 'updateOptions' changed (annotations/descriptions) |
| week 2026-47 | `2.37.5` → `2.37.7` | `deployApply` | description_changed | length 870 -&gt; 1211 |
| week 2026-47 | `2.37.5` → `2.37.7` | `deployBuild` | description_changed | length 454 -&gt; 542 |
| week 2026-47 | `2.37.5` → `2.37.7` | `deployPlan` | description_changed | length 652 -&gt; 1076 |
| week 2026-47 | `2.37.5` → `2.37.7` | `managePermissions` | description_changed | length 2324 -&gt; 2363 |
| week 2026-47 | `2.37.5` → `2.37.7` | `queryPermissions` | description_changed | length 1167 -&gt; 1225 |


