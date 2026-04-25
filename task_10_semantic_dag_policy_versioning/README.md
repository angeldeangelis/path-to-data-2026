\# Task 10 — Semantic DAG Policy Versioning



This task demonstrates how \*\*semantic policies can evolve over time\*\* without changing state, breaking consumers, or duplicating logic.



Using the same underlying dataset, two different semantic policies are defined, materialized, and compared to measure the \*\*impact of a controlled change in meaning\*\*.



The focus of this task is \*\*policy versioning, auditability, and impact analysis\*\*, not performance or data volume.



\---



\## Objective



The goal of this task is to demonstrate that:



\- semantic meaning can be versioned independently of data

\- multiple policies can coexist over the same state

\- policy changes can be audited and quantified

\- SQL can act as the single source of truth for semantic rules

\- Python is used only to measure consequences, not define logic



\---



\## Architectural Principle



State      → SQL tables

Meaning    → SQL views (one per policy)

Impact     → SQL + Python comparison



If policy logic leaks into Python, the design is incorrect.



\---



\## Project Structure





task\_10\_semantic\_dag\_policy\_versioning/

├── data/

│   └── numbers.csv

│

├── sql/

│   ├── 01\_create\_state.sql

│   ├── 02\_load\_state.sql

│

│   ├── policy\_baseline.sql

│   ├── policy\_adjusted.sql

│

│   ├── view\_baseline.sql

│   ├── view\_adjusted.sql

│

│   └── compare\_policies.sql

│

├── python/

│   └── compare\_results.py

│

├── README.md

└── .gitignore



Each layer has a single responsibility and a clear semantic boundary.



\---



\## State



The state is represented by a single table:





numbers(number)



The state does not change between policies.



\---



\## Policies



Two semantic policies are defined over the same state:



\### Baseline Policy



The baseline policy represents the original classification logic.  

It defines a conservative interpretation of the `CRITICAL` category.



\### Adjusted Policy



The adjusted policy expands the definition of `CRITICAL` by introducing an additional semantic condition.



No state is modified.  

Only meaning changes.



\---



\## Views



Each policy is materialized as its own SQL view:



\- `classified\_numbers\_baseline`

\- `classified\_numbers\_adjusted`



These views:



\- expose semantic meaning as stable system contracts

\- can be queried independently

\- can coexist safely

\- allow direct comparison



\---



\## Policy Comparison



Policy impact is evaluated in two ways:



\### Row-level comparison (SQL)



Records whose classification changed are identified directly in SQL using joins between policy views.



\### Aggregate impact analysis (Python)



Python reads both views and produces:



\- transition counts (from → to)

\- total affected records

\- impact ratio



Python never reimplements classification logic.



\---



\## Results Summary



With a dataset of 50,000 records:



\- Total records: 50,000

\- Records with changed classification: 4,167

\- Change ratio: \~8.33%



The change affected a specific subset of the domain, without introducing regressions or unintended side effects.



\---



\## Key Observation



> Semantic policies should evolve without rewriting systems.



By separating state, meaning, and impact analysis, policy changes become:



\- explicit

\- auditable

\- reversible

\- safe



\---



\## Conclusion



This task demonstrates that:



\- semantic rules can be versioned independently of data

\- SQL is an effective language for declarative meaning

\- multiple interpretations can coexist over the same state

\- policy changes can be measured precisely

\- Python’s role is analysis, not decision-making



This pattern is directly applicable to real-world systems involving business rules, regulatory changes, or evolving classification logic.



\---



\## Requirements



\- PostgreSQL

\- Python 3.x

\- pandas

\- psycopg2

