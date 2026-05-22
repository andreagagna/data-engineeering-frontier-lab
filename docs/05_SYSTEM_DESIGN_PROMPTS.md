# 05 — System Design Prompts

## How to use this file

For each prompt, produce a one-page answer/discussion using:

1. Requirements and assumptions.
2. Data model.
3. Architecture.
4. Failure modes.
5. Correctness guarantees.
6. Observability.
7. Trade-offs.

Keep answers concise enough to explain in 3 minutes.

## Prompt 1 — Batch market-price ingestion

Design a batch pipeline that ingests day-ahead market prices, validates them, and exposes clean hourly price data for analytics.

Questions to answer:

- How do you handle missing or overlapping intervals?
- How do you version corrected prices?
- How do you rerun a failed day safely?
- How do you alert on freshness issues?

## Prompt 2 — Battery telemetry pipeline

Design a pipeline that ingests battery telemetry every minute from many assets.

Questions to answer:

- What are the bronze, silver, and gold layers?
- How do you handle duplicates and out-of-order events?
- How do you compute latest state per asset?
- What do you monitor?

## Prompt 3 — Streaming grid-balancing signal

Design a near-real-time pipeline that computes rolling availability and dispatch readiness for a battery fleet.

Questions to answer:

- What is the event-time windowing strategy?
- What lateness do you allow?
- What happens when late data changes a prior window?
- How do you trade latency against correctness?

## Prompt 4 — Backfill and replay

Historical data for three months was discovered to contain incorrect asset capacity metadata. Design a safe correction and replay strategy.

Questions to answer:

- How do you identify affected outputs?
- How do you make the replay idempotent?
- How do you avoid corrupting current production outputs?
- How do you communicate the impact?

## Prompt 5 — Spark performance incident

A daily Spark job went from 20 minutes to 3 hours after a new data source was added.

Questions to answer:

- What do you inspect first?
- How do you detect skew?
- How do you reason about shuffles and joins?
- What fixes would you try?
- How do you prevent recurrence?

## Prompt 6 — Tech lead alignment

A stakeholder wants real-time dashboards, but the source systems only provide delayed and sometimes corrected data.

Questions to answer:

- How do you explain the latency/correctness trade-off?
- What service levels would you propose?
- How do you avoid overpromising?
- How do you design a phased delivery?
