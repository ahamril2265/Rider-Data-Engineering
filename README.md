# Rider Data Engineering — NYC Taxi Pipeline (Flagship Project)

This is an enterprise-level data engineering project built using:

- Apache Airflow (ETL orchestration)
- Python (data processing)
- PostgreSQL / DuckDB / BigQuery (warehouse)
- NYC Taxi Trip Data (real dataset)
- Docker (containerization)
- Data Lakes (Bronze → Silver → Gold architecture)

## Project Architecture

Extract → Transform → Load pipeline:
1. **Bronze Layer (Raw Data)**  
   Download monthly NYC Taxi CSV/Parquet files.

2. **Silver Layer (Cleaned Data)**  
   Standardize schema, handle missing values, fix datatypes.

3. **Gold Layer (Analytics Ready)**  
   Aggregations: hourly trips, fare distribution, heatmaps, etc.

## Airflow DAG

`nyc_taxi_pipeline.py`  
This orchestrates:
- extract_nyc_taxi
- transform_nyc_taxi
- load_nyc_taxi

## Future Enhancements
- Kafka streaming ingestion
- dbt for warehouse modeling
- Spark for big transformations
- Full CI/CD with GitHub Actions
