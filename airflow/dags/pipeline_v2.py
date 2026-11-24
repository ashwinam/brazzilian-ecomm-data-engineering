import re
from pathlib import Path
from datetime import datetime
from airflow.sdk import get_current_context, task, DAG
from src.extract import extract_all_datasets

with DAG(dag_id='pipeline_v2', start_date=datetime(2026, 11,15), schedule=None, catchup=False):
    @task
    def extract():
        context = get_current_context()

        # Create a unique directory for this DAG run
        run_id = context["run_id"]
        safe_run_id = re.sub(r"[^a-zA-Z0-9_.-]", "_", run_id)

        output_dir = Path("/opt/airflow/shared") / safe_run_id
        output_dir.mkdir(parents=True, exist_ok=True)

        # Extract all datasets
        dataset_path = Path(
            "/opt/airflow/project/datasets/brazilian-ecommerce"
        )
        dataframes = extract_all_datasets(dataset_path)

        # Save each DataFrame as a CSV file
        for name, df in dataframes.items():
            df.to_csv(output_dir / f"{name}.csv", index=False)

        print(f"Extracted {len(dataframes)} datasets")
        print(f"Output directory: {output_dir}")

        return str(output_dir)

    @task
    def transform(input_dir: str):
        print(f"Transforming datasets from: {input_dir}")

    @task
    def validate():
        print("Validating orders...")

    @task
    def load():
        print("Loading data into postgresql.")

    extract_result = extract()

    transform_result = transform(extract_result)

    validate_result = validate()

    load_result = load()

    transform_result >> validate_result >> load_result