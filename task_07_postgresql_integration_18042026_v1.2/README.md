
# task_07_python_postgresql_policy_driven_traffic


Policy‑driven Python–PostgreSQL pipeline for traffic data classification.


## Description

This task implements a **semantically clean, reproducible data pipeline** where:

- PostgreSQL stores:
  - **traffic state** (`traffic_reading`)
  - **classification policy** (`traffic_policy`)
- Python:
  - consumes state and policy
  - applies the policy **mechanically**
  - produces a derived classification without embedding business rules

This task explicitly separates:

- **State** (observed data)
- **Policy** (versioned decision criteria)
- **Derivation** (pure application of policy)

No classification logic is hard‑coded in Python.


## Architectural Principles

- PostgreSQL is the **source of truth** for both:
  - observed traffic data
  - decision criteria (policy)
- Python contains **no business rules**
- All thresholds, labels, and precedence live in SQL
- Policies are:
  - explicit
  - versioned
  - auditable
- The same state can be re‑interpreted by changing policy only


## Requirements

- Python 3.14
- Local PostgreSQL instance
- Database: `traffic_db`

Tables:
- `traffic_reading` (state)
- `traffic_policy` (policy)


## Database Schema

### traffic_reading (state)

Stores raw traffic observations coming from sensors.

This table is treated as **immutable state**.

---

### traffic_policy (policy)

Stores versioned classification criteria.

Example fields:

- `policy_version`
- congestion thresholds
- density thresholds
- rule precedence
- validity window

This table **declares meaning**, it does not execute logic.


## Usage

```text
INSTALLATION
------------

py -3.14 -m pip install -r requirements.txt


DATABASE SETUP
--------------

psql -U postgres -d traffic_db

-- state
SELECT COUNT(*) FROM traffic_reading;

-- policy
SELECT * FROM traffic_policy;


EXECUTION
---------

$env:DB_PASSWORD="your_password"
py -3.14 main.py


OUTPUT
------

The script:

- loads traffic state from PostgreSQL
- loads a specific policy version
- applies the policy using vectorized operations
- produces a derived traffic_state column
- reports:
  - total number of records processed
  - distribution of traffic states

No data is modified in the database.
