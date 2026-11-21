from extract import extract_all_datasets
from transform import transform_orders, transform_order_items
import pathlib as pl

def main():
    """
    Orchestrates the extraction and transformation pipeline.
    """
    # creating path object and pass it to extract all datasets
    dataset_directory = pl.Path('datasets/brazilian-ecommerce/')
    dataframes = extract_all_datasets(dataset_directory)

    # Getting the orders dataframe and transform it
    orders_df = dataframes['olist_orders_dataset']
    transformed_orders = transform_orders(orders_df)

    # transform order items dataframe
    order_items_df = dataframes['olist_order_items_dataset']
    transformed_order_items = transform_order_items(order_items_df)

    # validating outputs
    # orders
    assert orders_df.shape == transformed_orders.shape
    assert orders_df is not transformed_orders
    # order items
    assert order_items_df.shape == transformed_order_items.shape
    assert order_items_df is not transformed_order_items

if __name__ == '__main__':
    main()