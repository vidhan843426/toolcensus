# `@browserstack/mcp-server`

| | |
|---|---|
| Latest observed version | `2.4.5` |
| Status | ok |
| Weekly downloads | 36429 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.browserstack/mcp-server |
| Surface hash | `sha256:09e6fcca5c7d5d89` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 1 of 52 tools.
    - Consider `additionalProperties: false` on the input schema of 51 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 13 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 97 |
| `median_days_between_releases` | 0.56 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (52)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `accessibilityExpert` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `1c69a27149c3` |
| `addPercySnapshotCommands` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `470230e6c034` |
| `addTestResult` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `2b28dc7bc058` |
| `askBrowserStackAI` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `694b168e84a3` |
| `createAccessibilityAuthConfig` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `767f83b50967` |
| `createLCASteps` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `48a9017d74e4` |
| `createProjectOrFolder` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `e2a684d1ebbd` |
| `createTestCase` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `96ac3b64100b` |
| `createTestCasesFromFile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a7fb0261637e` |
| `createTestRun` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3a2a044e0fff` |
| `describeCapability` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `352ec4b44f7b` |
| `describeEntity` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d8d19a5fe807` |
| `expandPercyVisualTesting` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `b564655f9cb7` |
| `fetchAccessibilityIssues` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `04ba9487d0b1` |
| `fetchAutomationScreenshots` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `7e6e030beb49` |
| `fetchBuildInsights` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9d116cfd68eb` |
| `fetchPercyChanges` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3713154564de` |
| `fetchRCA` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `669eec694df9` |
| `fetchSelfHealedSelectors` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `567ed62cfbdc` |
| `getAccessibilityAuthConfig` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `c65df5b526f9` |
| `getBuildId` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `3b49c717bdee` |
| `getFailureLogs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `141bf99e3f5a` |
| `getSubTestPlan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `00e2f11a23b1` |
| `getTestPlan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `849e2117283b` |
| `invokeCapability` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `da3a64f39278` |
| `listBuildId` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `ff8ca5364475` |
| `listFolders` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fed8f57a5f9f` |
| `listProducts` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f1e31628e46a` |
| `listSessions` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e6ecd8d01563` |
| `listSubTestPlans` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9bacf442c316` |
| `listTestCaseTemplates` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `6ff0cc4763de` |
| `listTestCases` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `d6658d760f7e` |
| `listTestFiles` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `f492f8213996` |
| `listTestIds` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `9880a0f35858` |
| `listTestPlans` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `919fb2363454` |
| `listTestRuns` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `70ea9abf7f3a` |
| `managePercyBuildApproval` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `5635eb86ad4e` |
| `percyVisualTestIntegrationAgent` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `46731c762a53` |
| `prepareSelfHealingPlan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `a2d3c3df0b18` |
| `runAppLiveSession` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `f52b517e820a` |
| `runAppTestsOnBrowserStack` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `afc98aa2acd0` |
| `runBrowserLiveSession` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4bbd5758f356` |
| `runPercyScan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `fe2d509295d3` |
| `searchCapability` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `353bb3dd75f8` |
| `setupBrowserStackAppAutomateTests` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `946541dc7984` |
| `setupBrowserStackAutomateTests` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `229266611249` |
| `startAccessibilityScan` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `e2ed92adb540` |
| `submitFeedback` | — | yes | no | `2bf20ada29c1` |
| `takeAppScreenshot` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `6bc2527a2427` |
| `updateTestCase` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `456757fa48c2` |
| `updateTestRun` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `4487c369f00e` |
| `uploadProductRequirementFile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | no | `de38a3473d91` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-44 | `2.2.7` → `2.2.8` | `setupBrowserStackAutomateTests` | input_schema_changed (schema_widened) | property 'accessibility' added (optional) |
| week 2026-44 | `2.2.7` → `2.2.8` | `startAccessibilityScan` | input_schema_changed (schema_widened) | property 'experimentalRules' added (optional) |
| week 2026-45 | `2.2.8` → `2.4.5` | `addTestResult` | description_changed | length 293 -&gt; 124 |
| week 2026-45 | `2.2.8` → `2.4.5` | `askBrowserStackAI` | description_changed | length 1006 -&gt; 532 |
| week 2026-45 | `2.2.8` → `2.4.5` | `askBrowserStackAI` | input_schema_changed (schema_other) | property 'product' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `createLCASteps` | description_changed | length 340 -&gt; 149 |
| week 2026-45 | `2.2.8` → `2.4.5` | `createProjectOrFolder` | description_changed | length 264 -&gt; 217 |
| week 2026-45 | `2.2.8` → `2.4.5` | `createTestCase` | description_changed | length 283 -&gt; 143 |
| week 2026-45 | `2.2.8` → `2.4.5` | `createTestCase` | input_schema_changed (schema_other) | property 'automation_status' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `createTestRun` | description_changed | length 265 -&gt; 142 |
| week 2026-45 | `2.2.8` → `2.4.5` | `describeCapability` | description_changed | length 753 -&gt; 201 |
| week 2026-45 | `2.2.8` → `2.4.5` | `describeCapability` | input_schema_changed (schema_other) | property 'product': enum values added; property 'include_responses' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `describeEntity` | description_changed | length 219 -&gt; 132 |
| week 2026-45 | `2.2.8` → `2.4.5` | `describeEntity` | input_schema_changed (schema_widened) | property 'product': enum values added |
| week 2026-45 | `2.2.8` → `2.4.5` | `expandPercyVisualTesting` | description_changed | length 266 -&gt; 128 |
| week 2026-45 | `2.2.8` → `2.4.5` | `expandPercyVisualTesting` | input_schema_changed (schema_other) | property 'filePaths' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `fetchAccessibilityIssues` | description_changed | length 193 -&gt; 198 |
| week 2026-45 | `2.2.8` → `2.4.5` | `fetchAccessibilityIssues` | input_schema_changed (schema_other) | property 'appReportId' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `fetchRCA` | description_changed | length 236 -&gt; 189 |
| week 2026-45 | `2.2.8` → `2.4.5` | `fetchRCA` | input_schema_changed (schema_other) | property 'testId' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `fetchSelfHealedSelectors` | description_changed | length 452 -&gt; 226 |
| week 2026-45 | `2.2.8` → `2.4.5` | `getAccessibilityAuthConfig` | description_changed | length 150 -&gt; 133 |
| week 2026-45 | `2.2.8` → `2.4.5` | `getFailureLogs` | description_changed | length 242 -&gt; 153 |
| week 2026-45 | `2.2.8` → `2.4.5` | `getSubTestPlan` | description_changed | length 649 -&gt; 394 |
| week 2026-45 | `2.2.8` → `2.4.5` | `getTestPlan` | description_changed | length 807 -&gt; 422 |
| week 2026-45 | `2.2.8` → `2.4.5` | `invokeCapability` | description_changed | length 852 -&gt; 454 |
| week 2026-45 | `2.2.8` → `2.4.5` | `invokeCapability` | input_schema_changed (schema_other) | property 'select' added (optional); property 'product': enum values added; property 'name' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `listFolders` | description_changed | length 437 -&gt; 166 |
| week 2026-45 | `2.2.8` → `2.4.5` | `listProducts` | description_changed | length 856 -&gt; 252 |
| week 2026-45 | `2.2.8` → `2.4.5` | `listProducts` | input_schema_changed (schema_other) | property 'query' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `listSubTestPlans` | description_changed | length 655 -&gt; 396 |
| week 2026-45 | `2.2.8` → `2.4.5` | `listTestCases` | description_changed | length 472 -&gt; 200 |
| week 2026-45 | `2.2.8` → `2.4.5` | `listTestCases` | input_schema_changed (schema_other) | property 'folder_id' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `listTestIds` | input_schema_changed (schema_other) | property 'buildId' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `listTestPlans` | description_changed | length 652 -&gt; 325 |
| week 2026-45 | `2.2.8` → `2.4.5` | `listTestRuns` | description_changed | length 301 -&gt; 145 |
| week 2026-45 | `2.2.8` → `2.4.5` | `percyVisualTestIntegrationAgent` | description_changed | length 342 -&gt; 148 |
| week 2026-45 | `2.2.8` → `2.4.5` | `percyVisualTestIntegrationAgent` | input_schema_changed (schema_other) | property 'filePaths' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `prepareSelfHealingPlan` | description_changed | length 806 -&gt; 261 |
| week 2026-45 | `2.2.8` → `2.4.5` | `runAppLiveSession` | description_changed | length 183 -&gt; 185 |
| week 2026-45 | `2.2.8` → `2.4.5` | `runAppLiveSession` | input_schema_changed (schema_other) | property 'appPath' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `runAppTestsOnBrowserStack` | description_changed | length 297 -&gt; 139 |
| week 2026-45 | `2.2.8` → `2.4.5` | `runAppTestsOnBrowserStack` | input_schema_changed (schema_other) | property 'appPath' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `runBrowserLiveSession` | description_changed | length 55 -&gt; 186 |
| week 2026-45 | `2.2.8` → `2.4.5` | `runBrowserLiveSession` | input_schema_changed (schema_other) | property 'desiredBrowserVersion' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `runPercyScan` | input_schema_changed (schema_other) | property 'integrationType' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `searchCapability` | description_changed | length 2019 -&gt; 375 |
| week 2026-45 | `2.2.8` → `2.4.5` | `searchCapability` | input_schema_changed (schema_other) | property 'offset' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `setupBrowserStackAppAutomateTests` | description_changed | length 268 -&gt; 118 |
| week 2026-45 | `2.2.8` → `2.4.5` | `setupBrowserStackAppAutomateTests` | input_schema_changed (schema_other) | property 'accessibility' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `setupBrowserStackAutomateTests` | description_changed | length 328 -&gt; 136 |
| week 2026-45 | `2.2.8` → `2.4.5` | `setupBrowserStackAutomateTests` | input_schema_changed (schema_other) | property 'devices' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `startAccessibilityScan` | input_schema_changed (schema_other) | property 'wcagVersion' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `takeAppScreenshot` | description_changed | length 127 -&gt; 61 |
| week 2026-45 | `2.2.8` → `2.4.5` | `takeAppScreenshot` | input_schema_changed (schema_other) | property 'appPath' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `updateTestCase` | description_changed | length 501 -&gt; 154 |
| week 2026-45 | `2.2.8` → `2.4.5` | `updateTestCase` | input_schema_changed (schema_other) | property 'automation_status' changed (annotations/descriptions) |
| week 2026-45 | `2.2.8` → `2.4.5` | `updateTestRun` | description_changed | length 272 -&gt; 134 |
| week 2026-45 | `2.2.8` → `2.4.5` | `uploadProductRequirementFile` | description_changed | length 429 -&gt; 306 |


