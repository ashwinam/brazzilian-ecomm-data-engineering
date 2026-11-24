
import os
import re
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd

from airflow.sdk import DAG, task, get_current_context

from src.extract import extract_all_datasets
from src.transform import (
    transform_orders,
    transform_order_items,
    transform_reviews,
)
from src.validate import validate_orders
from src.load import load
from src.database import get_engine, clear_table

DATASET_PATH = Path(
    "/opt/airflow/project/datasets/brazilian-ecommerce"
)

SHARED_PATH = Path("/opt/airflow/shared")


with DAG(
    dag_id="pipeline_v2",
    start_date=datetime(2026, 11, 15),
    schedule=None,
    catchup=False,
    tags=["olist", "data-engineering"],
) as dag:

    @task
    def extract() -> str:
        """Extract all source CSV files and save them to shared storage."""

        context = get_current_context()
        run_id = context["run_id"]
        safe_run_id = re.sub(r"[^a-zA-Z0-9_.-]", "_", run_id)

        output_dir = SHARED_PATH / safe_run_id
        output_dir.mkdir(parents=True, exist_ok=True)

        dataframes = extract_all_datasets(DATASET_PATH)

        for name, df in dataframes.items():
            df.to_csv(output_dir / f"{name}.csv", index=False)

        logging.info("Extracted %s datasets", len(dataframes))
        logging.info("Extraction output: %s", output_dir)

        return str(output_dir)

    @task
    def transform(input_dir: str) -> str:
        """Transform the required datasets and save all datasets."""

        input_path = Path(input_dir)
        output_path = input_path / "transformed"
        output_path.mkdir(parents=True, exist_ok=True)

        # Read all extracted datasets
        dataframes = {
            file.stem: pd.read_csv(file)
            for file in input_path.glob("*.csv")
        }

        # Transform orders
        dataframes["olist_orders_dataset"] = transform_orders(
            dataframes["olist_orders_dataset"]
        )

        # Transform order items
        dataframes["olist_order_items_dataset"] = transform_order_items(
            dataframes["olist_order_items_dataset"]
        )

        # Transform reviews
        dataframes["olist_order_reviews_dataset"] = transform_reviews(
            dataframes["olist_order_reviews_dataset"]
        )

        # Save all datasets, including unchanged datasets
        for name, df in dataframes.items():
            df.to_csv(output_path / f"{name}.csv", index=False)

        logging.info("Transformed datasets saved to %s", output_path)

        return str(output_path)

    @task
    def validate(input_dir: str) -> dict:
        """Validate the transformed orders dataset."""

        orders_path = Path(input_dir) / "olist_orders_dataset.csv"
        orders_df = pd.read_csv(orders_path)

        results = validate_orders(orders_df)

        # These checks must pass before loading.
        required_checks = [
            "null_order_id",
            "null_customer_id",
            "any_duplicates_orders_id",
            "validate_order_statuses",
            "null_order_status",
        ]

        failed_checks = [
            check
            for check in required_checks
            if (
                not results[check]
                if check == "validate_order_statuses"
                else results[check]
            )
        ]

        logging.info("Validation results: %s", results)

        if failed_checks:
            raise ValueError(
                f"Order validation failed: {failed_checks}"
            )

        logging.info("All required validation checks passed")

        return results

    @task
    def load_data(input_dir: str, validation_results: dict) -> None:
        """Load validated datasets into PostgreSQL using full refresh."""

        logging.info(
            "Validation passed. Starting PostgreSQL full refresh."
        )

        input_path = Path(input_dir)

        # Read transformed datasets
        final_load = {
            "customers": pd.read_csv(
                input_path / "olist_customers_dataset.csv"
            ),
            "products": pd.read_csv(
                input_path / "olist_products_dataset.csv"
            ),
            "sellers": pd.read_csv(
                input_path / "olist_sellers_dataset.csv"
            ),
            "category_translation": pd.read_csv(
                input_path / "product_category_name_translation.csv"
            ),
            "geolocation": pd.read_csv(
                input_path / "olist_geolocation_dataset.csv"
            ),
            "orders": pd.read_csv(
                input_path / "olist_orders_dataset.csv",
                parse_dates=[
                    "order_purchase_timestamp",
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                ],
            ),
            "order_items": pd.read_csv(
                input_path / "olist_order_items_dataset.csv",
                parse_dates=["shipping_limit_date"],
            ),
            "order_payments": pd.read_csv(
                input_path / "olist_order_payments_dataset.csv"
            ),
            "order_reviews": pd.read_csv(
                input_path / "olist_order_reviews_dataset.csv",
                parse_dates=[
                    "review_creation_date",
                    "review_answer_timestamp",
                ],
            ),
        }

        # Delete child tables before parent tables.
        delete_order = [
            "order_reviews",
            "order_payments",
            "order_items",
            "orders",
            "geolocation",
            "category_translation",
            "sellers",
            "products",
            "customers",
        ]

        db_url = {
            "drivername": "postgresql+psycopg",
            "username": os.environ["DB_USER"],
            "password": os.environ["DB_PASSWORD"],
            "host": os.environ["DB_HOST"],
            "port": int(os.environ["DB_PORT"]),
            "database": os.environ["DB_NAME"],
        }

        from sqlalchemy import URL

        engine = get_engine(URL.create(**db_url))

        try:
            # All deletes and inserts belong to one transaction.
            with engine.begin() as conn:

                for table in delete_order:
                    clear_table(conn, table)

                # Insert parent tables before child tables.
                for table_name, df in final_load.items():
                    logging.info(
                        "Loading %s (%s rows)",
                        table_name,
                        len(df),
                    )
                    load(df, conn, table_name)

            logging.info("PostgreSQL full refresh completed")

        finally:
            engine.dispose()

    # Define task dependencies and pass outputs between tasks.
    extracted_dir = extract()

    transformed_dir = transform(extracted_dir)

    validation_results = validate(transformed_dir)

    load_data(transformed_dir, validation_results)
