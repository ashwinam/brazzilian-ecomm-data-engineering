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

def extract_all_datasets(directory_path: pathlib.Path) -> dict:
    """This function extract all csv files and pass it to extract function and return the Dataframes and store it in a dictionary

    Args:
        directory_path (pathlib.Path | str): takes a directory path as pathlib.path object

    Raises:
        NotADirectoryError: If it's not directory then raise an error

    Returns:
        dict: returns dict of dataframes extracted from directiry
    """
    if not directory_path.is_dir():
        raise NotADirectoryError(f"Directory not found: {directory_path}")

    # for storing all dataframes
    dataframes = {}

    # Iterating csv file paths and pass it to extract function for dataframes
    for path in directory_path.glob(pattern='*.csv'):
        data_df = extract(file_path=path)
        # It store the dataframes of each csv files
        dataframes[path.stem] = data_df

    return dataframes

if __name__ == '__main__':
    # Checking folder path is exists or not
    dataset_directory = pathlib.Path('datasets/brazilian-ecommerce/')
    dataframes = extract_all_datasets(dataset_directory)
    print(dataframes['olist_orders_dataset'].head())
