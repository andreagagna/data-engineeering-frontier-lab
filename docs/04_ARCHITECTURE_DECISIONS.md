# 04 — Architecture Decisions

## ADR-001 — Use synthetic energy-flex data

### Decision

Use a simulated battery / market domain instead of generic sales/order data.

### Rationale

The target role class is likely temporal, operational, and quantitative. Battery and market data naturally exposes late events, event ordering, interval joins, streaming windows, corrections, and economic consequence.

### Consequence

The project becomes more memorable and strategically aligned than a generic analytics pipeline.

## ADR-002 — Local-first implementation

### Decision

Build the project locally before mapping to Azure.

### Rationale

The preparation window is three weeks. Local-first development maximizes implementation velocity and testability.

### Consequence

Cloud fluency is demonstrated through architecture notes, not premature deployment.

## ADR-003 — Core logic belongs in `src/`, not notebooks

### Decision

Notebooks may be used for exploration, but reusable logic must live in the package.

### Rationale

The target signal is engineering maturity.

### Consequence

Codex should move exploratory logic into modules before considering a task done.

## ADR-004 — Use DuckDB for local SQL modeling

### Decision

Use DuckDB for local SQL exercises.

### Rationale

DuckDB supports fast local analytical workflows and Parquet-friendly experimentation without a database server.

### Consequence

The SQL layer can remain reproducible and lightweight.

## ADR-005 — Use PySpark selectively

### Decision

Introduce Spark where distributed-processing reasoning matters: joins, shuffles, skew, partitioning, streaming semantics.

### Rationale

Spark should not be used just for tool theater. It should teach execution-model reasoning.

### Consequence

Small data volumes are acceptable if the examples expose distributed concepts deliberately.

## ADR-006 — Treat Azure as an architecture mapping first

### Decision

Map local components to Azure services after the local design works.

### Mapping

| Local component | Azure equivalent |
|---|---|
| Synthetic event feed | Event Hubs / Kafka-compatible ingestion |
| Local files | ADLS Gen2 |
| DuckDB/Parquet | Databricks + Delta Lake |
| PySpark jobs | Azure Databricks jobs |
| Local config | Key Vault / managed identity / environment config |
| Local logs | Azure Monitor / Log Analytics |
| CI checks | GitHub Actions / Azure DevOps |

### Consequence

You should be able to explain cloud architecture without getting trapped in environment setup.
