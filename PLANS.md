# PLANS.md

## Purpose

Use this file to keep Codex work bounded, reviewable, and aligned with the preparation objective.

A plan should be short. It should describe the next coherent slice, not the entire universe.

## Execution plan template

```md
# Plan: <short title>

## Goal

<What should be true after this task?>

## Scope

In scope:
- ...

Out of scope:
- ...

## Steps

1. ...
2. ...
3. ...

## Verification

Run:

```bash
uv run pytest
uv run ruff check .
```

Expected result:
- ...

## Risks / trade-offs

- ...
```

## Current 3-week macro-plan

### Week 1 — Python engineering + SQL correctness

Goal: production-grade repo.

Deliverables:

- package skeleton;
- config and logging;
- synthetic event generator;
- event schemas;
- tests;
- DuckDB SQL models for temporal correctness;
- SCD2 and point-in-time join example.

### Week 2 — Spark + lakehouse + streaming semantics

Goal: distributed-processing reasoning.

Deliverables:

- PySpark bronze/silver/gold transformations;
- explain-plan notes;
- skew demonstration;
- late-event correction path;
- streaming simulation;
- watermark/checkpointing notes.

### Week 3 — operational maturity + systems design

Goal: architecture and system design thinking.

Deliverables:

- Docker and CI;
- observability metrics and runbook;
- Azure architecture mapping;
- system design one-pagers;
- STAR stories.

## Initial Codex implementation plan

# Plan: Phase 1 bootstrap

## Goal

Create the minimal runnable Python project for the Energy Flex Mini-Lakehouse.

## Scope

In scope:

- `pyproject.toml` tooling setup;
- package structure under `src/energy_flex_pipeline/`;
- config model;
- structured logging helper;
- Pydantic event models;
- deterministic synthetic data generator skeleton;
- initial pytest tests.

Out of scope:

- Spark;
- Delta Lake;
- streaming;
- Docker;
- Azure architecture;
- large generated datasets.

## Steps

1. Add package modules: `config.py`, `logging.py`, `schemas.py`, `generate.py`, `cli.py`.
2. Add CLI entry point for generating a small sample dataset.
3. Add tests for event validation and deterministic generation.
4. Add `.gitignore` for generated data/caches.
5. Run `uv sync`, `uv run pytest`, and `uv run ruff check .` if available.

## Verification

Expected:

- tests pass;
- package imports cleanly;
- sample generator can create a tiny local dataset;
- generated data is not committed except small fixtures if needed.

## Current working plan

# Plan: Timestamp helpers

## Goal

Create the shared timestamp policy helpers before implementing event schemas.

## Scope

In scope:

- `domain` package;
- UTC normalization helper;
- ISO timestamp parsing helper;
- current UTC timestamp helper;
- tests for naive timestamp rejection and UTC conversion.

Out of scope:

- schemas;
- synthetic generators;
- CLI;
- logging setup;
- file IO;
- generated data.

## Steps

1. Add tests that describe the expected timestamp behavior.
2. Run tests and confirm they fail for the missing implementation.
3. Implement the smallest `domain/time.py` helper module.
4. Run tests, lint, and type checks where available.

## Verification

Run:

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

Expected:

- timezone-aware UTC datetimes remain UTC;
- timezone-aware non-UTC datetimes are normalized to UTC;
- naive datetimes and naive timestamp strings are rejected;
- `utc_now` returns a timezone-aware UTC datetime.
