# 00 — Codex Starter Prompts

## Prompt 1 — Repository orientation

```text
Read README.md, AGENTS.md, PLANS.md, TASKS.md, and docs/01_CAPSTONE_SPEC.md.
Summarize the repository mission, the intended architecture, the current backlog, and the first three implementation tasks you recommend.
Do not modify files yet.
```

## Prompt 2 — Bootstrap implementation

```text
Read README.md, AGENTS.md, PLANS.md, TASKS.md, and docs/03_DATA_CONTRACTS.md.
Implement Phase 1 bootstrap:
- package skeleton under src/energy_flex_pipeline/;
- Pydantic event schemas;
- deterministic synthetic data generator skeleton;
- config model;
- structured logging helper;
- Typer CLI entry point for generating a tiny sample dataset;
- initial pytest tests.
Keep the implementation small.
Run relevant checks and summarize changed files, tests run, and limitations.
```

## Prompt 3 — SQL temporal correctness

```text
Read docs/01_CAPSTONE_SPEC.md and docs/03_DATA_CONTRACTS.md.
Add DuckDB-based SQL examples for:
- latest state per asset;
- hourly telemetry aggregation;
- SCD2 asset metadata;
- point-in-time join;
- late correction impact report.
Add tests or reproducible scripts where practical.
Update docs if assumptions change.
```

## Prompt 4 — Spark vertical slice

```text
Read docs/01_CAPSTONE_SPEC.md, docs/04_ARCHITECTURE_DECISIONS.md, and TASKS.md.
Implement a minimal PySpark bronze/silver/gold vertical slice using local generated data.
Include notes or comments showing where shuffles, joins, partitions, and skew risks appear.
Do not overbuild. Add tests if practical and document how to run the slice.
```

## Prompt 5 — Streaming simulation

```text
Read docs/05_SYSTEM_DESIGN_PROMPTS.md and the existing pipeline code.
Add a minimal streaming simulation using file-based events or another lightweight local mechanism.
Demonstrate event-time windowing, late data, and checkpoint/restart behavior.
Document the latency/correctness trade-off.
```

## Prompt 6 — Operational readiness

```text
Read AGENTS.md and docs/07_REVIEW_CHECKLIST.md.
Add operational readiness artifacts:
- Dockerfile;
- GitHub Actions workflow;
- runbook skeleton;
- metrics and alerts document;
- architecture diagram source using Mermaid if possible.
Keep it local-first and interview-oriented.
```

## Prompt 7 — Interview synthesis

```text
Review the implemented project and docs.
Create or update interview synthesis materials:
- 3-minute project pitch;
- one-page batch pipeline design;
- one-page streaming pipeline design;
- one-page incident recovery design;
- 6 STAR stories connected to the project and prior experience.
Be concise, senior, and operational.
```

## Prompt 8 — Code review

```text
Review the current uncommitted changes against AGENTS.md and docs/07_REVIEW_CHECKLIST.md.
Look for bugs, weak tests, overengineering, unclear naming, missing docs, and interview-signal gaps.
Return prioritized findings and small patches where appropriate.
```
