from extract import extract_all_datasets
from transform import transform_orders
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

    # validating outputs
    assert orders_df.shape == transformed_orders.shape
    assert orders_df is not transformed_orders


if __name__ == '__main__':
    main()