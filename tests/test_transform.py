import pandas as pd
from src.transform import transform_orders, transform_order_items, transform_reviews
from tests.input_datas import sample_orders_df, sample_missing_timestamp_orders_df, sample_order_items_df, sample_missing_timestamps_order_items_df, sample_review_df,sample_missing_timestamp_review_df

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

def test_missing_timestamps_orders_df(sample_missing_timestamp_orders_df):

    missing_timestamp_df = transform_orders(sample_missing_timestamp_orders_df)

    assert \
    missing_timestamp_df['order_purchase_timestamp'].isna().sum() == 1 and \
    missing_timestamp_df['order_approved_at'].isna().sum() == 1 and \
    missing_timestamp_df['order_delivered_carrier_date'].isna().sum() == 0 and \
    missing_timestamp_df['order_delivered_customer_date'].isna().sum() == 2 and \
    missing_timestamp_df['order_estimated_delivery_date'].isna().sum() == 2

def test_rows_and_columns_counts_after_transformation_orders_df(sample_orders_df):
    result_df = transform_orders(sample_orders_df)

    assert result_df.shape == sample_orders_df.shape

# Order Items Unit Test
def test_order_items_original_df_unchanged(sample_order_items_df):
    # Arrange
    original_df = sample_order_items_df.copy(deep=True)

    # Act
    transform_order_items(sample_order_items_df)

    # Assert
    pd.testing.assert_frame_equal(sample_order_items_df, original_df)

def test_shipping_limit_date_datatype_to_datetime_datatype(sample_order_items_df):
    result_df = transform_order_items(sample_order_items_df)

    assert pd.api.types.is_datetime64_any_dtype(result_df['shipping_limit_date'])

def test_missing_timestamp_order_items_df(sample_missing_timestamps_order_items_df):
    result_df = transform_order_items(sample_missing_timestamps_order_items_df)

    assert result_df['shipping_limit_date'].isna().sum() == 2

def test_rows_and_columns_counts_after_transformation_order_items_df(sample_order_items_df):
    result_df = transform_order_items(sample_order_items_df)

    assert result_df.shape == sample_order_items_df.shape

# Reviews Unit Test
def test_reviews_original_df_unchanged(sample_review_df):
    # Arrange
    original_df = sample_review_df.copy(deep=True)

    # Act
    transform_reviews(sample_review_df)

    # Assert
    pd.testing.assert_frame_equal(sample_review_df, original_df)

def test_creation_date_and_answer_timestamp_check_datatype_datetime(sample_review_df):
    result_df = transform_reviews(sample_review_df)

    assert pd.api.types.is_datetime64_any_dtype(result_df['review_creation_date']) and \
    pd.api.types.is_datetime64_any_dtype(result_df['review_answer_timestamp'])

def test_missing_timestamp_reviews_df(sample_missing_timestamp_review_df):
    result_df = transform_reviews(sample_missing_timestamp_review_df)

    assert result_df['review_creation_date'].isna().sum() == 1 and \
    result_df['review_answer_timestamp'].isna().sum() == 2


def test_rows_and_columns_counts_after_transformation_reviews_df(sample_review_df):
    result_df = transform_reviews(sample_review_df)

    assert result_df.shape == sample_review_df.shape