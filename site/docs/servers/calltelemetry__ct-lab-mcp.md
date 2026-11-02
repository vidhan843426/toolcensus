# `@calltelemetry/ct-lab-mcp`

| | |
|---|---|
| Latest observed version | `0.8.184` |
| Status | ok |
| Weekly downloads | 14224 |
| Protocol version | 2025-11-25 |
| Registry entry | not listed |
| Surface hash | `sha256:c9d379ba2a49caeb` |

!!! tip "Improvement hints"
    - Consider publishing from CI with npm provenance (`npm publish --provenance`).
    - Consider listing the server in the official MCP Registry.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 121 of 122 tools.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | False |
| `has_install_scripts` | False |
| `install_scripts` | — |
| `direct_dependency_count` | 12 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 216 |
| `median_days_between_releases` | 0.06 |
| `repo_linked` | True |
| `registry_listed` | False |



## Tools (122)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `appliance_candidate_retire` | — | yes | yes | `c769f5c609b8` |
| `appliance_candidate_update` | — | yes | yes | `c6fc206dbc35` |
| `appliance_exec` | — | no | yes | `66cc60169327` |
| `appliance_update` | — | yes | yes | `49c61ec8d6d0` |
| `apply_license` | — | yes | yes | `2de9ba408fc6` |
| `apply_manifest` | — | no | yes | `cd6f05e214f9` |
| `auto_provision_vm` | — | no | yes | `28baee0cd05f` |
| `build_stig_template` | — | yes | yes | `c9718e854a0e` |
| `claim_cube` | — | yes | yes | `11633d84a37e` |
| `claim_slot` | — | no | yes | `6c15b3bd03d2` |
| `claimed_import_ova` | — | yes | yes | `a4083a69597a` |
| `claimed_import_qcow` | — | yes | yes | `6492dd19997d` |
| `clean_storage` | — | yes | yes | `6593075c1781` |
| `cleanup_expired_vms` | — | no | yes | `d18a9a37f182` |
| `collect_stig_evidence` | — | yes | yes | `bdf8e7b92733` |
| `create_appliance_claim` | — | no | yes | `6debccf0c34c` |
| `create_environment_claim` | — | yes | yes | `83149af05157` |
| `create_environment_cube_config_operation` | — | yes | yes | `996d34502ff1` |
| `create_snapshot` | — | yes | yes | `108a6db993a1` |
| `create_stig_claim` | — | yes | yes | `b8767aa9e66c` |
| `credential_status` | — | no | yes | `f2037b288d74` |
| `cube_claim` | — | no | yes | `fbd07e68ab29` |
| `cube_config` | — | yes | yes | `f4ad450697e4` |
| `cube_dialpeer_apply` | — | yes | yes | `1b3324120895` |
| `cube_dialpeer_show` | — | yes | yes | `09d815bbdc7c` |
| `cube_exec` | — | yes | yes | `cfd96ffe0fda` |
| `cube_ios_snapshot` | — | yes | yes | `61b937a42697` |
| `cube_list` | — | no | no | `141bb7f50612` |
| `cube_status` | — | yes | yes | `e0c1ddadb5a0` |
| `cube_xcc_enable` | — | yes | yes | `4750e1dac41c` |
| `cube_xcc_status` | — | yes | yes | `be673879900b` |
| `delete_appliance_claim` | — | yes | yes | `581d38f868e5` |
| `delete_manifest` | — | yes | yes | `37dc2d3134e0` |
| `diff_environment_cube_config_revisions` | — | yes | yes | `cac4cb3489c9` |
| `environment_ssh_file` | — | no | no | `f3115ebb760e` |
| `environment_ssh_session` | — | no | no | `6adea77fc5e5` |
| `factory_reset_appliance` | — | yes | yes | `fe41d1df75fe` |
| `ferrum_fleet_metrics` | — | no | yes | `1ff4c0da0277` |
| `find_slot` | — | no | yes | `fcd847c91720` |
| `fleet_candidates` | — | yes | yes | `19a2273ce1ca` |
| `fleet_group` | — | yes | yes | `44d0021c089f` |
| `fleet_versions` | — | no | yes | `81a6739703e1` |
| `get_appliance_claim` | — | yes | yes | `55fbe3ed1fe6` |
| `get_appliance_diagnostics` | — | yes | yes | `fe37bc3c8d44` |
| `get_appliance_id` | — | yes | yes | `6538dc196535` |
| `get_appliance_import_operation` | — | yes | yes | `d00aef31ed5b` |
| `get_environment_claim` | — | yes | yes | `6f941f4a52c5` |
| `get_environment_cube_config_revision` | — | yes | yes | `bb4621b97192` |
| `get_environment_operation` | — | yes | yes | `8b731e5d77f4` |
| `get_guest_agent_status` | — | yes | yes | `4c34f6b12da4` |
| `get_manifest` | — | yes | yes | `d5c099d1ab00` |
| `get_sip_trunk_status` | — | yes | yes | `635d8d003481` |
| `get_stig_receipt` | — | yes | yes | `bdfb78573753` |
| `get_template_mirror_status` | — | no | yes | `fb1998c068ba` |
| `get_vm_storage` | — | no | yes | `9fdba6d48326` |
| `host_maintenance_shutdown` | — | yes | yes | `81e56563851d` |
| `host_migrate_vm` | — | yes | yes | `cecac86a03f5` |
| `lab_capacity` | — | no | yes | `91f0bb03932a` |
| `lab_dev` | — | yes | yes | `2b2deee26601` |
| `lab_host_cert` | — | no | yes | `4c213c1e4d91` |
| `lab_host_key_enroll` | — | no | yes | `0d6fb424bab3` |
| `lab_mission` | — | yes | yes | `4c723c26dad0` |
| `lab_preflight` | — | yes | yes | `086359881ee6` |
| `lab_ssh` | — | yes | yes | `4d08845e5f7e` |
| `list_appliance_claims` | — | no | yes | `b0c914c4518f` |
| `list_cubes` | — | no | yes | `b78a04bfdfed` |
| `list_environment_claims` | — | no | no | `572a354a0d96` |
| `list_environment_cube_config_revisions` | — | yes | yes | `250f39876b63` |
| `list_expired_vms` | — | no | yes | `4a2e08227588` |
| `list_held_claims` | — | no | yes | `e51418ca4df8` |
| `list_hosts` | — | no | yes | `265570d282d4` |
| `list_inventory` | — | no | yes | `cf07f57ea2e1` |
| `list_manifests` | — | no | no | `f9fa381b4968` |
| `list_slots` | — | no | yes | `b34d6de69ada` |
| `list_snapshots` | — | no | yes | `ede9ff63befe` |
| `list_storage` | — | no | yes | `a873d2e6e078` |
| `manage_mcp_server` | — | no | yes | `716a0634505d` |
| `manage_vm_network` | — | yes | yes | `546d4453c40d` |
| `mount_iso` | — | yes | yes | `5658e4325deb` |
| `pause_appliance_claim` | — | yes | yes | `bc2ede1a99f6` |
| `pin_pool_slots` | — | yes | yes | `c94debb0ef2d` |
| `provision_cube` | — | no | yes | `5360dde22eea` |
| `provision_cucm_trunk` | — | yes | yes | `8faf7b530186` |
| `provision_vm` | — | no | yes | `8220c2bf3bc0` |
| `proxmox_import_qcow` | — | yes | yes | `e2e16b9d66e7` |
| `proxmox_quick_provision` | — | yes | yes | `6496a94b9c52` |
| `prune_untracked_vms` | — | no | yes | `f70a4e252278` |
| `publish_stig_template` | — | yes | yes | `51a0b5982852` |
| `purge_and_redeploy` | — | no | yes | `d8c47b71188f` |
| `purge_slots` | — | no | yes | `2bb95e3e527a` |
| `reboot_environment_instance` | — | yes | yes | `ebe003d4560b` |
| `release_appliance_claim_without_destroy` | — | yes | yes | `520f76452bb7` |
| `release_cube` | — | yes | yes | `1fafb91537d4` |
| `release_environment_claim` | — | yes | yes | `b2ef8eea79ff` |
| `release_slot` | — | no | yes | `bf26aa1c787e` |
| `release_stig_template` | — | yes | yes | `18615638d20f` |
| `renew_appliance_claim` | — | yes | yes | `681d1fab885d` |
| `renew_environment_claim` | — | yes | yes | `bb1b095de3f3` |
| `renew_license` | — | yes | yes | `f7b64cef6a42` |
| `renew_manifest` | — | yes | yes | `f7c9888f44a2` |
| `replicate_cube_template` | — | yes | yes | `2b964f9d3e07` |
| `revalidate_appliance_claim_network` | — | yes | yes | `7c0aee85c97f` |
| `rollback_snapshot` | — | yes | yes | `9982cb13c43d` |
| `sandbox_clone` | — | yes | yes | `9c3919d1b7d6` |
| `sandbox_reset` | — | yes | yes | `4c7db9fc3626` |
| `setup_cucm_emulator` | — | no | yes | `83d5e5774a64` |
| `sideload_appliance_runner` | — | yes | yes | `65b3590f3eb1` |
| `sideload_license` | — | yes | yes | `a67f90239991` |
| `signal_claim_owner_terminal` | destructiveHint, readOnlyHint | yes | yes | `208e533e32ee` |
| `sync_stig_template` | — | yes | yes | `7dfbe4cbea0e` |
| `trigger_template_mirror_sync` | — | yes | yes | `f3f440ae9f82` |
| `uat_access` | — | yes | yes | `eee7b22c4a93` |
| `uat_credential` | — | no | yes | `52faae91d4f3` |
| `uc_fixture_object_read` | — | yes | yes | `2f1afc7d46db` |
| `unmount_iso` | — | no | yes | `6e5f89bdb226` |
| `update_appliance_cli` | — | yes | yes | `c3575395d402` |
| `validate_stig_claim` | — | yes | yes | `2f107a4b03c7` |
| `verify_appliance_demo` | — | yes | yes | `ece312bbe3be` |
| `vm_action` | — | yes | yes | `9c3392a8a7bc` |
| `vm_renew` | — | no | yes | `68479933c5e2` |
| `vm_repair` | — | yes | yes | `a5bff26b9819` |
| `vm_transfer` | — | no | yes | `6935534823eb` |



## Change history

No tool-definition changes observed.
