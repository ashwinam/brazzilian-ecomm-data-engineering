import pandas as pd

def transform_orders(orders_df: pd.DataFrame) -> pd.DataFrame:
    """transform orders function takes the input as the pandas dataframe and perform transformations on orders dataframe and returns result  pandas datafram.

    Args:
        orders_df (pd.DataFrame): orders_df is an panda dataframe that used in transformation process

    Returns:
        pd.DataFrame: end result comes as pandas dataframe.
    """
    final_df = orders_df.copy()
    # Changing datatypes of required columns.
    final_df['order_status'] = final_df['order_status'].astype('category')

    # Changing timestamps datatypes.
    timestamp_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
    ]

    for column in timestamp_columns:
        final_df[column] = pd.to_datetime(
            final_df[column],
            format="%Y-%m-%d %H:%M:%S",
            errors='coerce'
        )

    return final_df