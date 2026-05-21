# Insurance Claims Analytics Platform

End-to-end cloud data engineering project simulating an enterprise insurance claims analytics platform.

## Business Problem
Insurance claims reporting is slow because claims data arrives from multiple systems in different formats such as CSV, JSON, and Parquet. Business teams need clean, standardized, analytics-ready data for faster claim analysis and reporting.

## Solution
This project builds an ETL/ELT pipeline that:
- ingests raw claims, policy, and customer data,
- standardizes schemas using PySpark,
- performs data quality checks,
- loads curated data into Snowflake,
- builds Silver and Gold analytics models,
- orchestrates the workflow using Airflow,
- prepares reporting-ready tables for Power BI.

## Tech Stack
- Python
- PySpark
- AWS Glue-style ETL
- Amazon S3-style data lake
- Snowflake
- Apache Airflow
- dbt
- SQL
- Docker
- GitHub Actions

## Architecture

Source Systems → S3 Raw Layer → PySpark ETL → Snowflake Bronze/Silver/Gold → Power BI Reporting

## Key Features
- Multiple input formats: CSV and JSON
- Schema standardization
- Deduplication
- Null handling
- Claims aggregation
- Data quality validation
- Snowflake table design
- Airflow DAG orchestration
- dbt-style transformations
- CI workflow placeholder

## Project Result
The pipeline produces clean analytics-ready claims datasets that can support dashboards for:
- claim volume trends,
- claim approval/rejection rate,
- average claim settlement amount,
- processing delays,
- policy-level claim analysis.

## Repository Structure
```text
insurance-claims-analytics-platform/
├── airflow/dags/
├── pyspark_jobs/
├── snowflake/
├── dbt/models/
├── tests/
├── docs/
├── data/
└── README.md
```

## Interview Story
This project represents a realistic enterprise data engineering workflow similar to insurance claims analytics use cases. It demonstrates ETL pipeline development, schema standardization, Snowflake analytics modeling, data quality validation, and stakeholder-driven reporting.
