# Methodology

**Methodology version: 1.0.0**. Every record stores `methodology_version`. If the definition of
any metric below changes, the version is bumped (semver: a changed definition is a minor bump, a
removed or re-scaled metric is a major bump), and the change is listed in the changelog at the end.

ToolCensus measures **published metadata only**: what a package says about itself on npm, and the
tool, prompt and resource definitions a server *advertises* when it starts up. It never calls a
tool. See [ETHICS.md](ETHICS.md) for the rules and how they are enforced in code.

---

## 1. Population (which servers are measured)

Implemented in `src/toolcensus/discovery/population.py`. The exact rule text is stored in every
`population.json`, along with the full list of selected and excluded packages and the reason for
each exclusion.

1. **Candidates** are the union of:
   - (a) every npm package with `transport: stdio` listed in the official MCP Registry
     (`GET https://registry.modelcontextprotocol.io/v0.1/servers?version=latest`, all pages);
   - (b) npm search results for `keywords:mcp-server`, `keywords:mcp`,
     `keywords:modelcontextprotocol` and the free text `mcp server` (up to 1,000 results per
     query). The free-text query is needed because several official reference servers declare no
     npm keywords.
2. A candidate is **kept** if its latest version:
   - declares a `bin` (so it can be launched as a stdio server), **and**
   - is registry-listed, **or** depends on an official TypeScript SDK package
     (`@modelcontextprotocol/sdk` for 1.x, `@modelcontextprotocol/server` for 2.x), **or** has the keyword
     `mcp-server`, **and**
   - its name does not match the library pattern
     `(sdk|client|types|framework|inspector|proxy|gateway|bridge|cli-core)` (registry-listed
     packages are exempt), **and**
   - it is not listed in `exclusions.yaml` (manual exclusions with a written reason).
3. Kept candidates are ranked by **npm weekly downloads** (npm downloads API, last week) and the
   top **N = 200** are measured (configurable with `discover --top`).

**Cost of a cold run:** the registry lists more than 11,000 npm stdio packages, about half of them
scoped. npm's bulk downloads endpoint only accepts unscoped names, so scoped names are looked up
one at a time under npm's rate limits (with `Retry-After` respected). A cold `discover` therefore
takes about 2 hours, which fits within the weekly job's budget. `discover --no-registry` (npm search
only) is a fast mode for local experiments. Its populations say so in `selection_rule` and are
**not** comparable with weekly populations.

**Bias:** the population is popularity-biased by design. It describes what most users actually
install, not the long tail.

## 2. Introspection

Implemented in `src/toolcensus/sandbox/` and `src/toolcensus/introspect/`.

1. **Install** (network on): a throwaway container from `node:22-slim`, pinned by digest, installs
   the exact package version into a fresh Docker volume with
   `npm install --omit=dev --ignore-scripts` (capabilities dropped, read-only root filesystem).
   Install scripts stay off unless a reviewed entry in `launch_overrides.yaml` turns them on, and
   records say whether they ran (`launch.install_scripts_ran`).
2. **Run** (network off): the package's `bin` is started with `node` from the volume, mounted
   read-only, inside a container with `--network none`, a read-only root filesystem (only a tmpfs
   at `/tmp` is writable), the image's unprivileged `node` user (uid 1000), `--cap-drop ALL`,
   `no-new-privileges`, 1 CPU, 512 MB of memory, 256 PIDs, and a 60 s wall-clock limit.
   Launch arguments come from `launch_overrides.yaml` if the package has an entry, otherwise from
   the literal `packageArguments` in its MCP Registry entry (for example `server start`),
   otherwise none. Records say which was used (`launch.source`: `override`, `registry`, `bin`).
3. **Cleanup:** the volume is deleted as soon as the server has been measured, whatever the
   outcome, and each run ends by sweeping any labelled leftovers (for example after Ctrl-C).
   Nothing a scan downloads stays on disk; `toolcensus clean` removes leftovers on demand.
4. **Environment:** no host variables are passed. If the MCP Registry lists required environment
   variables, they are set to the literal placeholder `toolcensus-placeholder-not-a-real-secret`.
   Their names are recorded in `launch.placeholder_env`.
5. **Handshake** (allowlisted client): `initialize` → `notifications/initialized` → `tools/list` →
   `prompts/list` and `resources/list` + `resources/templates/list` (only if the server declares
   those capabilities). `nextCursor` pagination is followed, up to 100 pages, and stops if a
   cursor repeats. The client offers protocol version `2025-11-25` and declares no capabilities.
   It declines every request the server sends to the client (sampling, roots, elicitation).
6. **Status** (exactly one per record):

| Status | Meaning |
|---|---|
| `ok` | Handshake completed and definitions were collected |
| `timeout` | No complete answer within the time limit; the container was killed |
| `crashed` | The process exited or closed stdout before answering |
| `requires_configuration` | The server did not start without configuration: stderr or an error response mentions missing keys/tokens/env, *or* it crashed after receiving placeholder values |
| `install_failed` | Package metadata or `npm install` failed |
| `not_mcp` | Nothing that looks like JSON-RPC was received (only non-JSON output), or the package declares no `bin` |

## 3. Normalization and hashing

Implemented in `src/toolcensus/normalize/`.

- Canonical form: **RFC 8785 JSON Canonicalization Scheme** (JCS), tested against the RFC's own
  test vectors.
- `tool_hash = sha256(JCS(full tool definition exactly as sent))`. The definition includes every
  field: name, title, description, inputSchema, outputSchema, annotations, `_meta` and any others.
- Component hashes: `description_hash`, `input_schema_hash`, `output_schema_hash`,
  `annotations_hash`. When a component is missing, its hash is the hash of JSON `null`.
- `surface_hash = sha256(JCS(sorted [[tool name, tool_hash], ...]))` for the whole server.
- Hashes are prefixed `sha256:`.

Key order and whitespace never change a hash. Any change to the content does.

## 4. Metrics

All metrics are computed per server-version and then aggregated across the population as counts,
percentages and medians (`src/toolcensus/metrics/aggregate.py`). Unless stated otherwise,
percentages of *tools* use every tool from servers with status `ok`, and percentages of
*packages* use every record that has npm metadata.

### 4.1 Supply-chain signals (`metrics/supply_chain.py`), source: npm registry packument

| Id | Definition | Limitations |
|---|---|---|
| `has_provenance` | `versions[v].dist.attestations.provenance` is an object | Provenance only shows *where* a package was built, not that the code is safe |
| `has_install_scripts` / `install_scripts` | `scripts` contains `preinstall`, `install` or `postinstall`; `gypfile: true` with no explicit `install` counts as `install(gypfile)` | Does not check what the script does |
| `direct_dependency_count` | Number of keys in `dependencies` | Transitive dependencies are not counted |
| `maintainer_count` | Length of `maintainers` (version-level, falling back to package-level) | npm maintainers ≠ people with commit access |
| `releases_last_90d` | Releases with a publish time in (as_of − 90 d, as_of] | `as_of` = scan time for weekly scans, the version's publish time for backfill |
| `median_days_between_releases` | Median gap between consecutive release times up to `as_of`; `null` with fewer than 2 releases | Includes pre-releases |
| `repo_linked` | `repository` is a string or `{url}` that matches a public forge URL (GitHub, GitLab, Bitbucket, Codeberg, sr.ht) or npm shorthand (`owner/repo`, `github:owner/repo`) | String check only; the URL is never fetched |
| `registry_listed` | The package appears as an npm stdio package in the official MCP Registry | The registry was in preview when this was written |

### 4.2 Tool-surface drift (`diff/engine.py`)

Two observations of the same package are compared only when **both** have status `ok`. Tools are
matched by name. Each difference becomes one or more change records:

| `change_type` | Rule |
|---|---|
| `tool_added` / `tool_removed` | Name present in only one observation |
| `description_changed` | `description_hash` differs |
| `input_schema_changed` | `input_schema_hash` differs; then sub-classified (below) |
| `output_schema_changed` | `output_schema_hash` differs |
| `annotations_changed` | `annotations_hash` differs |
| `other_changed` | `tool_hash` differs but none of the above (e.g. `title`, `_meta`) |

**Schema sub-classes** compare only the top level of the input schema:

- *widening signals:* a new **optional** property; a property no longer `required`; an `enum`
  constraint removed or values added; `additionalProperties: false` removed; a property's type
  set grows; `pattern` / `format` / `maxLength` / `minLength` / `minimum` / `maximum` /
  `minItems` / `maxItems` / `const` removed.
- *narrowing signals:* the reverse of the above, plus a property removed or a new **required**
  property added.
- `schema_widened`: only widening signals. `schema_narrowed`: only narrowing signals.
  `schema_other`: a mix of both, an incompatible type change, a changed constraint value, or a
  change that is only in nested descriptions.

**Drift without a version bump:** the version string is the same in two weekly scans but
`surface_hash` differs. This is reported as a separate, neutral statistic. Possible causes include
servers that build their tool lists dynamically.

**Aggregates:** `pct_servers_changed` = share of `ok` servers with at least one change record
compared with the previous week. Monthly figures and the distribution of change types are computed
from `changes.csv`.

### 4.3 Schema strictness (`metrics/schema.py`), per tool, top-level properties only

| Id | Definition |
|---|---|
| `has_input_schema` | `inputSchema` is an object |
| `declares_required` | `required` is a non-empty array |
| `additional_properties_false` | `additionalProperties` is exactly `false` |
| `typed_property_ratio` | Properties with an explicit `type` ÷ all properties (`null` with no properties) |
| `constrained_string_ratio` | String properties with any of `enum`, `const`, `pattern`, `format`, `maxLength` ÷ string properties (`null` with none) |
| `has_output_schema` | `outputSchema` is an object |

### 4.4 Tool annotations (`metrics/annotations.py`)

Annotation names were checked against the MCP specification (2025-03-26 through 2025-11-25):
`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

- `declared[h]`: hint `h` is present, whatever its value.
- `has_any`: at least one hint is present. Aggregated as `pct_tools_annotated` and
  `pct_servers_all_annotated` (servers with at least one tool, where every tool has a hint).
- **Heuristic, clearly labelled:** `side_effect_verb` is true when a token of the tool name
  (split on non-alphanumerics and camelCase) or the first word of the description (with a
  trailing `s` removed) is one of: add, append, archive, cancel, commit, create, delete, deploy,
  drop, edit, execute, exec, insert, install, kill, merge, modify, move, patch, post, publish,
  push, put, remove, rename, replace, restart, run, send, set, submit, terminate, trigger,
  uninstall, update, upload, upsert, write. `side_effect_unannotated` = `side_effect_verb` and
  neither `readOnlyHint` nor `destructiveHint` is declared. This is **only ever reported in
  aggregate**. It has known false positives (for example `run_query` for a read-only query) and
  false negatives (side-effecting verbs that are not in the list).

### 4.5 Description hygiene (`metrics/descriptions.py`), counts only

- `length`: number of characters in `description`.
- `invisible_char_count` and `invisible_categories`: code points counted by category:
  `zero_width` (U+200B–U+200D, U+2060, U+FEFF, U+180E), `bidi_control` (U+061C, U+200E/F,
  U+202A–U+202E, U+2066–U+2069), `tag` (U+E0000–U+E007F), `variation_selector` (U+FE00–U+FE0D,
  U+E0100–U+E01EF; the emoji selectors U+FE0E/F are excluded), `control` (Cc except tab, LF and
  CR), `other_format` (other Cf), `private_or_unassigned` (Co, Cn).
- `markup_tag_count`: matches of `</?[A-Za-z][A-Za-z0-9:-]*(\s[^<>]*)?/?>`.

No intent is inferred. **Public output never reproduces such text.** Any string in a definition
that contains these code points is replaced with a neutral placeholder in public records. The
original goes to the git-ignored `private/` directory for manual review (ETHICS.md rule 5).
Hashes and metrics are always computed on the original.

### 4.6 Authorization metadata (phase 2, remote servers, opt-in; `metrics/auth.py`)

One unauthenticated `GET` per remote endpoint per scan, to the RFC 9728 OAuth 2.0 Protected
Resource Metadata location that the MCP authorization specification references:
`https://host/.well-known/oauth-protected-resource{path}`. Recorded: whether a JSON document was
returned (`published`), the HTTP status, and which of `resource`, `authorization_servers`,
`scopes_supported` and `bearer_methods_supported` are present. No authentication is attempted.

## 5. Historical backfill and backtesting

- `backfill` introspects past npm versions published since a date (pre-releases skipped, at most
  N per package, oldest to newest) with the **same** sandbox and allowlist. The records are marked
  `observed_via: backfill` and keep the original `published_at`. Charts show backfilled history
  separately from live weekly observations.
- `backtest` compares the first affected version of each incident in `incidents/incidents.yaml`
  with the version before it. It records which neutral signals changed (tool-surface diffs,
  provenance loss, new install scripts, maintainer count, dependency count growth, repository link
  removed). A *hit* is not a detection claim. Misses are listed with their reason. Incidents
  marked `holdout` must not be used when designing metrics.

## 6. Known limitations

- Servers that need real credentials may not expose their tools without them. They are
  under-measured and reported as `requires_configuration`.
- Tool definitions can depend on environment and configuration. We measure the default behaviour
  in an empty, offline sandbox.
- Remote and hosted servers can change at any time. Weekly sampling misses changes within a week.
- Heuristic metrics (side-effect verbs) have false positives and false negatives.
- The sandbox image is a minimal Node.js image. Packages that need another runtime (for example
  Bun) or native system libraries it lacks (for example a bundled .NET binary that needs OpenSSL)
  cannot start and are reported as `crashed`. Servers that download their tool list from the
  internet at startup cannot do so offline and are reported the same way.
- Install scripts are disabled by default, so a few packages that need them may fail to start.
  They are reported as `crashed` or `install_failed`, not silently dropped.
- The population is popularity-biased by design.

## 7. Reproducibility

Every number in the report is regenerated from committed data with:

```bash
uv run toolcensus verify-data && uv run toolcensus dataset && uv run toolcensus report
```

## Changelog

- **1.0.0** (2026-10-24): initial definitions.
