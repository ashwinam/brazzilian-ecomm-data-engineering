import pandas as pd
from sqlalchemy.engine import Connection

def load(df: pd.DataFrame, con: Connection, table_name: str) -> None:
    """Write the data into sql table using pandas dataframe.

    Args:
        df (pd.DataFrame): panda dataframe that load into sql table
        engine (Engine): sqlalachemy engine
        table_name (str): table name for storing data
    """
    df.to_sql(name=table_name, con=con, index=False, if_exists='append')