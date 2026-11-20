import pathlib
import pandas as pd


def extract(file_path: pathlib.Path | str) -> pd.DataFrame:
    """Extract the csv file and return the pandas dataframe

    Args:
        file_path (str): take the file path as string

    return:
        pd.DataFrame object

    example:
        customer_df = extract(file_path='datasets/customers.csv')
        print(customer_df.shape)
        (99441, 5)
    """

    return pd.read_csv(file_path)


# Checking folder path is exists or not
dataset_directory = pathlib.Path('datasets/brazilian-ecommerce/')

if not dataset_directory.is_dir():
    raise NotADirectoryError(f"Directory not found: {dataset_directory}")

# for storing all dataframes
dataframes = {}

# Iterating csv file paths and pass it to extract function for dataframes
for path in dataset_directory.glob(pattern='*.csv'):
    data_df = extract(file_path=path)
    # It store the dataframes of each csv files
    dataframes[path.stem] = data_df

if __name__ == '__main__':
    print(dataframes['olist_orders_dataset'].head())
