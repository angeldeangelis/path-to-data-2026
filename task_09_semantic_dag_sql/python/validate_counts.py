import psycopg2
import pandas as pd
import os
# -------------------------
# Database connection
# -------------------------
conn = psycopg2.connect(
    dbname="task_09",
    user="postgres",
    password=os.environ["DB_PASSWORD"]
)

# -------------------------
# Read semantic state
# -------------------------
query = """
SELECT label, COUNT(*) AS count
FROM classified_numbers
GROUP BY label
ORDER BY label;
"""

df = pd.read_sql(query, conn)

# -------------------------
# Invariants
# -------------------------
total_expected = pd.read_sql(
    "SELECT COUNT(*) AS total FROM numbers;", conn
)["total"][0]

total_observed = df["count"].sum()

expected_labels = {"CRITICAL", "IMPORTANT", "SECONDARY", "NORMAL"}
observed_labels = set(df["label"])

# -------------------------
# Assertions
# -------------------------
assert total_observed == total_expected, (
    f"Row count mismatch: expected {total_expected}, got {total_observed}"
)

assert observed_labels == expected_labels, (
    f"Unexpected labels found: {observed_labels}"
)

# -------------------------
# Output
# -------------------------
print("✅ Semantic validation passed")
print(df)
print(f"Total rows validated: {total_observed}")