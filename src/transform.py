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

def transform_order_items(order_items_df: pd.DataFrame) -> pd.DataFrame:
    """Transform order items dataset

    Args:
        order_items_df (pd.DataFrame): original order items dataframe

    Returns:
        pd.DataFrame: transformed order items dataframe, its an copied dataframe of original dataframe
    """
    # copy the dataframe
    copied_order_items_df = order_items_df.copy()

    # change timestamp datatype of shipping_limit_date from str to datetime
    copied_order_items_df['shipping_limit_date'] = copied_order_items_df['shipping_limit_date'] = pd.to_datetime(copied_order_items_df['shipping_limit_date'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

    return copied_order_items_df
    