# E-commerce Data Engineering Pipeline 

An end-to-end batch data engineering pipeline built using **Python, Pandas, SQLAlchemy, and PostgreSQL** to extract, transform, and load Brazilian e-commerce data from the Olist dataset.

This project is part of my journey from Software Engineering to Data Engineering. The objective is to build a practical data pipeline while applying real-world engineering concepts such as modular code, data quality investigation, database constraints, transaction management, and logging.

## Architecture

```text
       Olist CSV Datasets
               |
               v
       Extraction (Python)
               |
               v
    Transformation (Pandas)
               |
               v
       PostgreSQL Loading
               |
               v
       PostgreSQL Database
```

The pipeline uses a **full-refresh batch loading strategy**. Existing records are deleted and the latest dataset is loaded within a single database transaction.

## Tech Stack

- **Python** – Pipeline development
- **Pandas** – Data extraction and transformation
- **PostgreSQL** – Relational database
- **SQLAlchemy** – Database connectivity and transaction management
- **Psycopg** – PostgreSQL driver
- **python-dotenv** – Environment variable management
- **pytest** – Unit testing
- **Logging** – Pipeline execution monitoring

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

It contains nine CSV datasets:

| Dataset | Description |
|---|---|
| Customers | Customer information |
| Orders | Order details and statuses |
| Order Items | Products associated with orders |
| Products | Product attributes |
| Sellers | Seller information |
| Order Payments | Payment details |
| Order Reviews | Customer reviews |
| Geolocation | Brazilian ZIP code coordinates |
| Category Translation | Portuguese-to-English category mapping |

## Project Features

### 1. Data Extraction
- Extracts all nine CSV datasets using Python and Pandas.
- Uses `pathlib` for filesystem operations.
- Keeps extraction logic reusable and separate from pipeline orchestration.

### 2. Data Investigation and Transformation
- Inspects dataset structures, data types, and missing values.
- Investigates anomalies before deciding how to handle them.
- Converts relevant timestamp columns into appropriate datetime types.
- Uses reusable transformation functions.
- Preserves the original DataFrames during transformations.

### 3. Data Validation and Testing
- Implements basic order dataset validation.
- Writes unit tests using pytest.
- Tests transformations, data types, missing values, and whether original DataFrames remain unchanged.

### 4. PostgreSQL Integration
- Designs a relational schema containing nine tables.
- Defines primary keys, composite primary keys, and foreign key relationships.
- Connects Python to PostgreSQL using SQLAlchemy.
- Loads Pandas DataFrames into their corresponding database tables.

### 5. Pipeline Reliability
- Implements full-refresh loading.
- Deletes existing records in foreign-key dependency order.
- Loads records in parent-to-child dependency order.
- Uses database transactions to ensure deletes and inserts succeed or roll back together.
- Handles exceptions and manages database engine resources.

### 6. Logging
- Records pipeline execution steps.
- Captures errors and exception tracebacks.
- Maintains execution logs for troubleshooting.

## Database Tables

The pipeline loads data into the following nine PostgreSQL tables:

```text
customers
orders
order_items
products
sellers
order_payments
order_reviews
geolocation
category_translation
```

**Latest successful execution:** 1,550,922 records loaded across all nine tables.

| Table | Records |
|---|---:|
| customers | 99,441 |
| orders | 99,441 |
| products | 32,951 |
| sellers | 3,095 |
| order_items | 112,650 |
| order_payments | 103,886 |
| order_reviews | 99,224 |
| geolocation | 1,000,163 |
| category_translation | 71 |
| **Total** | **1,550,922** |

## Project Structure

```text
brazilian-ecomm-data-engineering/
│
├── datasets/
│   └── brazilian-ecommerce/
│       ├── olist_customers_dataset.csv
│       ├── olist_geolocation_dataset.csv
│       ├── olist_order_items_dataset.csv
│       ├── olist_order_payments_dataset.csv
│       ├── olist_order_reviews_dataset.csv
│       ├── olist_orders_dataset.csv
│       ├── olist_products_dataset.csv
│       ├── olist_sellers_dataset.csv
│       └── product_category_name_translation.csv
│
├── docs/
│   ├── images/
│   ├── tasks.md
│   └── technical-design.md
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   └── main.py
│
├── tests/
│   ├── input_datas.py
│   ├── test_transform.py
│   └── test_validation.py
│
├── logs/
├── .env
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Olist dataset CSV files

### 1. Clone the repository

```bash
git clone https://github.com/ashwinam/brazzilian-ecomm-data-engineering.git
cd brazilian-ecomm-data-engineering
```

### 2. Create and activate a virtual environment and install dependencies

```bash
pip install uv
```

macOS/Linux:

```bash
uv sync
source .venv/bin/activate
```

### 3. Configure environment variables

Create a `.env` file in the project root:
>already provided an .env.example you can use that

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=olist_data_engineering
DB_USER=postgres
DB_PASSWORD=your_password
```

Do not commit your `.env` file or expose database credentials.

### 4. Prepare PostgreSQL

Create the database and configure the nine tables with the required columns, primary keys, and foreign key relationships.

### 5. Add the dataset

Place all nine Olist CSV files inside:

```text
datasets/brazilian-ecommerce/
```

### 6. Run the pipeline

From the project root:

```bash
python src/main.py
```

The pipeline extracts the CSV files, transforms the required datasets, and performs a full refresh of the PostgreSQL tables.

### 7. Run tests

```bash
pytest
```

## Future Improvements — Version 2

The next iteration will focus on orchestration and scalability:

- Integrate Apache Airflow 2 for workflow orchestration.
- Define task dependencies and scheduling through DAGs.
- Implement retries and failure monitoring.

## Learning Outcomes

This project helped me understand that data engineering is not just about moving data from one place to another.

It involves investigating source data, understanding relationships, making transformation decisions, maintaining data integrity, handling failures, and building repeatable pipelines.

**Version 1 completed. More improvements ahead.**