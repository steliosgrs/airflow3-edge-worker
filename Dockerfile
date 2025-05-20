FROM apache/airflow:3.0.1

USER airflow

# Install the Google Cloud Storage package
RUN pip install --no-cache-dir google-cloud-storage 