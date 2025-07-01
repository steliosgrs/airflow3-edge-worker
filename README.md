# Setup Airflow 3 with Edge Worker

## Set Airflow 3

### Build Airflow images

The image we are using (and it is curretly the latest) is `3.0.2` .
Also the image contains the provider `edge3` for Edge Executor in the latest version `1.1.1`.

```bash
# Server Airflow
docker compose build
# Edge Worker
docker build -f edge.Dockerfile -t airflow-edge-worker .
```

### Start the Airflow 3 instance

```bash
# Start Server Airflow (first)
docker compose up
# Start Edge Worker
docker run -it --rm --name edge-worker -v dags:/opt/airflow/dags airflow-edge-worker
```

### Succeful Case

If the worker connects successfully to server, the edge worker starts to wait for a job from server

```bash
[2025-07-01T08:12:11.594+0000] {worker.py:318} INFO - No new job to process
[2025-07-01T08:12:16.664+0000] {worker.py:318} INFO - No new job to process
[2025-07-01T08:12:22.130+0000] {worker.py:318} INFO - No new job to process
```

## Important Issues

#### Bug Fix `edge_job_command_len`

Due to a bug mention and fixed you need to copy the correct file into the container

```bash
docker cp edge_executor.py  airflow3-edge-worker-airflow-scheduler-1:/home/airflow/.local/lib/python3.10/site-packages/airflow/providers/edge3/executors/edge_executor.py
```

or follow the steps:

[Issue - Got UnboundLocalError when I add EdgeExecutor into executor in Airflow3.0.2](https://github.com/apache/airflow/issues/52326)

**More Details**

- [PR - Fix UnboundLocalError for edge_job_command_len](https://github.com/apache/airflow/pull/52328)
- [Fix](https://github.com/apache/airflow/pull/52328/files)

#### Bug Fix `jwtSecret`

[Issue & Fix - Failed to start edge worker with 403 Client Error: Forbidden for url: https://<AIRFLOW-HOST>/edge_worker/v1/worker/<WORKER-IP>](https://github.com/apache/airflow/issues/52327)

https://github.com/apache/airflow/issues/51235
https://github.com/apache/airflow/issues/49646

## General Helpful Links / Guides

- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#)
- [docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/3.0.2/docker-compose.yaml)

```bash
docker cp scheduler_job_runner.py airflow3-edge-worker-airflow-scheduler-1:/home/airflow/.local/lib/python3.10/site-packages/airflow/jobs/scheduler_job_runner.py
```

https://github.com/apache/airflow/blob/87e34a69638e39c46697cd483249771ede793568/providers/edge3/src/airflow/providers/edge3/executors/edge_executor.py

https://github.com/apache/airflow/blob/87e34a69638e39c46697cd483249771ede793568/airflow-core/src/airflow/jobs/scheduler_job_runner.py#L2462

https://github.com/apache/airflow/blob/87e34a69638e39c46697cd483249771ede793568/airflow-core/src/airflow/executors/executor_loader.py
