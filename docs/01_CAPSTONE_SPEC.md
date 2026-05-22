# 01 — Capstone Specification

## Capstone

Build a local mini-lakehouse for simulated battery-flex and market-price data.

## Domain story

A fleet of battery assets participates in energy flexibility markets. The system receives telemetry, market prices, dispatch instructions, trades, and asset metadata updates. Events can arrive late, be corrected, or conflict. The data platform must reconstruct reliable historical truth and expose analytical outputs.

## Data entities

### Battery telemetry event

Represents observed state of a battery asset.

Candidate fields:

- `event_id`
- `asset_id`
- `event_time`
- `ingested_at`
- `state_of_charge_pct`
- `power_kw`
- `temperature_c`
- `availability_status`
- `source_system`

### Market price event

Represents market price for a time interval.

Candidate fields:

- `price_event_id`
- `market`
- `delivery_start`
- `delivery_end`
- `published_at`
- `price_eur_mwh`
- `currency`
- `source_system`

### Dispatch instruction event

Represents instruction to charge/discharge/hold.

Candidate fields:

- `instruction_id`
- `asset_id`
- `event_time`
- `target_power_kw`
- `instruction_type`
- `valid_from`
- `valid_to`
- `created_at`

### Trade event

Represents commercial trade/position data.

Candidate fields:

- `trade_id`
- `asset_id`
- `market`
- `trade_time`
- `delivery_start`
- `delivery_end`
- `volume_mwh`
- `price_eur_mwh`
- `side`

### Asset metadata / SCD2 entity

Represents changing asset attributes.

Candidate fields:

- `asset_id`
- `asset_name`
- `location`
- `capacity_mwh`
- `max_power_mw`
- `operator`
- `valid_from`
- `valid_to`
- `is_current`

### Correction event

Represents a late correction or replacement.

Candidate fields:

- `correction_id`
- `original_event_id`
- `corrected_event_id`
- `correction_time`
- `reason`
- `correction_type`

## Required scenarios

The synthetic generator should produce:

1. Normal telemetry events.
2. Late-arriving telemetry events.
3. Duplicate events.
4. Corrected events.
5. Out-of-order events.
6. Asset metadata changes over time.
7. Market price intervals with rolling windows.
8. At least one skewed asset or market to demonstrate Spark skew.

## Required analytical outputs

- Latest state per asset.
- Hourly average state of charge and power.
- Revenue estimate by asset and market interval.
- Point-in-time asset metadata enrichment.
- Data quality report.
- Late-event impact report.

## Required engineering outputs

- Event schemas.
- Deterministic synthetic data generation.
- SQL models.
- PySpark transforms.
- Basic streaming simulation.
- Tests.
- Operational runbook.
- Architecture diagram.

## Non-goals

- Real trading strategy.
- Real energy market integration.
- Production cloud deployment.
- Full MLOps system.
- Full Kubernetes/Terraform stack.

## Interview value

This project should make it easier to explain and reason about:

- how temporal truth differs from latest ingested state;
- how to make backfills safe;
- how to handle corrections idempotently;
- why Spark jobs become slow;
- how to reason about streaming windows;
- what to monitor in a consequential data pipeline;
- how to map local design to Azure/Databricks.
