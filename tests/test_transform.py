from tests.test_data import sample_orders_df, sample_missing_timestamp_orders_df
import pandas as pd
from src.transform import transform_orders

# Orders DataFrame Unit tests
def test_transform_does_not_modify_original_df(sample_orders_df):
    # Arrange
    original_df = sample_orders_df.copy(deep=True)
    # Act
    transform_orders(sample_orders_df)
    # Assert
    pd.testing.assert_frame_equal(sample_orders_df, original_df)

def test_after_transformed_datatypes(sample_orders_df):
    result_df = transform_orders(sample_orders_df)

    assert result_df['order_status'].dtype == 'category' and \
    pd.api.types.is_datetime64_any_dtype(result_df['order_purchase_timestamp']) and \
    pd.api.types.is_datetime64_any_dtype(result_df['order_approved_at']) and \
    pd.api.types.is_datetime64_any_dtype(result_df['order_delivered_carrier_date']) and \
    pd.api.types.is_datetime64_any_dtype(result_df['order_delivered_customer_date'])  and \
    pd.api.types.is_datetime64_any_dtype(result_df['order_estimated_delivery_date'])

def test_missing_timestamps(sample_missing_timestamp_orders_df):

    missing_timestamp_df = transform_orders(sample_missing_timestamp_orders_df)

    assert \
    missing_timestamp_df['order_purchase_timestamp'].isna().sum() == 1 and \
    missing_timestamp_df['order_approved_at'].isna().sum() == 1 and \
    missing_timestamp_df['order_delivered_carrier_date'].isna().sum() == 0 and \
    missing_timestamp_df['order_delivered_customer_date'].isna().sum() == 2 and \
    missing_timestamp_df['order_estimated_delivery_date'].isna().sum() == 2

def test_rows_and_columns_counts_after_transformation(sample_orders_df):
    result_df = transform_orders(sample_orders_df)

    assert result_df.shape == sample_orders_df.shape