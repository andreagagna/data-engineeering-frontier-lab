# Energy Flex Mini-Lakehouse

**Project type:** data engineering self-learning and reviewing
**Target archetype:** cloud-native, quantitative, operationally consequential data engineering
**Last updated:** 2026-05-22

## 1. Purpose

This repository is a compact preparation environment for building and demonstrating the capability frontier expected of a data engineer in a tech or fin-tech company.

The goal is to review and increase fluency in:

- production-grade Python;
- temporal SQL correctness;
- Spark / distributed processing reasoning;
- lakehouse design;
- late-arriving and corrected data;
- streaming semantics;
- observability and operational readiness;
- senior-level systems design communication.

The project uses a simulated battery / energy-market domain because it naturally exposes the hard parts: time, ordering, replay, correction, latency, reliability, and economic consequence.

## 2. Capstone concept

Build a local mini-lakehouse:

```text
Synthetic battery + market events
        ↓
Bronze ingestion
        ↓
Validation + schema enforcement
        ↓
Silver temporal correction / normalization
        ↓
Gold analytical models
        ↓
Streaming simulation + late-event handling
        ↓
Operational runbook + interview-ready design notes
```

## 3. Expected final artifacts

By the end of the 3-week preparation sprint, this repo should contain:

1. A clean Python package under `src/energy_flex_pipeline/`.
2. Synthetic data generation for telemetry, market prices, trades, asset metadata, and corrections.
3. SQL models for temporal correctness, latest state, SCD2, point-in-time joins, and revenue aggregation.
4. PySpark transformations for bronze/silver/gold layers.
5. A late-arriving data correction path using merge/upsert semantics.
6. A minimal streaming simulation with event-time windows and checkpointing.
7. Tests for schemas, transformations, and idempotency.
8. A Dockerized runtime and CI checks.
9. An Azure architecture mapping.
10. One-pagers explaining design trade-offs.

## 4. Repository layout

```text
.
├── AGENTS.md                         # Codex instructions and working agreements
├── PLANS.md                          # Execution plan template and current sprint plan
├── README.md                         # Project overview
├── TASKS.md                          # Implementation backlog
├── pyproject.toml                    # Python project metadata and tooling skeleton
├── docs/
│   ├── 00_PROJECT_BRIEF.md
│   ├── 01_CAPSTONE_SPEC.md
│   ├── 02_THREE_WEEK_PLAN.md
│   ├── 03_DATA_CONTRACTS.md
│   ├── 04_ARCHITECTURE_DECISIONS.md
│   ├── 05_SYSTEM_DESIGN_PROMPTS.md
│   ├── 06_INTERVIEW_STORIES.md
│   └── 07_REVIEW_CHECKLIST.md
├── prompts/
│   └── 00_CODEX_STARTER_PROMPTS.md
├── src/
│   └── energy_flex_pipeline/
├── tests/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
└── diagrams/
```

## 5. Suggested local stack

This project should stay small and local-first.

Recommended stack:

- Python 3.11+
- `uv` for dependency and environment management
- `pytest` for tests
- `ruff` for linting/formatting
- `mypy` for static type checks
- `pydantic` for event schemas and config
- `duckdb` for local SQL modeling
- `polars` or `pandas` for lightweight data work
- `pyspark` for distributed-processing exercises
- `delta-spark` only when needed for merge/upsert semantics
- Docker for reproducibility

Do not begin with Kubernetes, Terraform, or heavy cloud infrastructure. Those belong in the architecture mapping unless time remains.

## 6. Quickstart for Codex

Open this repository in Codex and begin with one of the prompts in:

```text
prompts/00_CODEX_STARTER_PROMPTS.md
```

Recommended first task:

```text
Read README.md, AGENTS.md, PLANS.md, TASKS.md, and docs/01_CAPSTONE_SPEC.md.
Summarize the repository mission, the intended architecture, the current backlog, and the first three implementation tasks you recommend.
Do not modify files yet.
```

## 7. Operating principle

Prefer:

- correctness over tool glamour;
- reproducibility over notebook improvisation;
- narrow complete slices over broad unfinished scaffolding;
- explainable trade-offs over maximal architecture;
- operational maturity over demo theater.

## 8. Definition of done

A task is done only when:

- code is implemented in the intended location;
- tests are added or updated;
- relevant commands pass locally or the failure is documented;
- README/docs are updated if behavior changed;
- design trade-offs are captured when relevant;
- the final Codex response summarizes files changed, tests run, and known limitations.
