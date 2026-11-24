from datetime import datetime

from airflow.sdk import dag, task, DAG

@dag(
    dag_id="first_dag",
    start_date=datetime(2026, 11,15),
    schedule=None,
    catchup=None
)

def first_dag():
    @task
    def extract():
        print("Extracting olist data.")

    @task
    def transform():
        print("Transforming olist data.")

    @task
    def load():
        print("Loaing data into postgresql,")

    extract() >> transform() >> load()


first_dag()

with DAG(dag_id='pipeline_v2', start_date=datetime(2026, 11,15), schedule=None, catchup=None):
    @task
    def extract():
        print("Extracting olist data.")

    @task
    def transform():
        print("Transforming olist data.")

    @task
    def validate():
        print("Validating orders...")

    @task
    def load():
        print("Loaing data into postgresql,")

    extract() >> transform() >> validate() >> load()