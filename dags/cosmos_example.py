from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


# PostgreSQL profile configuration
profile_config = ProfileConfig(
    profile_name="my_dbt_project",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_conn",
        profile_args={
            "host": "172.18.0.1",
            "port": 5433,
            "user": "my_user",
            "password": "my_password",
            "dbname": "my_database",
            "schema": "public"
        }
    )
)


dbt_example = DbtDag(project_config=ProjectConfig("/usr/local/airflow/dags/dbt/my_dbt_project",),
                    operator_args={"install_deps": True},
                    profile_config=profile_config,
                    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
                    schedule_interval="@daily",
                    start_date=datetime(2023, 9, 10),
                    catchup=False,
                    dag_id="dbt_example",)