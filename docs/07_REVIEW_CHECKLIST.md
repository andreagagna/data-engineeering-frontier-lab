# 07 — Review Checklist

## Code review checklist

Before accepting Codex changes, verify:

- [ ] The change is aligned with the current task.
- [ ] Core logic lives in `src/`, not notebooks.
- [ ] Public functions have useful type hints.
- [ ] Tests were added or updated.
- [ ] Synthetic data generation is deterministic where needed.
- [ ] No large generated data files were committed.
- [ ] No secrets or real data were added.
- [ ] Commands were actually run or failures were documented.
- [ ] README/docs were updated if behavior changed.
- [ ] The implementation remains small enough to explain.

## Data correctness checklist

- [ ] Event time and ingestion time are clearly separated.
- [ ] Late-arriving data behavior is explicit.
- [ ] Duplicate handling is explicit.
- [ ] Correction/replacement behavior is idempotent.
- [ ] Point-in-time joins do not use future metadata.
- [ ] Aggregations are reproducible.
- [ ] Data quality checks cover impossible values.

## Spark checklist

- [ ] Joins are intentional.
- [ ] Shuffles are understood and documented.
- [ ] Partitioning strategy is explicit.
- [ ] Skew risks are considered.
- [ ] Caching is justified if used.
- [ ] Streaming checkpoints are explained if used.

## Operational checklist

- [ ] Freshness metric exists.
- [ ] Failure rate metric exists.
- [ ] Row-count anomaly check exists.
- [ ] Duplicate-rate check exists.
- [ ] Schema-drift check exists.
- [ ] Runbook explains likely failures.
- [ ] Backfill/replay path is documented.

## Peer-review readiness checklist

For each major component, be able to answer:

1. Why did you design it this way?
2. What can go wrong?
3. How would you detect failure?
4. How would you recover?
5. How would this map to Azure/Databricks?
6. How would it scale?
7. What did you deliberately not build?
