import pathlib
import pandas as pd


def extract(file_path: pathlib.Path | str) -> pd.DataFrame:
    """Extract the csv file and return the pandas dataframe

    Args:
        file_path (str): take the file path as string

    return:
        pd.DataFrame object

    example:
        cust = extract(file_path='datasets/customers.csv')
        print(customer_df.shape)
        (99441, 5)
    """

    return pd.read_csv(file_path)


if __name__ == '__main__':
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

    # inspecting datasets
    # for key, value in dataframes.items():
    #     # Investigating missing values

    #     # Getting datasets that has the null values
    #     # getting total column values for calculating total rows and columns
    #     column_with_nulls = value.columns[value.isna().any()].tolist()
    #     if column_with_nulls:
    #         print(key) # dataset name
    #         # Getting columns that has null values
    #         for column_name in column_with_nulls:
    #             # Calculating percentage for null values
    #             null_counts = value[column_name].isna().sum()
    #             total_count = value.shape[0]
    #             null_value_percentage = (null_counts / total_count) * 100
    #             print(
    #                 f"{column_name}: {null_counts} missing values "
    #                 f"({null_value_percentage:.2f}%)"
    #             )

    #         print() # for new line

    # Investigating orders dataset for order_delivered_customer_date, by checking orders status column and other things
    orders_df = dataframes['olist_orders_dataset']

    null_rows = orders_df[orders_df['order_delivered_customer_date'].isna()]

    filtered_null_rows = null_rows.loc[
        :, 
            [
                
                'order_id', 
                'customer_id', 
                'order_status', 
                'order_approved_at',
                'order_purchase_timestamp', 
                'order_delivered_carrier_date', 'order_delivered_customer_date'
                
            ]
        ]

    # print(filtered_null_rows['order_status'].value_counts()) # check the order status wise counts

    print(filtered_null_rows[filtered_null_rows['order_status'] == 'delivered'])

    print(filtered_null_rows[(filtered_null_rows['order_status'] == 'delivered') & (filtered_null_rows['order_delivered_carrier_date'].isna())])

    print(filtered_null_rows[(filtered_null_rows['order_status'] == 'delivered') & (filtered_null_rows['order_approved_at'].isna())])
