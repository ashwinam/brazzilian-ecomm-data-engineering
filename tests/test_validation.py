from tests.input_datas import sample_orders_df
import pandas as pd
from src.validate import validate_orders

def test_validate_orders_valid_data(sample_orders_df):
    """ 
    Verify this:
    1. Verify there are no missing IDs.
    2. Verify there are no duplicate order IDs.
    3. Verify there are no missing or invalid statuses.
    """

    result = validate_orders(sample_orders_df)

    assert result['null_order_id'] is False
    assert result['any_duplicates_orders_id'] is False
    assert result['validate_order_statuses'] is True 
    assert result['null_order_status'] is False
    