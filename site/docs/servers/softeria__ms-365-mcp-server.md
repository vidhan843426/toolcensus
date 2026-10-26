# `@softeria/ms-365-mcp-server`

| | |
|---|---|
| Latest observed version | `0.173.0` |
| Status | ok |
| Weekly downloads | 18314 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.Softeria/ms-365-mcp-server |
| Surface hash | `sha256:d913f945df51a853` |

!!! tip "Improvement hints"
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 5 of 200 tools.
    - Consider `additionalProperties: false` on the input schema of 188 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 14 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 73 |
| `median_days_between_releases` | 0.44 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (200)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `accept-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8f605d7206af` |
| `add-calendar-event-attachment` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `d222660b929e` |
| `add-excel-table-rows` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5f11ca66b0d1` |
| `add-mail-attachment` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a45734ab2f65` |
| `cancel-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5fac70731011` |
| `clear-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ede583ad0f13` |
| `copy-drive-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `2333d0717d3c` |
| `copy-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `37c81428aa22` |
| `create-calendar` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `eda37fefba6c` |
| `create-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1d401a08b450` |
| `create-calendar-event-attachment-upload-session` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `34971e05f403` |
| `create-contact-child-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1b1b88fba65f` |
| `create-contact-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `9280ddcb3d62` |
| `create-contact-in-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `72706151bad1` |
| `create-draft-email` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b464bebdd005` |
| `create-drive-item-preview` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `2b646302abaf` |
| `create-drive-item-share-link` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6caf863fe9da` |
| `create-excel-chart` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ab01d80ccfd1` |
| `create-excel-table` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e7c45b3841d8` |
| `create-focused-inbox-override` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `388a9bcddb6b` |
| `create-forward-draft` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1f2963a47a33` |
| `create-mail-attachment-upload-session` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4a1a9eb8529d` |
| `create-mail-child-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `08bdd44cf5cc` |
| `create-mail-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `694161fdc7bb` |
| `create-mail-rule` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5c6e3690b652` |
| `create-my-calendar-permission` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `866c69be6598` |
| `create-onedrive-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5bd964ab9217` |
| `create-onenote-notebook` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `bea07f1847e9` |
| `create-onenote-page` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `fc4420d6dbf4` |
| `create-onenote-section` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `11aacc063779` |
| `create-onenote-section-page` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1b2a0817897f` |
| `create-outlook-category` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `edfb5748d110` |
| `create-outlook-contact` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `146837afa717` |
| `create-planner-bucket` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `cbd8f945cab5` |
| `create-planner-plan` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b7be39c3bfdd` |
| `create-planner-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `68a1a623705b` |
| `create-planner-task-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `525eacbdd3f9` |
| `create-reply-all-draft` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5c41c1fc0d6e` |
| `create-reply-draft` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `eea558a301a1` |
| `create-specific-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6dc82dd6db2e` |
| `create-subscription` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `04d55ddf66d3` |
| `create-todo-checklist-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8b1e64f5dfe8` |
| `create-todo-linked-resource` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `726d894a7970` |
| `create-todo-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `66833b216406` |
| `create-todo-task-list` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `88dec0112f53` |
| `create-upload-session` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6c53ca9745fd` |
| `decline-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8afaeb186be9` |
| `delete-calendar` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1b138305d510` |
| `delete-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `decec65cc215` |
| `delete-contact-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e17c87679b27` |
| `delete-drive-item-permission` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e1b0cf0a77e6` |
| `delete-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `eba25dee7b6c` |
| `delete-excel-table-row` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6b3872d9c015` |
| `delete-focused-inbox-override` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `cf1b5f13e1d5` |
| `delete-mail-attachment` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `50768e7a8ee9` |
| `delete-mail-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `3225f7faa2ef` |
| `delete-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1757b0da9c78` |
| `delete-mail-rule` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `592b4c745eb4` |
| `delete-my-calendar-permission` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `598218b90fe7` |
| `delete-onedrive-file` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c619a1244f46` |
| `delete-onenote-page` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8018e4b987cc` |
| `delete-outlook-contact` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c6ffa2043e74` |
| `delete-planner-bucket` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f68dd7afbe8f` |
| `delete-planner-task-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1ccf9f5228e0` |
| `delete-specific-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `308629a5d6e6` |
| `delete-subscription` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a3e46a13b164` |
| `delete-todo-checklist-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4dc97faf9718` |
| `delete-todo-linked-resource` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `3fa98ec1c4da` |
| `delete-todo-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4b7ff28b9dee` |
| `delete-todo-task-list` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `cd7c293b1210` |
| `dismiss-calendar-event-reminder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `9db8ce70868f` |
| `download-bytes` | openWorldHint, readOnlyHint | yes | yes | `6f1306f90389` |
| `download-bytes-to-file` | openWorldHint, readOnlyHint | yes | yes | `d1215956cfaf` |
| `format-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4dc6ae846303` |
| `format-excel-range-border` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `36c442ec90e8` |
| `format-excel-range-fill` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `08dbaab1adcb` |
| `format-excel-range-font` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1cd7bd4d5785` |
| `forward-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b6b9ecd382cd` |
| `forward-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `58054c434829` |
| `get-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `630047bfadac` |
| `get-calendar-view` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `50c508aa11c0` |
| `get-current-user` | destructiveHint, openWorldHint, readOnlyHint | no | no | `e1afe8c95a0e` |
| `get-download-url` | openWorldHint, readOnlyHint | yes | yes | `f5965a441a03` |
| `get-drive-delta` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `cd8e752037f4` |
| `get-drive-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b46bf0d18de2` |
| `get-drive-root-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `d18ede675c9f` |
| `get-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e07b6ffa01fe` |
| `get-excel-range-format` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `41aabd27ed2f` |
| `get-excel-table` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1a7176b69163` |
| `get-excel-used-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `eb27ee860f62` |
| `get-mail-attachment-content` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a5a471f24c80` |
| `get-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a913ae92d240` |
| `get-mail-message-mime` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `956131e1e73e` |
| `get-mail-tips` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e24e6317b7b8` |
| `get-mailbox-settings` | destructiveHint, openWorldHint, readOnlyHint | no | no | `f0a56b49f504` |
| `get-my-profile` | destructiveHint, openWorldHint, readOnlyHint | no | no | `2ba2757eb37d` |
| `get-onenote-page-content` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5a3eff6d5ce3` |
| `get-outlook-contact` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `334d7600bb30` |
| `get-planner-bucket` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4c01a20cd53e` |
| `get-planner-plan` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4c95d341aebc` |
| `get-planner-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `849b1e6b858c` |
| `get-planner-task-details` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1a1a37dea184` |
| `get-specific-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `140c59afd1ee` |
| `get-specific-calendar-view` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `40df3fc00f34` |
| `get-subscription` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `23667eb553c2` |
| `get-todo-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `610c7d87a1eb` |
| `get-upload-url` | openWorldHint, readOnlyHint | yes | yes | `45651e118fd8` |
| `graph-batch` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e44c44c5bb3d` |
| `insert-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `acf7d629b448` |
| `list-accounts` | openWorldHint, readOnlyHint | no | no | `44052c4d8712` |
| `list-all-onenote-sections` | destructiveHint, openWorldHint, readOnlyHint | no | no | `22d7041e01b1` |
| `list-calendar-event-instances` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `17f2e069f265` |
| `list-calendar-events` | destructiveHint, openWorldHint, readOnlyHint | no | no | `b1ef63db23e5` |
| `list-calendar-events-delta` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `481eba2acedd` |
| `list-calendar-view-delta` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ea86af8059d9` |
| `list-calendars` | destructiveHint, openWorldHint, readOnlyHint | no | no | `3082b1db4a83` |
| `list-contact-folder-child-folders` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `7a5b232347ac` |
| `list-contact-folder-contacts` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4bed46134e39` |
| `list-contact-folders` | destructiveHint, openWorldHint, readOnlyHint | no | no | `1297b04ce003` |
| `list-drive-item-permissions` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `049fa45ddca3` |
| `list-drive-item-thumbnails` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `30e87fe77c38` |
| `list-drive-item-versions` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `163bc6d3e2f0` |
| `list-drives` | destructiveHint, openWorldHint, readOnlyHint | no | no | `2c6d4ffcd83c` |
| `list-excel-table-rows` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `d8de4c5ad8a2` |
| `list-excel-tables` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `55a347150640` |
| `list-excel-worksheets` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `0cac231bea22` |
| `list-focused-inbox-overrides` | destructiveHint, openWorldHint, readOnlyHint | no | no | `054b36de2a23` |
| `list-folder-files` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `6e692e636a9c` |
| `list-group-planner-plans` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `52ff9458c0a3` |
| `list-mail-attachments` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f477ef20c015` |
| `list-mail-child-folders` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `811cd806133f` |
| `list-mail-folder-messages` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c0977fcf2d29` |
| `list-mail-folder-messages-delta` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `d0116d6604a0` |
| `list-mail-folders` | destructiveHint, openWorldHint, readOnlyHint | no | no | `782ad8729ed0` |
| `list-mail-messages` | destructiveHint, openWorldHint, readOnlyHint | no | no | `1a9c5eafc2c4` |
| `list-mail-rules` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8e21f690fa30` |
| `list-my-calendar-permissions` | destructiveHint, openWorldHint, readOnlyHint | no | no | `ab176f5bc76b` |
| `list-onenote-notebook-sections` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `13dae0d4103b` |
| `list-onenote-notebooks` | destructiveHint, openWorldHint, readOnlyHint | no | no | `70a6fc3c0de4` |
| `list-onenote-pages` | destructiveHint, openWorldHint, readOnlyHint | no | no | `119635871cf2` |
| `list-onenote-section-groups` | destructiveHint, openWorldHint, readOnlyHint | no | no | `932a4baab5cc` |
| `list-onenote-section-pages` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `bbb84f006c5f` |
| `list-outlook-categories` | destructiveHint, openWorldHint, readOnlyHint | no | no | `d92d243197dd` |
| `list-outlook-contacts` | destructiveHint, openWorldHint, readOnlyHint | no | no | `69f6881c6993` |
| `list-plan-buckets` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `58a065ea492a` |
| `list-plan-tasks` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `8d0875559606` |
| `list-planner-task-messages` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1ef564c17940` |
| `list-planner-tasks` | destructiveHint, openWorldHint, readOnlyHint | no | no | `7470820b88a7` |
| `list-specific-calendar-events` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1232ddc298b4` |
| `list-subscriptions` | destructiveHint, openWorldHint, readOnlyHint | no | no | `91580557dc80` |
| `list-supported-languages` | destructiveHint, openWorldHint, readOnlyHint | no | no | `c3ef51d80700` |
| `list-supported-time-zones` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `e3948de38012` |
| `list-todo-checklist-items` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `51c186ff7c7e` |
| `list-todo-linked-resources` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `dd68b9e833ab` |
| `list-todo-task-lists` | destructiveHint, openWorldHint, readOnlyHint | no | no | `5e71db8dd0cc` |
| `list-todo-tasks` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `cbddd65edf59` |
| `login` | — | no | yes | `85fcedc301b8` |
| `logout` | — | no | no | `107143ab6edb` |
| `merge-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ffe42846a064` |
| `move-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `57e28066ce13` |
| `move-rename-onedrive-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5259723d7213` |
| `parse-teams-url` | openWorldHint, readOnlyHint | yes | yes | `96e64fabbe8f` |
| `read-mail-text` | openWorldHint, readOnlyHint | no | yes | `e71380b5181e` |
| `reauthorize-subscription` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a1c6630b2056` |
| `remove-account` | — | yes | yes | `0b874ec34913` |
| `reply-all-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1d4bddc35010` |
| `reply-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `28239c5a715f` |
| `search-onedrive-files` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `46e21c1c9b34` |
| `select-account` | — | yes | yes | `81f88b9ee46b` |
| `send-draft-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `2847b473a8b4` |
| `send-mail` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `126009fc2bd5` |
| `share-drive-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ee15fe3678cd` |
| `snooze-calendar-event-reminder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f69cf07fd107` |
| `sort-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `52a0f9f66140` |
| `tentatively-accept-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ee5b0046248a` |
| `unmerge-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f61e503285d9` |
| `update-calendar` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `54e492c8b23a` |
| `update-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `a14174ba81d7` |
| `update-contact-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `9c2c219bbee9` |
| `update-excel-range` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `22bbb7e4cfd6` |
| `update-excel-table-row` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `4fcc55f22822` |
| `update-focused-inbox-override` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `d0ad1870f7da` |
| `update-mail-folder` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `abb8cf8fc2a1` |
| `update-mail-message` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `3a7672158de6` |
| `update-mail-rule` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1811fa73936a` |
| `update-mailbox-settings` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f363fd6ec0d8` |
| `update-my-calendar-permission` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `ac6fd9fd1a5f` |
| `update-outlook-contact` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `56a9f6fb1c5d` |
| `update-planner-bucket` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `f97395ef9665` |
| `update-planner-plan` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `b514c423da48` |
| `update-planner-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `89b862c67166` |
| `update-planner-task-details` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `5a7517247846` |
| `update-specific-calendar-event` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `9787a77a9b1e` |
| `update-subscription` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `2c3e50445a94` |
| `update-todo-checklist-item` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c8d58a4a1833` |
| `update-todo-task` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `c1950b6e533a` |
| `update-todo-task-list` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `1734a09d5e68` |
| `upload-file-content` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `0e2362f06ff5` |
| `upload-my-profile-photo` | destructiveHint, openWorldHint, readOnlyHint | yes | no | `24ee60948f5a` |
| `verify-login` | — | no | no | `d9611e2b42e6` |



## Change history

| Observed | Version | Tool | Change | Details |
|---|---|---|---|---|
| week 2026-44 | `0.171.0` → `0.173.0` | `get-upload-url` | description_changed | length 738 -&gt; 850 |
| week 2026-44 | `0.171.0` → `0.173.0` | `get-upload-url` | input_schema_changed (schema_widened) | property 'contentId' added (optional) |


