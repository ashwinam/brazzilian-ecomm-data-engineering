import os
import logging
import pathlib as pl
from sqlalchemy import URL
from extract import extract_all_datasets
from transform import transform_orders, transform_order_items, transform_reviews
from validate import validate_orders
from load import load 
from database import clear_table, get_engine
from dotenv import load_dotenv

load_dotenv()

# 1. Create the 'logs' folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Logging module configuration
logging.basicConfig(
    filename='logs/pipeline.log', 
    level=logging.DEBUG, 
    format='%(asctime)s | %(levelname)s | %(message)s'
    )

def main():
    """
    Orchestrates the ETL  pipeline.
    """
    logging.debug("Process starts")
    
    engine = None
    try:
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
        logging.info("connecting dataset folder")
        # creating path object and pass it to extract all datasets
        dataset_directory = pl.Path('datasets/brazilian-ecommerce/')
        logging.info("Extraction process starts:")
        dataframes = extract_all_datasets(dataset_directory)

        # Getting the orders dataframe and transform it
        logging.info("Transforming orders.")
        orders_df = dataframes['olist_orders_dataset']
        transformed_orders = transform_orders(orders_df)

        # transform order items dataframe
        logging.info("Transforming order items")
        order_items_df = dataframes['olist_order_items_dataset']
        transformed_order_items = transform_order_items(order_items_df)

        # transform reviews dataframe
        logging.info("Transforming reviews.")
        reviews_df = dataframes['olist_order_reviews_dataset']
        transformed_reviews_df = transform_reviews(reviews_df)

        # validate orders
        validate_orders(orders_df)

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

        logging.info("Loading transformed dataframes into sql table.")
        delete_order = [
            'order_reviews',
            'order_payments',
            'order_items',
            'orders',
            'geolocation',
            'category_translation',
            'sellers',
            'products',
            'customers'
        ]
        with engine.begin() as conn:
            # clear the tables
            for table in delete_order:
                clear_table(conn, table)
            # load the data into tables
            for key, value in final_load.items():
                logging.info(f"{key} is now processing...")
                load(value, conn, key)
    except Exception:
        logging.exception("pipeline failed.")
        raise
    finally:
        if engine is not None:
            engine.dispose()

    logging.info("Pipeline completed successfully.")

    return None

if __name__ == '__main__':
    main()