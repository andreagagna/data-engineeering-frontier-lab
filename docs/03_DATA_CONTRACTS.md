# 03 — Data Contracts

## Purpose

This document defines the first-pass contracts for synthetic events. These should become Pydantic models and test fixtures.

## General event rules

All events should include:

- stable unique identifier;
- event-time timestamp;
- ingestion timestamp where relevant;
- source system;
- deterministic generation path;
- validation rules.

Use timezone-aware UTC timestamps internally.

## BatteryTelemetryEvent

### Fields

| Field | Type | Rule |
|---|---|---|
| `event_id` | string | unique, stable |
| `asset_id` | string | non-empty |
| `event_time` | datetime | timezone-aware UTC |
| `ingested_at` | datetime | timezone-aware UTC, may be after event time |
| `state_of_charge_pct` | float | 0–100 |
| `power_kw` | float | can be negative for discharge, positive for charge |
| `temperature_c` | float | plausible operational range, e.g. -40 to 90 |
| `availability_status` | enum | `available`, `limited`, `offline` |
| `source_system` | string | non-empty |

### Quality checks

- duplicate `event_id`;
- impossible state of charge;
- impossible temperature;
- missing asset;
- excessive ingestion delay;
- out-of-order event arrival.

## MarketPriceEvent

### Fields

| Field | Type | Rule |
|---|---|---|
| `price_event_id` | string | unique |
| `market` | string | non-empty |
| `delivery_start` | datetime | timezone-aware UTC |
| `delivery_end` | datetime | greater than start |
| `published_at` | datetime | timezone-aware UTC |
| `price_eur_mwh` | float | may be negative |
| `currency` | string | default `EUR` |
| `source_system` | string | non-empty |

### Quality checks

- overlapping intervals by market;
- missing interval;
- duplicate interval version;
- extreme price outliers.

## AssetMetadataVersion

### Fields

| Field | Type | Rule |
|---|---|---|
| `asset_id` | string | non-empty |
| `asset_name` | string | non-empty |
| `location` | string | non-empty |
| `capacity_mwh` | float | positive |
| `max_power_mw` | float | positive |
| `operator` | string | non-empty |
| `valid_from` | datetime | timezone-aware UTC |
| `valid_to` | datetime/null | greater than `valid_from` if present |
| `is_current` | bool | one current row per asset |

### Quality checks

- overlapping validity windows;
- multiple current versions;
- negative capacity;
- missing historical version for point-in-time join.

## CorrectionEvent

### Fields

| Field | Type | Rule |
|---|---|---|
| `correction_id` | string | unique |
| `original_event_id` | string | references prior event |
| `corrected_event_id` | string | references replacement event |
| `correction_time` | datetime | timezone-aware UTC |
| `reason` | string | non-empty |
| `correction_type` | enum | `replace`, `invalidate`, `amend` |

## Design note

The critical modeling separation is:

- `event_time`: when the business event happened;
- `ingested_at`: when the platform learned about it;
- `correction_time`: when the known truth changed.
