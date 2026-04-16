# task_06_python_postgresql_integration_traffic



Python–PostgreSQL integration pipeline for traffic data classification.



## Description

This task implements a **reproducible Python–PostgreSQL pipeline** where:

- PostgreSQL acts as the **source of truth** for traffic sensor data
- Python loads the data into memory
- Traffic state is **classified in Python using vectorized logic**
- The final result is printed to the console

The objective of this task is to **design and validate set‑based classification logic**
in Python before moving it into SQL in a subsequent task.



## Requirements

- Python 3.14
- Local PostgreSQL instance
- Database: `traffic_db`
- Table: `traffic_reading`



## Usage

```text
INSTALLATION
------------

py -3.14 -m pip install -r requirements.txt


DATA GENERATION
---------------

py generate_traffic_csv.py

This script:
- reads a deterministic base dataset (traffic_base.csv)
- generates multiple traffic sensors using vectorized transformations
- produces traffic_readings.csv (200 rows total)


DATABASE LOAD
-------------

psql -U postgres -d traffic_db

TRUNCATE TABLE traffic_reading;

\copy traffic_reading FROM 'traffic_reading.csv' CSV HEADER;


EXECUTION
---------

$env:DB_PASSWORD="your_password"
py -3.14 read_traffic.py


OUTPUT
------

The script:

- reads traffic data from PostgreSQL
- applies vectorized classification rules in Python
- assigns a traffic_state to each record:
  - FREE_FLOW
  - DENSE
  - CONGESTED
- sorts the results by sensor and timestamp
- prints the resulting DataFrame to the console



NOTES
-----

- Traffic classification is intentionally performed in Python in this task
- The classification logic is fully set‑based and O(n)
- SQL is used only for data storage and retrieval
- Database credentials are injected via environment variables
- No secrets are stored in the source code
- This task serves as a **preparatory step** for moving classification logic
  into SQL in the next task
``