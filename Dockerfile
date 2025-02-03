FROM quay.io/astronomer/astro-runtime:12.6.0

# Install dbt into a virtual environment correctly
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-postgres
