from sqlalchemy import URL, create_engine, Engine, text
from dotenv import load_dotenv
from sqlalchemy.engine import Connection
import os
import logging

load_dotenv()

# postgresql://user:password@host:5432/dbname	5432

def get_engine(db_uri: str) -> Engine:
    """create the postgresql connection and return engine

    Args:
        db_uri (str): takes as an db_uri

    Returns:
        Engine: sqlalchemy engine
    """
    return create_engine(db_uri)

def clear_table(con: Connection, table: str):
    logging.info(f"Deleting records from {table}")
    con.execute(text(f'DELETE FROM {table}'))
    logging.info(f"Deleting records from {table}")

if __name__ == '__main__':
    db_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"]
    )

    engine = get_engine(db_url)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print(result.fetchone())
