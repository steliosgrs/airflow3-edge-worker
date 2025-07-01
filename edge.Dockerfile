FROM python:3.10-slim-bullseye

# Install Airflow and Edge provider
RUN pip install --no-cache-dir \
    apache-airflow==3.0.2 \
    apache-airflow-providers-edge3[fab]==1.1.1

# Create airflow user and directories
RUN useradd -ms /bin/bash airflow && \
    mkdir -p /opt/airflow-edge/dags /opt/airflow-edge/config && \
    chown -R airflow:airflow /opt/airflow-edge

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow-edge
ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags

# Minimum required environment variables for edge worker
ENV AIRFLOW__CORE__EXECUTOR=airflow.providers.edge3.executors.EdgeExecutor
# ENV AIRFLOW__CORE__INTERNAL_API_SECRET_KEY=b3kAmMbnMKS31iH8jxMhu6WRYWhVSQ31do0LrAZtBck
ENV AIRFLOW__API_AUTH__JWT_SECRET=v6NXpLFRTeo20bF+X2R6Eg== 
ENV AIRFLOW__OPERATORS__DEFAULT_QUEUE=libra-premises-gpu
ENV AIRFLOW__EDGE__API_URL="http://host.docker.internal:8080/edge_worker/v1/rpcapi"

ENV jwtSECRET=v6NXpLFRTeo20bF+X2R6Eg== 
USER airflow
WORKDIR /opt/airflow-edge

RUN airflow db migrate
# Start edge worker by default
CMD ["bash"]