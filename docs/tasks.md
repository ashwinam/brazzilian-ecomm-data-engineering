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

# Task 06 - Investigate Product Information
Let's move to olist_products_dataset.

- [x] load the `olist_products_dataset`
- [x] display these columns
      - product_category_name
      - product_name_lenght
      - product_description_lenght
      - product_photos_qty
- [x] Filter products where product_category_name is missing.
- [x] Check whether the other three columns are also missing in those same records.
- [x] Count how many products have all four fields missing.
- [x] Check whether product_id is missing in any of these records.

# Task 07 - Transform the Orders dataset
- [x] Investigate the current data types of the order dataset(timestamps)
- [x] Determine what needs to change before storing it in postgresql

# Task 08 — Investigate order timestamp consistency

### Part 1 — Investigate chronological consistency
- [x] Approval timestamp is earlier than purchase timestamp.
- [x] Carrier delivery timestamp is earlier than approval timestamp.
- [x] Customer delivery timestamp is earlier than carrier delivery timestamp.
- [x] Customer delivery timestamp is earlier than purchase timestamp.

### Part 2 — Investigate estimated delivery
- [x] Estimated delivery date is earlier than purchase date.
- [x] Actual customer delivery is later than the estimated delivery date.

### Part 3 — Report your findings
- [x] Number of affected records.
- [x] A few sample records (order_id and relevant timestamps).

# Task 09 — Create the Orders transformation module

- [x] create a transform.py file
- [x] create a function for orders transform_orders(orders_df)
- [x] give the appropriate data types to those columns
    - Requirements
      1. Accept a Pandas DataFrame as input.
      2. Return a transformed DataFrame.
      3. Do not modify the original input DataFrame.
      4. Preserve missing timestamp values.
      5. Keep the function reusable. It should work regardless of which CSV file path was used to extract the data.
- [x] Import your function into 01_data_exploration.ipynb and test it.
    - Verify:
      - The returned DataFrame has the expected dtypes.
      - The original DataFrame remains unchanged.
      - The number of rows remains the same.
      - Missing timestamp counts remain unchanged.

# Task 10 - Test transform_order functionality

- [x] Original DataFrame remains unchanged
    - Call transform_orders().
    - Verify that the original DataFrame has not been modified.
- [x] Correct data types
    - order_status should be a category.
    - All five timestamp columns should have a datetime dtype.
- [x] Missing timestamps
    - Create a small test DataFrame containing a missing timestamp.
    - Verify that it remains NaT after transformation.
- [x] Row and column counts
    - Verify that transformation doesn't unexpectedly change the DataFrame's shape.

# Task 11 - Integrate extraction and transformation

### Part 1 — Make extraction reusable
- [x] convert dataframe dictionary extraction into a function

### Part 2 — Integrate the modules
- [x] Create a small script, perhaps src/main.py
    - [x] Imports extract_all_datasets() from extract.py.
    - [x] Imports transform_orders() from transform.py.
    - [x] Extracts all CSV datasets into a dictionary.
    - [x] Retrieves olist_orders_dataset from that dictionary.
    - [x] Transforms the orders DataFrame.
    - [x] Prints the original and transformed shapes and dtypes.

# Task 12 - Build transform_order_items()

- [x] create `transform_order_items` function
- [x] Create a copy rather than modifying the original.
- [x] Convert `shipping_limit_date` to datetime.
- [x] returned transformed dataframe.

### added tasks to task no 12 - Unit Test
- [x] Original DataFrame remains unchanged.
- [x] `shipping_limit_date` becomes a datetime dtype.
- [x] Existing missing timestamps remain missing.
- [ ] Row and column counts remain unchanged.

# Task 13 — Investigate the products dataset

- [x] Data types of every column.
- [x] Missing values in every column.
- [x] Duplicate rows.
- [x] Missing product_id values.
- [x] Zero or negative values in:
      - product_name_lenght
      - product_description_lenght
      - product_photos_qty
      - product_weight_g
      - product_length_cm
      - product_height_cm
      - product_width_cm

# Task 14 — Review the remaining datasets

- [x] Data types of all columns.
- [x] Missing values.
- [x] Duplicate rows.
- [x] Zero or negative values in payment_sequential, payment_installments, and payment_value.

# Task 15 — Build transform_reviews()

- [x] Accept a Pandas DataFrame.
- [x] Copy the original DataFrame.
- [x] Convert review_creation_date to datetime.
- [x] Convert review_answer_timestamp to datetime.
- [x] Preserve missing values.
- [x] Return the transformed DataFrame.

# Task 16 - Build validate orders

- [x] Check NULL values
    - order_id must not contain NULL values.
    - customer_id must not contain NULL values.
- [x] Check uniqueness
    - order_id must be unique.
    - Identify duplicate order IDs.
- [x] Validate order status
    - identify any unexpected statuses
- [x] return validation result
    - create a dictionary and return the results

### part B - write pytest test for validate_orders()

- [x] Valid data passes
- [x] Duplicate order IDs are detected.
- [x] Missing IDs are detected.
- [x] Missing statuses are detected.
- [x] Unexpected statuses are detected.

# TASK 17 - Postgresql setup and table creation

- [x] create tables with relationship using er diagram.