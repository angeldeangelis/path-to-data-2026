
\# Task 08 — Imperative vs Declarative Classification (Semantic DAG)



This task explores the \*\*structural differences between imperative control flow and declarative, set‑based reasoning\*\* when solving classification problems with increasing semantic complexity.



The same problems are implemented twice:

\- using \*\*imperative Python\*\* (`for`, `if/elif`)

\- using \*\*declarative, vectorized pandas operations\*\*



The goal is \*\*not performance\*\*, but \*\*semantic clarity, correctness, and extensibility\*\*.





\---



\## Objective



To demonstrate how \*\*classification problems governed by dependencies and precedence rules\*\* naturally form a \*\*Directed Acyclic Graph (DAG)\*\*, and how:



\- imperative code tends to \*\*collapse the DAG into control flow\*\*

\- declarative code allows the DAG to remain \*\*explicit and inspectable\*\*



This task shows \*\*where and why the imperative approach starts to break down\*\* as complexity increases.





\---



\## Structure



Each `imperativeN.py` and `declarativeN.py` pair solves the \*\*same logical problem\*\*, with strictly increasing difficulty.





\---



\## Exercise Progression



\### Exercise 1

\- Single condition

\- No precedence

\- No dependencies



Both approaches are equally readable.



\---



\### Exercise 2

\- Multiple conditions

\- AND / OR combinations

\- First signs of semantic overlap



Declarative version begins to show clearer intent.



\---



\### Exercise 3

\- Overlapping categories

\- Explicit precedence rules

\- Mutual exclusion required



Imperative version becomes fragile:

\- order‑dependent

\- semantically implicit



Declarative version remains stable.



\---



\### Exercise 4

\- Multi‑level dependencies

\- Intermediate semantic categories

\- Explicit DAG of meaning



At this point:

\- imperative code collapses the DAG into `if/elif` order

\- declarative code expresses the DAG directly



This exercise represents the \*\*inflection point\*\*.





\---



\## Key Observation



> \*\*When a problem can be drawn as a DAG,  

> imperative code hides the structure,  

> while declarative code preserves it.\*\*



In the declarative implementations:

\- properties are defined once

\- intermediate concepts are named

\- final decisions are derived, not re‑computed

\- precedence is structural, not positional



In the imperative implementations:

\- logic is duplicated

\- meaning depends on execution order

\- semantic changes require global rewrites





\---



\## Design Principles Demonstrated



\- Separation of \*\*properties\*\*, \*\*intermediate meaning\*\*, and \*\*final decision\*\*

\- Use of \*\*set algebra\*\* instead of control flow

\- Explicit handling of \*\*precedence and exclusion\*\*

\- Avoidance of duplicated logic

\- Deterministic, order‑independent derivation





\---



\## Why This Matters



Most real‑world classification systems:

\- business rules

\- policies

\- eligibility logic

\- risk scoring

\- segmentation



are \*\*not sequential problems\*\* — they are \*\*relational problems\*\*.



This task demonstrates why \*\*declarative, set‑based approaches\*\* scale conceptually, while imperative approaches accumulate hidden complexity.





\---



\## Conclusion



Imperative code answers the question:

> \*“What should I do next?”\*



Declarative code answers the question:

> \*“What does this data mean?”\*



For problems governed by semantic relationships and dependencies, \*\*the second question is the correct one\*\*.





\---



\## Requirements



\- Python 3.x

\- pandas



