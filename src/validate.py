import pandas as pd

def validate_orders(orders_df: pd.DataFrame) -> dict:
    """Validate orders dataframe, for quality data

    Args:
        orders_df (pd.DataFrame): orders dataframe

    Returns:
        dict: returns result in a dictionary format for reporting purposes
    """
    # check null values
    null_order_id = bool(orders_df['order_id'].isna().any())
    null_customer_id = bool(orders_df['customer_id'].isna().any())

    # check uniqueness and duplicates
    unique_order_id_count = orders_df['order_id'].nunique()
    any_duplicates_orders_id = bool(orders_df['order_id'].duplicated(keep=False).any())
    duplicate_order_id_count = orders_df['order_id'].duplicated().sum()

    # validate order statuses
    statuses = [
        'delivered',
        'shipped',
        'canceled',
        'unavailable',
        'invoiced',
        'processing',
        'created',
        'approved'
    ]

    validate_order_statuses = bool(orders_df['order_status'].isin(statuses).all())
    null_order_status = bool(orders_df['order_status'].isna().any())

    result = {
        'null_order_id': null_order_id,
        'null_customer_id': null_customer_id,
        'unique_order_id_count': unique_order_id_count,
        'any_duplicates_orders_id': any_duplicates_orders_id,
        'duplicate_order_id_count': duplicate_order_id_count,
        'validate_order_statuses': validate_order_statuses,
        'null_order_status': null_order_status
    }

    return result