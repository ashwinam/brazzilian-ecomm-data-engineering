import pathlib
import pandas as pd

def extract(file_path: str):
    """Extract the csv file and return the pandas dataframe

    Args:
        file_path (str): take the file path as string
    
    return:
        pd.DataFrame object
    
    example:
        cust = extract(file_path='datasets/customers.csv')

    """

    return pd.read_csv(file_path)

if __name__ == '__main__':
    # Checking file path is exists or not
    customer_data_filepath = pathlib.Path('datasets/brazilian-ecommerce/olist_customers_dataset.csv')

    if not customer_data_filepath.is_file():
        raise FileNotFoundError(f"File not found: {customer_data_filepath}")

    # Collecting Customer DataFrame
    customer_df = extract(file_path=customer_data_filepath)
    print(customer_df.head()) 
    print(customer_df.shape)
    print(list(customer_df))
    print(customer_df.dtypes)