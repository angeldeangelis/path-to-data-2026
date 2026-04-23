

\# Task 09 — Semantic DAG Materialized in SQL



This task demonstrates how a semantic classification model expressed as a Directed Acyclic Graph (DAG) can be materialized and governed entirely in SQL, with Python used strictly as a validation and orchestration layer.



The focus of this task is semantic stability under state growth, not performance tuning or query optimization.



\---



\## Objective



The goal of this task is to demonstrate that:



\- classification logic governed by semantic dependencies can live entirely in SQL

\- the Directed Acyclic Graph (DAG) remains unchanged as the dataset grows

\- Python does not duplicate business logic

\- scaling affects state, not meaning



The system is validated against increasing data volumes:



\- 500 records

\- 5,000 records

\- 50,000 records



\---



\## Architectural Principle



SQL defines both state and meaning and acts as the source of truth.  

Python consumes and validates meaning but never defines it.



If Python needs to know the classification logic, the design is incorrect.



\---



\## Project Structure



task\_09\_semantic\_dag\_sql\_v1/

├── data/

│   └── numbers\_500.csv

│

├── sql/

│   ├── 01\_create\_state.sql

│   ├── 02\_load\_state.sql

│   ├── 03\_semantic\_dag.sql

│   └── 04\_views.sql

│

├── python/

│   └── validate\_counts.py

│

├── README.md

└── .gitignore



Each file has a single responsibility and operates at a clearly defined semantic level.



\---



\## SQL Layer Responsibilities



\### 01\_create\_state.sql



Defines the state container.



\- Creates the base table

\- Contains no data

\- Contains no logic

\- Contains no semantic meaning



\---



\### 02\_load\_state.sql



Defines how state is loaded.



\- Replaces the contents of the table

\- Used to scale from 500 to 5,000 and 50,000 records

\- This is the only file that changes when scaling data



\---



\### 03\_semantic\_dag.sql



Expresses the semantic DAG using Common Table Expressions (CTEs).



\- Defines base properties

\- Defines intermediate semantic nodes

\- Defines final classification

\- Used for reasoning and validation

\- Does not persist results



\---



\### 04\_views.sql



Persists semantic meaning as a database view.



\- Stores the DAG definition

\- Recomputes meaning from state

\- Avoids data duplication

\- Acts as the semantic source of truth



\---



\## Python Layer Responsibility



\### validate\_counts.py



Python is used exclusively to validate semantic invariants, not to compute classifications.



The script verifies that:



\- the semantic partition is total

\- no unexpected labels appear

\- the model remains consistent as data volume changes



Python never reimplements the DAG.



\---



\## Scaling Strategy



Scaling is performed by:



1\. Generating a larger CSV file

2\. Re-executing the state loading script

3\. Re-running semantic validation



No SQL logic is modified during scaling.



If the DAG needs to change to support more data, the model is incorrect.



\---



\## Key Observation



When a problem can be represented as a DAG, the DAG should live in structure, not in control flow.



SQL expresses the DAG directly.  

Imperative logic collapses it into execution order.



\---



\## Conclusion



This task demonstrates that:



\- semantic models can remain stable under state growth

\- SQL is an effective language for declarative meaning

\- Python’s role is validation and orchestration, not rule definition

\- separating state, meaning, and validation prevents hidden complexity



The system scales by changing data, not logic.



\---



\## Requirements



\- PostgreSQL

\- Python 3.x

\- pandas

\- psycopg2

