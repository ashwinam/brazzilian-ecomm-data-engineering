Let's step back and look at the complete setup from the beginning.

Our goal was to take your existing **Olist V1 ETL pipeline** and make it a runnable, orchestrated pipeline using **Apache Airflow 3.4.0**.

We didn't need to rewrite your ETL logic. We needed to prepare an environment where Airflow could access, execute, and monitor it.

# **1. High-level overview**

There are essentially five configuration stages:

1. **Prepare the Airflow environment**

   Install and run Airflow using Docker Compose.

   Why: Airflow needs its own runtime services to schedule and execute tasks.
2. **Configure the Python environment**

   Create a custom Airflow Docker image with the dependencies required by your project.

   Why: The Airflow containers need Pandas, Psycopg, SQLAlchemy and other project dependencies.
3. **Connect your project files**

   Mount your source code, datasets and shared storage into the Airflow containers. Configure Python's import path.

   Why: Airflow runs inside Docker, so it cannot automatically access files on your Mac.
4. **Configure external connections**

   Provide PostgreSQL connection details and environment variables.

   Why: Your pipeline needs to communicate with the PostgreSQL server running outside Docker.
5. **Create and register the DAG**

   Define the workflow, its tasks, dependencies and execution settings in the DAG directory.

   Why: Airflow needs a workflow definition before it can schedule or execute your pipeline.

# **2. What we configured at each stage**

Let's go through the actual work we completed.

## **Stage 1 — Prepare the Airflow environment**

We created an `airflow/` directory inside your existing project.

```
airflow/
├── dags/
├── logs/
├── plugins/
├── config/
└── docker-compose.yaml
```

**What we did:**

- Downloaded the official Airflow 3.4.0 Docker Compose configuration.
- Created the required directories.
- Configured `AIRFLOW_UID`.
- Initialized Airflow's metadata database.
- Started the Airflow services.
- Accessed the Airflow UI at `localhost:8080`.

**Why?**

Airflow is not just a Python library. It consists of multiple services that work together.

**Our Airflow environment**

**Scheduler**

Determines when tasks are ready to run.

**DAG Processor**

Processes DAG definitions.

**API Server**

Provides access to Airflow's API and UI.

**Worker**

Executes the tasks.

**PostgreSQL**

Stores Airflow metadata.

**Redis**

Supports Celery task distribution.

These are the main services in our Docker Compose setup. Airflow's metadata PostgreSQL is separate from your Olist application database.

## **Stage 2 — Configure the Python environment**

We created:

```
airflow/Dockerfile
```

We used the official Airflow image as our base and installed the additional dependencies needed by your pipeline.

**Why?**

Your local Python environment and Airflow's Docker environment are separate.

Even though Pandas works on your Mac, it won't automatically be available inside an Airflow worker.

We also aligned the image with Python 3.13, matching the existing Airflow container.

## **Stage 3 — Connect the project files**

This was one of the most important configurations.

Your original project files live on your Mac, but Airflow runs inside Docker containers.

We configured Docker volume mounts:

| Mac project directory | Airflow container directory     | Purpose                          |
| --------------------- | ------------------------------- | -------------------------------- |
| `src/`                | `/opt/airflow/project/src`      | Access existing Python modules   |
| `datasets/`           | `/opt/airflow/project/datasets` | Access source CSV files          |
| `airflow/data/`       | `/opt/airflow/shared`           | Store intermediate pipeline data |

We also configured:

```
PYTHONPATH=/opt/airflow/project
```

**Why?**

- Volume mounts make your project files accessible inside Docker.
- `PYTHONPATH` allows Python to find and import your existing `src` package.
- Shared storage allows different Airflow tasks to access the same intermediate files.

We verified this by importing your extraction module and successfully extracting all nine datasets from inside the Airflow worker.

## **Stage 4 — Configure PostgreSQL connectivity**

Your Olist database is running on your Mac, outside Docker.

From inside a Docker container, `localhost` refers to that container—not your Mac.

So we configured:

```
DB_HOST=host.docker.internal
```

We also provided:

- `DB_USER`
- `DB_PASSWORD`
- `DB_PORT`
- `DB_NAME`

These are supplied through environment variables rather than hardcoding credentials in the DAG.

**Why?**

The Airflow worker needs to connect to your existing PostgreSQL database to load the processed datasets.

## **Stage 5 — Create and register the DAG**

Finally, we created the DAG file inside:

```
airflow/dags/
```

We defined:

- DAG ID
- Start date
- Schedule
- Catchup behaviour
- Tasks
- Task dependencies

We also tested the initial DAG with dummy tasks before connecting your real extraction logic.

**Why?**

The DAG is the workflow definition that tells Airflow what needs to happen, in what order, and under what execution conditions.

# **3. How everything fits together**

This is the complete picture of our setup:

**Your Olist project on Mac**

Python modules · Datasets · PostgreSQL

Docker volume mounts and network connectivity

**Docker environment**

**Custom Airflow image**

Airflow 3.4.0 + Python dependencies

**Airflow services**

Scheduler · DAG Processor · API Server · Worker

**DAG definition**

Extract → Transform → Validate → Load

**Shared storage**

Intermediate CSV files

Database connection

**Olist PostgreSQL database**

Processed datasets

# **4. The configuration checklist**

Here's a reusable checklist for setting up Airflow for another Python project.

**Airflow setup progress**

8/8 complete

**Create Airflow directory structure**

dags, logs, plugins, config and Docker Compose

**Initialize and start Airflow services**

Docker Compose and metadata database

**Build custom Airflow image**

Install project runtime dependencies

**Configure volume mounts**

Source code, datasets and shared storage

**Configure Python import path**

Make project modules importable

**Configure external connections**

Database credentials and environment variables

**Create DAG definition**

DAG settings, tasks and dependencies

**Verify DAG registration and execution**

Test through the Airflow UI

One distinction worth remembering: **configuration makes the DAG runnable; the DAG's task implementation makes the pipeline do useful work.** We've worked on both, but this overview focused on the configuration.

Next, we can study the actual DAG execution lifecycle—from when Airflow discovers a DAG to when a worker executes each task.