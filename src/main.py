from extract import extract_all_datasets
from transform import transform_orders
import pathlib as pl

def main():
    """Main pipeline function that joins the extraction and transformation functionality
    """
    # creating path object and pass it to extract all datasets
    dataset_directory = pl.Path('datasets/brazilian-ecommerce/')
    dataframes = extract_all_datasets(dataset_directory)

    # Getting the orders dataframe and transform it
    orders_df = dataframes['olist_orders_dataset']
    transformed_orders = transform_orders(orders_df)

    # validating outputs
    print(orders_df.shape)
    print(orders_df.dtypes)
    print()
    print(transformed_orders.shape)
    print(transformed_orders.dtypes)


if __name__ == '__main__':
    main()