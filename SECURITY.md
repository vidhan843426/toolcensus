# Security policy

## Reporting a problem with ToolCensus itself

Examples: a way for a measured package to escape the sandbox, a way to make the client send a
non-allowlisted message, or data appearing in public output that should have been routed to
`private/`.

Please **do not open a public issue**. Use GitHub's private vulnerability reporting
(**Security → Report a vulnerability**) on this repository. We aim to reply within 7 days.

## Reporting a problem in an MCP server we measure

ToolCensus does not handle vulnerability reports for third-party packages. Please report them
privately to:

1. the package maintainer (their `SECURITY.md` or a private GitHub advisory),
2. npm, for malicious packages: <https://www.npmjs.com/support> → "Report malware",
3. the official MCP Registry maintainers, if the server is listed there.

If our own analysis surfaces something like this, we follow the same route and publish nothing
about the specific package until it has been resolved (see [ETHICS.md](ETHICS.md), rule 5).

## Supported versions

Only the latest release receives fixes.
