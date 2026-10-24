# Verification notes (2026-10-24)

What the build spec asked us to *verify* before relying on it, and what we found.

## MCP Python SDK (`mcp` on PyPI)

- Current version: **2.3.0** (requires Python ≥ 3.10).
- `ClientSession` (in `mcp.client.session`) negotiates handshake versions
  `2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`. It also knows the "modern" `2026-07-28`
  protocol, and for that protocol it **drops tools whose `x-mcp-header` annotations are invalid**
  (`ClientSession._absorb_tool_listing`) and re-validates results into typed models.
- **Decision:** our measurement client (`introspect/client.py`) is a small newline-delimited
  JSON-RPC client over stdio rather than `ClientSession`. Reasons:
  1. *Fidelity:* we must hash definitions exactly as sent. The SDK filters and normalizes them.
  2. *Auditability of the allowlist:* every outgoing message passes through one ~10-line choke
     point. The client has no `call_tool` code path at all.
- The SDK is still a dependency. Tests use it to (a) list every client method defined in
  `mcp.types.ClientRequest` / `ClientNotification` and prove each non-allowlisted one is
  blocked, and (b) run a fixture server built with `mcp.server.MCPServer` to prove interop.
- We offer protocol version `2025-11-25` in `initialize`. Servers negotiate down.

## MCP spec: tool annotations

`ToolAnnotations` fields: `title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`,
`openWorldHint`. Checked against the SDK's generated types (`read_only_hint` etc., serialized in
camelCase). Unchanged from 2025-03-26 through 2025-11-25.

## MCP spec: authorization discovery

The MCP authorization spec relies on **RFC 9728 OAuth 2.0 Protected Resource Metadata**. Its
location is `/.well-known/oauth-protected-resource`, inserted between the host and the path of the
resource URL. Implemented in `metrics/auth.py` (phase 2, opt-in).

## Official MCP Registry API

- Base: `https://registry.modelcontextprotocol.io`. OpenAPI at `/openapi.yaml`. Both `/v0` and
  `/v0.1` exist. We use **`/v0.1/servers`**.
- Query parameters: `cursor`, `limit`, `search` (substring of the name), `updated_since`
  (RFC 3339), `version` (`latest` or an exact version), `include_deleted`.
- Response: `{"servers": [{"server": {...}, "_meta": {"io.modelcontextprotocol.registry/official": {...}}}],
  "metadata": {"nextCursor": "...", "count": N}}`.
- `server.packages[]` entries carry `registryType` (`npm`, `pypi`, ...), `identifier`, `version`,
  `runtimeHint`, `transport.type` (`stdio`, ...) and `environmentVariables[]` with `isRequired`.
  `server.remotes[]` carry `type` (`streamable-http`, `sse`) and `url`.
- Server JSON schema version seen: `2025-12-11`.

## npm

- Packument: `GET https://registry.npmjs.org/<name>` (scoped names encoded as `@scope%2Fname`).
- **Provenance:** `versions[v].dist.attestations = {"url": ".../-/npm/v1/attestations/<pkg>@<v>",
  "provenance": {"predicateType": "https://slsa.dev/provenance/v1"}}`. Seen on
  `@modelcontextprotocol/server-filesystem@2.0.0`.
- Unpublished packages: the packument has `time.unpublished` and no `versions`. Example:
  `postmark-mcp`, unpublished on 2025-09-25.
- Downloads: `GET https://api.npmjs.org/downloads/point/last-week/<name>` →
  `{"downloads": N, "start", "end", "package"}`.
- Search: `GET https://registry.npmjs.org/-/v1/search?text=...&size<=250&from=N`. Each object
  includes `downloads.weekly` / `downloads.monthly`.
- Official TypeScript SDK: 1.x is the single package `@modelcontextprotocol/sdk`. **2.x is split**
  into `@modelcontextprotocol/server`, `/client`, `/core`, `/node`, `/express`, `/hono` and
  `/fastify`. Reference servers such as `server-filesystem@2.0.0` depend on
  `@modelcontextprotocol/server` and declare **no npm keywords**. Population discovery checks both
  SDK generations and adds a free-text `mcp server` search for this reason.

## Base image

`node:22-slim` resolved to
`sha256:de170b39439eb0e5a3444ad7d60b015614a381e10fecae2e30ec9e735122f38d` with
`docker buildx imagetools inspect`. Update deliberately and record the change.

## SARIF

Output follows SARIF 2.1.0 (`$schema: https://json.schemastore.org/sarif-2.1.0.json`). GitHub
code scanning requires a `physicalLocation.artifactLocation.uri` on each result. We point it at
the snapshot/record file that was compared.

## GitHub Actions pins (resolved with `git ls-remote`)

| Action | Tag | SHA |
|---|---|---|
| actions/checkout | v7.0.1 | 3d3c42e5aac5ba805825da76410c181273ba90b1 |
| actions/upload-artifact | v7.0.2 | cf430e030ddbb5b0abf93d22962f4752f3646cd9 |
| actions/download-artifact | v8.0.2 | 9000827ccba6bdab643e8b6fd33ac0654aef8333 |
| astral-sh/setup-uv | v10.3.2 | 07a047e608db84b3d8c06cd9a7c7dcc9c355c18e |
| actions/configure-pages | v6.0.0 | 45bfe0192ca1faeb007ade9deae92b16b8254a0d |
| actions/upload-pages-artifact | v5.0.0 | fc324d3547104276b827a68afc52ff2a11cc49c9 |
| actions/deploy-pages | v5.0.1 | 368f82528645a54fb793d4d04e342629a3f51346 |

## Incidents

Version ranges in `incidents/incidents.yaml` come from the GitHub Advisory Database API
(`GHSA-q66q-fx2p-7w4m`, `GHSA-hc55-p739-j48w`, `GHSA-6xpm-ggf7-wc3p`) and the npm registry
(publish times, and the unpublish record for `postmark-mcp`). The `postmark-mcp` entry has no
GitHub advisory, so a maintainer should review its description against the public reporting
before the first backtest is published.
