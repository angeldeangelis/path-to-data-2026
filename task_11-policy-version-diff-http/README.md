
# Task 11 — Policy Version Diff (HTTP Boundary)

This task demonstrates how **stateless comparison logic** can be safely exposed through an **HTTP boundary** without leaking state, duplicating logic, or coupling transport with meaning.

The system compares two versions of a policy stored in PostgreSQL and returns a classified result, while preserving strict separation between **state**, **logic**, and **transport**.

The focus of this task is **boundary design, stateless execution, and correct HTTP semantics**, not feature completeness or scalability.

---

## Objective

The goal of this task is to demonstrate that:

- state can be stored and versioned independently of logic
- comparison logic can remain pure and stateless
- HTTP can be used strictly as a boundary, not as a decision layer
- configuration belongs to the environment, not the code
- errors can be classified correctly using HTTP semantics

---

## Architectural Principle

State        → PostgreSQL  
Logic        → Pure Python functions  
Boundary     → HTTP (FastAPI)  

If business logic leaks into the HTTP layer, the design is incorrect.  
If state is cached or mutated in Python, the design is incorrect.

---

## Project Structure

``
task_11-policy-version-diff-http/
├── db.py
├── repository.py
├── diff_engine.py
├── main.py
├── README.md
└── .gitignore

Each module has a single responsibility and a clear boundary.

---

## State

State is stored exclusively in PostgreSQL.

A single table is used:


policies(name, version, content)

- The database is the single source of truth
- Policy versions are immutable
- No state is stored in application memory

---

## Logic

All comparison logic lives in a pure Python function.

### `diff_engine.py`

The comparison function:

- receives two policy versions as input
- produces a deterministic classification result
- has no side effects
- has no knowledge of HTTP or SQL

This function is complete and does not require modification when the transport layer changes.

---

## Repository Layer

The repository layer:

- translates SQL state into Python values
- contains no business logic
- contains no HTTP knowledge

It acts strictly as a **state access boundary**.

---

## HTTP Boundary

FastAPI is used to expose the comparison logic over HTTP.

The HTTP layer is responsible for:

- receiving input parameters
- validating state existence
- mapping outcomes to HTTP status codes
- returning structured responses

It does **not** define business rules.

---

## HTTP Semantics

The endpoint follows explicit HTTP semantics:

- `200 OK` → valid comparison executed
- `404 Not Found` → one or both policy versions do not exist
- `500 Internal Server Error` → infrastructure or unexpected failure

Errors are not hidden or reclassified.

---

## Configuration

All database configuration is provided via environment variables:

- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

No credentials or environment-specific values are hardcoded.

---

## Example Request

GET /diff?name=access_policy&v1=1&v2=2

Example response:

```json
{
  "policy": "access_policy",
  "from_version": 1,
  "to_version": 2,
  "result": {
    "status": "changed",
    "severity": "warning",
    "message": "Policy content has changed"
  }
}

Key Observation

HTTP is a transport boundary, not a logic layer.

By keeping the system stateless and explicit at the boundary, the same core logic can later be reused via CLI, batch jobs, or other services without modification.

Conclusion
This task demonstrates that:

stateless logic is easier to reason about and test
state and meaning should not be coupled to transport
HTTP can be introduced without restructuring the system
configuration belongs to the environment
small systems can still exhibit production-grade discipline

The result is a minimal but architecturally correct service that can evolve without refactoring its core.