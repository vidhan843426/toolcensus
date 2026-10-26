# ToolCensus — MCP ecosystem health report

*Week 2026-44 · methodology v1.0.0 · 200 servers measured*

ToolCensus measures the **published metadata** of popular public MCP servers every week:
supply-chain signals, how precisely tools are described, annotation adoption and how tool
definitions change over time. These are neutral measurements, not security verdicts.

## Headline numbers

| Metric | This week |
|---|---|
| Servers measured | 200 |
| Reached status `ok` | 46.5% |
| Tools measured | 3388 |
| Packages with npm provenance | 57.5% |
| Packages with install scripts | 12.5% |
| Tools declaring any annotation | 64.0% |
| Servers with all tools annotated | 55.9% |
| Tools with `additionalProperties: false` | 38.1% |
| Tools with non-printing code points | 0.0% |
| Servers with a tool change vs previous week | 7.5% |


## Trends

![Servers measured](assets/charts/servers_measured.svg)
![% packages with npm provenance](assets/charts/pct_provenance.svg)
![% packages with install scripts](assets/charts/pct_install_scripts.svg)
![% tools annotated](assets/charts/pct_tools_annotated.svg)
![% servers with a tool change (week over week)](assets/charts/pct_servers_changed.svg)


See [Ecosystem trends](trends.md) for every metric, [Servers](servers/index.md) for per-server
pages, and [Download](download.md) for the open dataset.
