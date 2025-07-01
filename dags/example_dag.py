import os

import pendulum

from airflow import DAG
from airflow.decorators import task
from airflow.example_dags.libs.helper import print_stuff
from airflow.settings import AIRFLOW_HOME
from airflow.providers.edge3.executors.edge_executor import EdgeExecutor
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="example_edge_pool_slots",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
    default_args={"executor": "EdgeExecutor", "queue": "libra-premises-gpu"},
) as dag:

    task = BashOperator(
        task_id="edge_task",
        bash_command='echo "Running on Edge"',
        executor="EdgeExecutor",
        executor_config={
            "executor": "EdgeExecutor",
            "queue": "libra-premises-gpu",
            # "pool_slots": 2,
            # EdgeExecutor-specific configuration
            # This will depend on what the EdgeExecutor supports
            # "edge_node": "node-1",
            # "resources": {"cpu": "500m", "memory": "1Gi"},
            # Add other EdgeExecutor-specific parameters
        },
    )
    task
    # @task(
    #     executor_config={
    #         "executor": "EdgeExecutor",
    #         "pool_slots": 2,
    #         "queue": "libra-premises-gpu",
    #     },
    #     # queue="default",
    # )
    # def task_with_template():
    #     print_stuff()

    # task_with_template()
