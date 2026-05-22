# 02 — Three-Week Intensive Plan

## Assumption

45–60 focused hours total.

The plan is intentionally compressed. Some areas remain superficial. The aim is a hands-on refresh of a selection of data engineering themes.

## Week 1 — Engineering foundation and SQL correctness

### Goal

Look like an engineer, not a notebook user.

### Topics

- Production Python.
- Pydantic schemas.
- Testing.
- Config and logging.
- Synthetic data generation.
- SQL temporal modeling.
- SCD2 and point-in-time joins.

### Deliverables

- Runnable package skeleton.
- Synthetic data generator.
- Event validation tests.
- DuckDB SQL models.
- One-page SQL correctness note.

### Exercises

1. Create synthetic telemetry and market data with deterministic seeds.
2. Write validation tests for impossible values and malformed timestamps.
3. Write SQL for latest state per asset using window functions.
4. Build SCD2 metadata and point-in-time joins.
5. Add a late-arriving correction scenario and prove the output changes correctly.

## Week 2 — Spark, lakehouse, streaming semantics

### Goal

Show distributed-processing intuition.

### Topics

- Spark execution model.
- Partitions, shuffles, joins, skew.
- Bronze/silver/gold structure.
- Delta-style merge/upsert thinking.
- Structured Streaming concepts.
- Watermarks and checkpointing.

### Deliverables

- PySpark bronze/silver/gold pipeline.
- Explain-plan notes.
- Skew demo.
- Late-event merge/upsert demo.
- Streaming simulation note.

### Exercises

1. Port SQL transformations to PySpark.
2. Inspect execution plans.
3. Create skewed asset data and mitigate it.
4. Simulate corrected events and idempotent merge behavior.
5. Add file-based streaming window aggregation with late events.

## Week 3 — Operational maturity and leadership signal

### Goal

Move from “can code” to “can own.”

### Topics

- Docker.
- CI.
- Observability.
- Runbooks.
- Azure architecture mapping.
- System design communication.
- Behavioral narrative.

### Deliverables

- Dockerfile.
- GitHub Actions workflow.
- Operational runbook.
- Azure architecture diagram.
- Three system-design one-pagers.
- Six STAR stories.

### Exercises

1. Dockerize the local project.
2. Add CI for tests/linting.
3. Define freshness, duplication, row-count, lag, and schema-drift metrics.
4. Write failure-mode recovery paths.
5. Design the Azure equivalent of the local architecture.
6. Practice 3-minute explanations of each major design choice.

## Ruthless priority order

If time collapses, protect:

1. Python package + tests.
2. SQL temporal correctness.
3. Spark joins/shuffles/skew reasoning.
4. Late-event correction and idempotency.
5. Streaming concepts.
6. System-design one-pagers.

Cut first:

1. Kubernetes.
2. Full IaC.
3. Heavy dashboards.
4. Deep Azure networking.
5. Fancy notebooks.
