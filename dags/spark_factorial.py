from datetime import datetime

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    "owner": "airflow",
}


dag = DAG(
    dag_id="spark_factorial",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["lab2", "spark"],
)


spark_job = SparkSubmitOperator(
    task_id="spark_factorial_job",
    application="/opt/airflow/spark/spark_factorial_job.py",
    name="spark_factorial_job",
    conn_id="spark_local",
    dag=dag,
)


spark_job
