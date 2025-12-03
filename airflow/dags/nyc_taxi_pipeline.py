from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract.extract_nyc_taxi import extract_nyc_taxi
from scripts.transform.transform_nyc_taxi import transform_nyc_taxi
from scripts.load.load_nyc_taxi import load_nyc_taxi

with DAG(
    dag_id="nyc_taxi_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@monthly",
    catchup=False,
    default_args={"owner": "ahamed"}
):

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_nyc_taxi
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_nyc_taxi
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_nyc_taxi
    )

    extract >> transform >> load
