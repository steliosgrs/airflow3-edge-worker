import os

import pendulum

from airflow import DAG
from airflow.decorators import task
from airflow.example_dags.libs.helper import print_stuff
from airflow.settings import AIRFLOW_HOME

with DAG(
    dag_id="example_edge_pool_slots",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task(queue="default")
    def task_with_template():
        print_stuff()

    task_with_template()
