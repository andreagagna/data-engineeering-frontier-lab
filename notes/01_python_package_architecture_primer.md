# Python Package Architecture Primer

## Purpose

This note explains how to design the first production-grade Python package for the Energy Flex Mini-Lakehouse.

The immediate package role is narrow:

- generate deterministic synthetic data;
- validate event contracts with Pydantic;
- expose a small CLI;
- centralize config and local settings;
- emit structured logs;
- support tests for schemas, generation, and idempotency.

The package should be small enough to understand in one sitting and structured enough to grow into SQL, Spark, streaming, observability, and runbook work later.

## What Production-Grade Means Here

Production-grade here means the code has clear contracts, predictable execution, observable behavior, and tests around important assumptions.

For this repo, production-grade means:

- public functions are typed;
- event shapes are explicit Pydantic models;
- timestamps are timezone-aware UTC values;
- generated data is deterministic when given the same seed;
- file outputs are predictable and idempotent where practical;
- config is explicit and environment-overridable;
- logging is structured and suitable for local debugging or cloud mapping;
- CLI commands fail with useful errors;
- tests cover validation, deterministic generation, and basic output behavior.

## Questions To Ask Before Designing

Start with behavior, not files.

1. What is the smallest useful workflow?
   - For this repo: run a CLI command that creates a tiny synthetic dataset under `data/raw/`.

2. What are the domain objects?
   - Telemetry events, market price events, trade events, asset metadata versions, correction events.

3. What are the invariants?
   - IDs are stable.
   - Event timestamps are timezone-aware UTC.
   - State of charge is between 0 and 100.
   - Market intervals have `delivery_end > delivery_start`.
   - Metadata validity windows do not overlap for the same asset.

4. What must be deterministic?
   - The generator should produce identical records for the same seed and config.

5. What changes often?
   - Generation parameters, output paths, scenario volumes, and data quality edge cases.

6. What should be hard to misuse?
   - Writing outside approved data directories.
   - Creating naive datetimes.
   - Generating random data without an explicit seed.
   - Mixing business event time with ingestion or correction time.

7. What should be easy to test?
   - Pydantic validation.
   - Generator determinism.
   - CLI argument parsing.
   - Output file names and row counts.

8. What will need a cloud equivalent later?
   - Local config maps to environment variables and managed secrets.
   - Local files map to object storage.
   - Structured logs map to centralized observability.
   - Deterministic generation maps to replayable ingestion and backfill patterns.

## Recommended Package Shape

Use `src/` layout:

```text
src/
└── energy_flex_pipeline/
    ├── __init__.py
    ├── cli.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    ├── domain/
    │   ├── __init__.py
    │   └── time.py
    ├── generation/
    │   ├── __init__.py
    │   ├── assets.py
    │   ├── corrections.py
    │   ├── market_prices.py
    │   ├── telemetry.py
    │   └── trades.py
    ├── io/
    │   ├── __init__.py
    │   └── local_files.py
    ├── observability/
    │   ├── __init__.py
    │   └── logging.py
    └── schemas/
        ├── __init__.py
        └── events.py
```

Test layout:

```text
tests/
├── test_config.py
├── test_schemas.py
├── test_generation_determinism.py
└── test_cli.py
```

This structure keeps architectural boundaries explicit without introducing a full framework. The top-level package contains the application entry point. Subpackages separate settings, domain helpers, contracts, generation, local IO, and observability.

Do not add a `pipelines/` package immediately. Add it once there are real multi-step workflows to compose, such as bronze validation, silver normalization, gold aggregation, or Spark jobs.

## Module Responsibilities

### `config/settings.py`

Owns application settings.

Use Pydantic settings so local defaults can be overridden by environment variables.

Examples of settings:

- `raw_data_dir`;
- `processed_data_dir`;
- `default_seed`;
- `default_asset_count`;
- `default_start_time`;
- `log_level`.

Rules:

- avoid reading environment variables throughout the codebase;
- load config once near the application boundary;
- pass config into functions explicitly where practical.

### `observability/logging.py`

Owns structured logging setup.

Use `structlog` as the package logging standard.

The goal is consistent, structured logs that are useful locally and easy to map to centralized observability later.

Recommended fields:

- `timestamp`;
- `level`;
- `logger`;
- `message`;
- optional context such as `run_id`, `dataset`, `row_count`, `output_path`, `seed`.

Rules:

- package code should create loggers with `structlog.get_logger(__name__)`;
- CLI entry points should configure logging once;
- package code should not use ad-hoc `print`.
- log events should use stable event names and key-value context, for example `logger.info("dataset_written", dataset="telemetry", row_count=100)`;
- avoid embedding important context only inside formatted message strings.

### `schemas/events.py`

Owns event contracts.

Use Pydantic models for:

- `BatteryTelemetryEvent`;
- `MarketPriceEvent`;
- `TradeEvent`;
- `AssetMetadataVersion`;
- `CorrectionEvent`.

Rules:

- validate timezone-aware UTC timestamps;
- use enums for constrained string values;
- validate ranges directly on models;
- keep schema models free of file IO and random generation logic.

### `domain/time.py`

Owns timestamp helpers.

This is useful because temporal correctness is central to the project.

Potential helpers:

- `ensure_utc`;
- `utc_now`;
- `parse_utc_datetime`;
- `hour_range`.

Rules:

- avoid naive datetimes;
- prefer timezone-aware UTC internally;
- make time handling explicit in tests.

### `generation/*`

Owns synthetic data generation.

Each module should generate one family of records. For example, `telemetry.py` should know how to generate telemetry records, but it should not know how to write files or parse CLI arguments.

Rules:

- accept explicit config and seed inputs;
- return typed records or serializable dictionaries;
- keep randomness behind a seeded random number generator;
- model abnormal scenarios deliberately: late arrivals, duplicates, corrections, out-of-order events, skewed assets.

### `io/local_files.py`

Owns local file output.

Rules:

- write to configured data directories;
- create parent directories when needed;
- prefer stable file names for deterministic runs;
- avoid committing generated outputs except tiny fixtures when explicitly needed.

### `cli.py`

Owns the command-line interface.

The CLI should be thin:

- parse arguments;
- load config;
- configure logging;
- call generation functions;
- report output paths and row counts.

It should not contain domain generation logic.

### Future `pipelines/*`

Will own workflow composition once individual pieces exist.

Examples:

- generate raw datasets;
- validate bronze inputs;
- build silver normalized outputs;
- build gold analytical outputs;
- run late-event correction scenarios.

Rules:

- compose lower-level modules;
- keep business contracts in `schemas/`;
- keep storage behavior in `io/`;
- keep Spark-specific work isolated when it arrives.

## Basic Design Patterns

### Boundary Pattern

Keep IO, configuration, and CLI parsing at the edges of the application.

Core generation functions should be easy to call from tests without touching files or environment variables.

### Dependency Injection

Pass dependencies into functions instead of hiding them globally.

For this project, that mainly means:

- pass settings;
- pass seeds or random generators;
- pass output paths.

This makes tests simple and reproducible.

### Factory Pattern

Use small factory functions to create domain events.

Example shape:

```python
def make_telemetry_event(...) -> BatteryTelemetryEvent:
    ...
```

Factories are useful when event construction has repeated validation or timestamp logic.

### Strategy Pattern

Use explicit scenario functions for different generation behaviors.

Examples:

- normal telemetry;
- late telemetry;
- duplicate telemetry;
- corrected telemetry;
- skewed asset distribution.

This keeps scenario complexity visible instead of hiding it in one large generator.

### Repository / Writer Pattern

Keep writing separate from generating.

The generator should answer: "What records should exist?"

The writer should answer: "Where and how are records persisted locally?"

### Contract Tests

Use tests to protect assumptions that later SQL and Spark code will rely on.

Examples:

- invalid state of charge is rejected;
- market interval end must be after start;
- same seed produces same records;
- correction events reference original and corrected IDs;
- generated timestamps are timezone-aware UTC.

## Rules Of Thumb

1. Keep domain logic independent from the CLI.
2. Keep schemas independent from generators.
3. Keep file writing independent from record creation.
4. Pass config explicitly at boundaries.
5. Use enums for constrained business values.
6. Use fixed seeds in tests.
7. Treat time as a first-class modeling concern.
8. Do not introduce Spark before the local data contracts are stable.
9. Add dependencies only when they simplify a real problem.
10. Prefer small modules with one reason to change.
11. Write tests for invariants, not just happy paths.
12. Make generated data explainable by reading the generator code.

## Natural Build Order

The lowest-risk order is:

1. `pyproject.toml` and tooling.
2. Package skeleton with `__init__.py`.
3. Config model and local settings pattern.
4. Timestamp helpers.
5. Pydantic schemas and enums.
6. Structured logging helper.
7. One deterministic generator for telemetry.
8. Tests for schema validation and generator determinism.
9. File writer for local raw outputs.
10. CLI command for a tiny sample dataset.
11. Additional generators for market prices, trades, metadata, and corrections.
12. Data quality tests.
13. DuckDB SQL models over generated files.
14. Spark transforms once contracts and local outputs are stable.

This order lets each step create something testable before adding another layer.

## Proposed First Vertical Slice

The first implementation slice should create:

- `src/energy_flex_pipeline/__init__.py`;
- `src/energy_flex_pipeline/config/__init__.py`;
- `src/energy_flex_pipeline/config/settings.py`;
- `src/energy_flex_pipeline/domain/__init__.py`;
- `src/energy_flex_pipeline/domain/time.py`;
- `src/energy_flex_pipeline/schemas/__init__.py`;
- `src/energy_flex_pipeline/schemas/events.py`;
- `src/energy_flex_pipeline/observability/__init__.py`;
- `src/energy_flex_pipeline/observability/logging.py`;
- `src/energy_flex_pipeline/generation/__init__.py`;
- `src/energy_flex_pipeline/generation/telemetry.py`;
- `src/energy_flex_pipeline/io/__init__.py`;
- `src/energy_flex_pipeline/io/local_files.py`;
- `tests/test_schemas.py`;
- `tests/test_generation_determinism.py`.

Definition of done:

- package imports cleanly;
- telemetry schema rejects impossible values;
- telemetry generator is deterministic for a fixed seed;
- tests run with `uv run pytest`;
- lint runs with `uv run ruff check .`.

## Common Failure Modes

Avoid these early mistakes:

- starting with a broad generator before schemas are stable;
- hiding important logic in notebooks;
- mixing random generation, validation, and file writing in one function;
- using local timezone datetimes;
- making tests depend on current wall-clock time;
- adding Spark before the synthetic contracts are trustworthy;
- overbuilding plugin systems or abstract base classes before there are multiple real implementations.

## Design Standard For This Repo

Each new module should make one of these things clearer:

- the event contract;
- the generation scenario;
- the execution boundary;
- the operational behavior;
- the testable invariant.

If a module does not make one of those clearer, it is probably too early.
