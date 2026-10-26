# Ethics and safety ground rules

ToolCensus is a **measurement** project. These rules are hard requirements, and each one names the
code that enforces it and the test that proves it.

| # | Rule | Enforced in | Proven by |
|---|---|---|---|
| 1 | **Metadata only.** The only MCP messages ever sent are `initialize`, `notifications/initialized`, `tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`. | `introspect/client.py`: every outgoing message passes through one choke point that checks `ALLOWED_METHODS`. The client has no `call_tool` method. It declines every request the server sends to the client. | `tests/test_client_allowlist.py` (tries `tools/call` and every other method defined in the official SDK) and `tests/test_collect.py::test_only_allowlisted_methods_reach_the_server` (records what actually crossed the wire) |
| 2 | **Sandbox every third-party server.** Install with network in a separate build step; run with `--network none`, a read-only rootfs plus tmpfs, a non-root user, `--cap-drop ALL`, `no-new-privileges`, CPU/memory/PID limits and a hard timeout. No secrets: only obviously fake placeholders. | `sandbox/docker.py`, `sandbox/runner.py` (`LaunchSpec` rejects any env value that is not a placeholder, and any unsafe name, version, path or argument), `introspect/collect.py` (an almost-empty environment by default; the container is killed on timeout) | `tests/test_sandbox.py`, including integration tests that an outbound connection fails, that the rootfs is read-only and the user is non-root, and that a timeout removes the container |
| 3 | **Remote servers (phase 2, opt-in):** one GET of a public discovery document per server per scan, an identifying User-Agent, rate limits, caching. No authentication attempts, no brute forcing, no crawling. | `metrics/auth.py`, `discovery/http.py` | `tests/test_discovery.py` |
| 4 | **Respect upstream services.** Official public APIs only, a SQLite cache with conditional requests, per-host rate limiting, honouring `Retry-After`, exponential backoff, conservative defaults (`TOOLCENSUS_MIN_INTERVAL`). | `discovery/http.py` | `tests/test_discovery.py::test_cache_conditional_and_retry_after` |
| 5 | **Responsible disclosure.** Anything that may need private handling is written only to the git-ignored `private/` directory. Public output carries aggregate statistics only. | `privacy.py` (refuses to write under `data/`, `site/`, `reports/`, `schemas/`), `metrics/descriptions.py::redact_invisible` | `tests/test_cli_report.py::test_report_build_and_no_private_leak` |
| 6 | **Neutral language.** Facts, never accusations. No grades, scores or "unsafe" labels. | Report templates and `report/hints.py` ("Consider …") | Review |
| 7 | **Secure CI.** The job that runs untrusted packages has no write token and no secrets. A separate job only validates and commits data. `permissions: {}` at the top level; third-party actions pinned by commit SHA. | `.github/workflows/weekly-scan.yml` | Workflow review |

## What we will never do

- Call tools, read resources, fetch prompts, or otherwise run a server's functionality.
- Fuzz, probe, exploit or craft malicious input for any server.
- Scan private, authenticated or non-public servers.
- Publish a "security score" or call any project malicious or unsafe.

## If the analysis surfaces a possible vulnerability

1. Nothing about the specific package is published. The details stay in `private/`.
2. A maintainer reviews it by hand.
3. It is reported privately to the package maintainer (security policy or private advisory), to
   npm (<https://www.npmjs.com/support>, "Report malware"), and, if the package is listed there,
   to the MCP Registry maintainers.
4. It can be mentioned publicly only after it has been resolved or disclosed by the maintainer,
   and then only with neutral wording and public references (see `incidents/incidents.yaml`).

See [SECURITY.md](SECURITY.md) to report a problem *with ToolCensus itself*.
