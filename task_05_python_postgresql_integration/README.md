\# task\_05\_python\_postgresql\_integration



Simple Python–PostgreSQL integration pipeline.



\## Description

This script reads data from a PostgreSQL database, applies classification rules

to infrastructure records (bridges), and prints the final result to the console.



\## Requirements

\- Python 3.14

\- Local PostgreSQL instance

\- Database: `infra\_db`

\- Table: `bridges`



\## Usage

```text

INSTALLATION

\------------

py -3.14 -m pip install -r requirements.txt



EXECUTION

\---------

$env:DB\_PASSWORD="your\_password"

py -3.14 read\_bridges.py



OUTPUT

\------

The script:

\- reads data from PostgreSQL

\- applies structural classification rules (OK, CRITICAL, OLD)

\- prints the resulting DataFrame to the console



NOTES

\-----

\- Database credentials are injected via environment variables

\- No secrets are stored in the source code

\- The project is designed to be reproducible and environment-agnostic

