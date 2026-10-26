# `@postman/postman-mcp-server`

| | |
|---|---|
| Latest observed version | `2.14.0` |
| Status | ok |
| Weekly downloads | 7080 |
| Protocol version | 2025-11-25 |
| Registry entry | com.postman/postman-mcp-server |
| Surface hash | `sha256:422fb9c7eefd1b0c` |

!!! tip "Improvement hints"
    - Consider whether the install-time script(s) (preinstall) are necessary; many users install with `--ignore-scripts`.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | True |
| `install_scripts` | ['preinstall'] |
| `direct_dependency_count` | 6 |
| `maintainer_count` | 3 |
| `releases_last_90d` | 6 |
| `median_days_between_releases` | 4.31 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (42)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `createCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `c8db8848b5a5` |
| `createCollectionRequest` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ad5021e5e584` |
| `createCollectionResponse` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `bc2f5f81de0b` |
| `createEnvironment` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `9f790bc181eb` |
| `createMock` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `874ec25d93eb` |
| `createSpec` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `00b4a0ab25d4` |
| `createSpecFile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `3e6fb66563ce` |
| `createWorkspace` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `70c7b98b2a1d` |
| `duplicateCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `a69c1a877858` |
| `generateCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `17b30d76283f` |
| `generateSpecFromCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `7e5ff87ed101` |
| `getAllSpecs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `03a954de65e2` |
| `getAuthenticatedUser` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `8d07ca34d99f` |
| `getCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `83b1bf23095c` |
| `getCollections` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ffe68e91a76f` |
| `getDuplicateCollectionTaskStatus` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `1f7e533ded0b` |
| `getEnabledTools` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `87dc5089626e` |
| `getEnvironment` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `63a3aa70afe3` |
| `getEnvironments` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `b2d359d77ec9` |
| `getGeneratedCollectionSpecs` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `f23d957d5956` |
| `getMock` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `020cbcc782f7` |
| `getMocks` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `ff1179aeb8e5` |
| `getSpec` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8b354ebb0fb7` |
| `getSpecCollections` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `ecd70d90b1e4` |
| `getSpecDefinition` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `abd9f0c80f14` |
| `getSpecFile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `71a2d6ae43e0` |
| `getSpecFiles` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4e15b1e66737` |
| `getTaggedEntities` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `5c8e9b1d23d8` |
| `getWorkspace` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `932333161a29` |
| `getWorkspaces` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `1929519b28d9` |
| `publishMock` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8e6584e4d1ee` |
| `putCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `9955ecf41c0d` |
| `putEnvironment` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `e024d5b06a4b` |
| `runCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `12b48ff6d18d` |
| `searchPostmanElements` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | yes | `7935e15e678d` |
| `syncCollectionWithSpec` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `5fb05625ba16` |
| `syncSpecWithCollection` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `55b0a41bc0f0` |
| `updateCollectionRequest` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `dea739f4b82c` |
| `updateMock` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `fe04a6479055` |
| `updateSpecFile` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `8bd44bc18aa2` |
| `updateSpecProperties` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `4a089a809d54` |
| `updateWorkspace` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | yes | yes | `e4c319b6a003` |



## Change history

No tool-definition changes observed.
