FROM apache/airflow:3.4.0-python3.13

RUN pip install --no-cache-dir \
    "apache-airflow==${AIRFLOW_VERSION}" \
    --constraint "${HOME}/constraints.txt" \
    pandas \
    "psycopg[binary]" \
    python-dotenv
