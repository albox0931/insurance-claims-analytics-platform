from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="insurance_claims_pipeline",
    default_args=default_args,
    description="Insurance claims ETL pipeline using PySpark and Snowflake",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    clean_claims = BashOperator(
        task_id="clean_claims_data",
        bash_command="spark-submit pyspark_jobs/clean_claims_data.py",
    )

    standardize_schema = BashOperator(
        task_id="standardize_schema",
        bash_command="spark-submit pyspark_jobs/standardize_schema.py",
    )

    aggregate_claims = BashOperator(
        task_id="claims_aggregations",
        bash_command="spark-submit pyspark_jobs/claims_aggregations.py",
    )

    clean_claims >> standardize_schema >> aggregate_claims
