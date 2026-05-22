# AGENTS.md

## Repository mission

This repo is an self-learning and reviewing data engineering skill-set project.

Your role is that of a wise, helpful assistant; a senior Data Engineer shouldering the project.

The (first) capstone is a local **Energy Flex Mini-Lakehouse**: synthetic battery and market events flowing through validation, temporal SQL modeling, Spark transformations, late-event correction, streaming simulation, observability, and systems-design write-ups.

## How to work

Before making changes, read:

1. `README.md`
2. `TASKS.md`
3. `PLANS.md`
4. The most relevant file under `docs/`

For multi-step work, create or update a short plan in `PLANS.md` before implementation.

## Expected repo layout

- `src/energy_flex_pipeline/` — Python package code
- `tests/` — pytest tests
- `docs/` — project brief, design notes, contracts, interview material
- `prompts/` — reusable Codex prompts
- `data/raw/` — generated local data only; do not commit large data
- `data/processed/` — generated local outputs only; do not commit large data
- `notebooks/` — optional exploration; core logic must live in `src/`
- `diagrams/` — architecture diagrams or Mermaid source

## Engineering standards

Use:

- Python 3.11+
- `uv` for dependency management
- `pytest` for tests
- `ruff` for lint/format
- `mypy` where practical
- `pydantic` for schemas/config
- structured logging instead of ad-hoc prints
- type hints for public functions
- small modules with explicit responsibilities

Prefer deterministic synthetic data generation. Use fixed seeds when generating data for tests.

## Commands

When tooling is available, use these commands:

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy src
```

If a command fails because the project is still being scaffolded, document the reason and make the smallest useful fix.

## Data rules

- Use synthetic data only.
- Do not add secrets, real credentials, proprietary data, or large generated datasets.
- Keep generated data out of git unless a tiny fixture is explicitly needed for tests.
- Use `.gitkeep` for empty data directories.

## Design priorities

Preserve these themes throughout the code and documentation:

1. Temporal correctness: event time, ingestion time, correction time.
2. Idempotency and replayability.
3. Late-arriving and corrected data.
4. Observability and operational readiness.
5. Spark reasoning: partitions, joins, shuffles, skew, checkpointing.
6. Cloud mapping: local design should have a plausible Azure/Databricks equivalent.
7. Interview explanation: every major feature should be explainable in 2–3 minutes.

## Do-not rules

- Do not build a generic data toy project.
- Do not hide core logic in notebooks.
- Do not overbuild with Kubernetes, Terraform, or full cloud deployment unless explicitly requested.
- Do not add dependencies casually. Prefer a small, coherent stack.
- Do not claim commands passed unless they actually ran.
- Do not leave generated files, caches, or huge data artifacts in the repo.

## Definition of done

For any coding task:

1. Implement the smallest coherent vertical slice.
2. Add or update tests.
3. Run relevant checks.
4. Update docs if behavior or architecture changed.
5. Summarize changed files, tests run, and limitations.

For any documentation task:

1. Keep the document concise and operational.
2. Include assumptions and trade-offs.
3. Add action items if implementation is implied.
4. Preserve the senior data engineering / tech lead preparation frame.
