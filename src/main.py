from extract import extract_all_datasets
from transform import transform_orders, transform_order_items, transform_reviews
import pathlib as pl
from load import load 
from database import get_engine
import os
from sqlalchemy import URL

def main():
    """
    Orchestrates the extraction and transformation pipeline.
    """
    # connecting engine
    db_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"]
    )
    engine = get_engine(db_url)

    # creating path object and pass it to extract all datasets
    dataset_directory = pl.Path('datasets/brazilian-ecommerce/')
    dataframes = extract_all_datasets(dataset_directory)

    # Getting the orders dataframe and transform it
    orders_df = dataframes['olist_orders_dataset']
    transformed_orders = transform_orders(orders_df)

    # transform order items dataframe
    order_items_df = dataframes['olist_order_items_dataset']
    transformed_order_items = transform_order_items(order_items_df)

    # transform reviews dataframe
    reviews_df = dataframes['olist_order_reviews_dataset']
    transformed_reviews_df = transform_reviews(reviews_df)

    # Load the final results to sql
    final_load = {
        'customers': dataframes['olist_customers_dataset'],
        'products': dataframes['olist_products_dataset'],
        'sellers': dataframes['olist_sellers_dataset'],
        'category_translation': dataframes['product_category_name_translation'],
        'geolocation': dataframes['olist_geolocation_dataset'],
        'orders': transformed_orders,
        'order_items': transformed_order_items,
        'order_payments': dataframes['olist_order_payments_dataset'],
        "order_reviews": transformed_reviews_df
    }

    for key, value in final_load.items():
        load(value, engine, key)

    return None

if __name__ == '__main__':
    main()