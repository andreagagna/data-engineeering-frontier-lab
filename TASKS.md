# TASKS.md

## Priority legend

- P0 — essential interview signal
- P1 — strong differentiator
- P2 — polish or extension

## Phase 1 — Bootstrap production Python foundation

- [x] P0: Create package skeleton under `src/energy_flex_pipeline/`.
- [x] P0: Add `pyproject.toml` with `uv`, `pytest`, `ruff`, `mypy`, `pydantic`.
- [ ] P0: Add deterministic synthetic data generator.
- [ ] P0: Define event schemas with Pydantic.
- [ ] P0: Add structured logging helper.
- [x] P0: Add config model and local settings pattern.
- [ ] P0: Add initial pytest tests for schemas and deterministic generation.
- [ ] P1: Add CLI entry point.

## Phase 2 — SQL temporal correctness

- [ ] P0: Generate battery telemetry events.
- [ ] P0: Generate market price events.
- [ ] P0: Generate asset metadata with historical changes.
- [ ] P0: Implement latest-state SQL query.
- [ ] P0: Implement hourly revenue aggregation.
- [ ] P0: Implement SCD2 asset metadata model.
- [ ] P0: Implement point-in-time join.
- [ ] P1: Add query explain notes.
- [ ] P1: Add data quality checks for duplicates, nulls, impossible values, and time anomalies.

## Phase 3 — Spark and lakehouse reasoning

- [ ] P0: Implement PySpark bronze ingestion from local files.
- [ ] P0: Implement silver validation/normalization transform.
- [ ] P0: Implement gold aggregation transform.
- [ ] P0: Document partitioning and shuffle behavior.
- [ ] P1: Create skewed data example and mitigation.
- [ ] P1: Add Delta-style merge/upsert correction path.
- [ ] P2: Add performance notes comparing DuckDB and Spark for this local use case.

## Phase 4 — Streaming simulation

- [ ] P1: Add file-based streaming simulation or local event feed.
- [ ] P1: Add event-time windows.
- [ ] P1: Add watermarking example.
- [ ] P1: Add checkpointing/restart notes.
- [ ] P1: Add late-event scenario and expected behavior.

## Phase 5 — Operational readiness

- [ ] P0: Add Dockerfile.
- [ ] P0: Add GitHub Actions workflow.
- [ ] P0: Add runbook skeleton.
- [ ] P0: Define operational metrics and alert conditions.
- [ ] P1: Add lineage/dataflow diagram.
- [ ] P1: Add Azure architecture mapping.

## Phase 6 — Interview synthesis

- [ ] P0: Write 3-minute project pitch.
- [ ] P0: Write system-design one-pager for batch pipeline.
- [ ] P0: Write system-design one-pager for streaming pipeline.
- [ ] P0: Write incident-recovery one-pager.
- [ ] P0: Write 6 STAR stories.
- [ ] P1: Add final README section: what this project proves.
