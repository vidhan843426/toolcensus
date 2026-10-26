# `brightspace-mcp-server`

| | |
|---|---|
| Latest observed version | `5.1.23` |
| Status | ok |
| Weekly downloads | 7087 |
| Protocol version | 2025-11-25 |
| Registry entry | io.github.RohanMuppa/brightspace |
| Surface hash | `sha256:1e3c6bc8328d8204` |

!!! tip "Improvement hints"
    - Consider whether the install-time script(s) (postinstall) are necessary; many users install with `--ignore-scripts`.
    - Consider adding tool annotations (`readOnlyHint`, `destructiveHint`, ...) to 3 of 26 tools.
    - Consider `additionalProperties: false` on the input schema of 24 tool(s) so unexpected arguments are rejected.



## Supply-chain signals

| Signal | Value |
|---|---|
| `has_provenance` | True |
| `has_install_scripts` | True |
| `install_scripts` | ['postinstall'] |
| `direct_dependency_count` | 10 |
| `maintainer_count` | 1 |
| `releases_last_90d` | 175 |
| `median_days_between_releases` | 0.04 |
| `repo_linked` | True |
| `registry_listed` | True |



## Tools (26)

| Tool | Annotations | Required declared | additionalProperties false | Tool hash |
|---|---|---|---|---|
| `download_dropbox_submission_file` | — | yes | no | `2d7b0afd26dd` |
| `download_file` | — | yes | no | `5959b9056232` |
| `get_announcement_files` | readOnlyHint | yes | no | `4f79728fc5e1` |
| `get_announcements` | readOnlyHint | no | no | `cf6810f88ca6` |
| `get_assignment_files` | readOnlyHint | yes | no | `f841a63a36ad` |
| `get_assignment_rubric` | readOnlyHint | yes | no | `7ab46a041c0e` |
| `get_assignments` | readOnlyHint | no | no | `c014ab6c138c` |
| `get_calendar_events` | readOnlyHint | no | no | `59e966043a82` |
| `get_classlist_emails` | readOnlyHint | yes | no | `54a780571980` |
| `get_course_content` | readOnlyHint | yes | no | `146379e72274` |
| `get_discussions` | readOnlyHint | yes | no | `6afc20138094` |
| `get_dropbox_feedback` | readOnlyHint | yes | no | `7ab46c735558` |
| `get_dropbox_folders` | readOnlyHint | yes | no | `b4058328f5a5` |
| `get_dropbox_submissions` | readOnlyHint | yes | no | `8fc4ed5ca979` |
| `get_dropbox_user_submissions` | readOnlyHint | yes | no | `c0bd3e6ba838` |
| `get_my_courses` | readOnlyHint | no | no | `af4ce153c507` |
| `get_my_grades` | readOnlyHint | no | no | `a8ecc602c908` |
| `get_my_groups` | readOnlyHint | yes | no | `bf265b4d2604` |
| `get_roster` | readOnlyHint | yes | no | `7cda7058c9ed` |
| `get_rubrics_for_object` | readOnlyHint | yes | no | `1fea481182ec` |
| `get_server_info` | readOnlyHint | no | no | `76d0e9d357cc` |
| `get_syllabus` | — | yes | no | `af9a30d8f275` |
| `get_upcoming_due_dates` | readOnlyHint | no | no | `acdc2e142c7c` |
| `get_video_transcript` | readOnlyHint | no | no | `988ccef19964` |
| `search_course` | readOnlyHint | yes | no | `c84d12422ca2` |
| `sign_out` | destructiveHint, idempotentHint, openWorldHint, readOnlyHint | no | no | `80f0140ee0ed` |



## Change history

No tool-definition changes observed.
