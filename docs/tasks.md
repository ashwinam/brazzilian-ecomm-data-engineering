# Task 01

- [x] Create extract python file
- [x] Start with one Data File
- [x] Locate the csv file using its path
- [x] Check whether the file exists
- [x] Read it using pandas
- [x] Display:
  - First five records
  - Number of rows and columns
  - Column names
  - Data types

# Task 02 — Extract all Olist datasets

- [x] Discover all CSV files inside datasets/brazilian-ecommerce/
- [x] Read each CSV using your existing extract() function.
- [x] Keep the resulting DataFrames accessible.
- [x] Display each dataset's name and shape.

# Task 03 - Inspect the extracted datasets

- [x] return the dataset name
- [x] Shape - number of rows and columns
- [x] column names
- [x] Data Types, data types of each column
- [x] Missing values, Count of missing column in each column 

# Task 04 - Investigate missing values

- [x] Identify which dataset contains missing values
- [x] Identify columns with missing values
- [x] Calculate the missing values percentage

# Task 05 — Investigate missing order dates
Let's investigate `olist_orders_dataset` first.

- [x] Load the orders DataFrame from your existing dictionary.
- [x] Find the rows where order_delivered_customer_date is missing.
- [x] Display these columns:
        - order_id
        - customer_id
        - order_status
        - order_purchase_timestamp
        - order_delivered_carrier_date
        - order_delivered_customer_date
- [x] Count how many records belong to each order_status among these rows.

## Further Investigation in task 05
- [x] Filter only records where `order_status` == 'delivered'
- [x] Display all six columns you selected earlier.
- [x] Check whether `order_delivered_carrier_date` is also missing for these eight records.
- [x] Check whether order_approved_at is missing for them.