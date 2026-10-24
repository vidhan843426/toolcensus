# Contributing

Thanks for helping. Please read [ETHICS.md](ETHICS.md) first: contributions that add active
probing, tool invocation or per-project "scores" will not be accepted.

## Setup

```bash
uv sync
uv run pre-commit install
```

## Checks (the same ones CI runs)

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest --cov            # unit tests, coverage ≥ 85 %
uv run pytest -m sandbox       # integration tests, needs Docker
uv run toolcensus schemas --check
uv run toolcensus verify-data
```

## Changing a metric

1. Update the code and its tests.
2. Update the definition in `METHODOLOGY.md`.
3. Bump `METHODOLOGY_VERSION` in `src/toolcensus/__init__.py` and add a changelog entry.
4. If a record shape changed, bump `SCHEMA_VERSION` and run `uv run toolcensus schemas`.

## Population exclusions and launch overrides

- `exclusions.yaml`: packages that match the selection rule but are not servers (SDKs,
  frameworks). Always give a `reason`.
- `launch_overrides.yaml`: per-package `bin`, `args` and **placeholder-only** `env`. Real values
  are rejected in code. `allow_install_scripts: true` needs a reviewer to sign off.

## Incidents

Only add incidents that are public and already disclosed or resolved, with public references and a
neutral one-line description. No exploit details. Mark roughly half as `split: holdout`.
