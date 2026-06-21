# NYC Taxi Data Platform

A production-inspired Data Engineering project that processes NYC Taxi trip records using Apache Airflow, Python, PostgreSQL, and a Medallion Architecture (Bronze → Silver → Gold).

---

## Project Goal

This project demonstrates how modern data platforms ingest, transform, validate, and serve large-scale transportation datasets for analytics.

The pipeline processes NYC Taxi trip data and produces analytics-ready datasets for reporting and business intelligence.

---

## Architecture

```text
NYC Taxi Dataset
        │
        ▼
 ┌─────────────┐
 │ Bronze      │
 │ Raw Data    │
 └──────┬──────┘
        │
        ▼
 ┌─────────────┐
 │ Silver      │
 │ Clean Data  │
 └──────┬──────┘
        │
        ▼
 ┌─────────────┐
 │ Gold        │
 │ Analytics   │
 └──────┬──────┘
        │
        ▼
 PostgreSQL
        │
        ▼
 Dashboards
```

---

## Tech Stack

| Category | Technology |
|-----------|-----------|
| Language | Python |
| Orchestration | Apache Airflow |
| Storage | Parquet |
| Database | PostgreSQL |
| Containerization | Docker |
| Analytics | SQL |

---

## Pipeline Workflow

```text
extract_nyc_taxi
        │
        ▼
transform_nyc_taxi
        │
        ▼
load_nyc_taxi
```

---

## Features

### Bronze Layer

- Raw trip ingestion
- Immutable storage
- Historical snapshots

### Silver Layer

- Data cleaning
- Schema standardization
- Quality validation

### Gold Layer

- Revenue analytics
- Trip aggregation
- Geographic insights

### Orchestration

- Airflow scheduling
- Retry policies
- Dependency management

---

## Future Enhancements

- Kafka Streaming
- Spark Processing
- dbt Modeling
- Data Quality Framework
- Grafana Monitoring
- CI/CD Pipelines

---

## Author

Ahamed Rilwan

GitHub: https://github.com/ahamril2265

LinkedIn: https://linkedin.com/in/ahamedrilwan
