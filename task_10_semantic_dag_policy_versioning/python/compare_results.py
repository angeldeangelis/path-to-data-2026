import psycopg2
import pandas as pd
import os

# -------------------------
# Database connection
# -------------------------
conn = psycopg2.connect(
    dbname="task_10",
    user="postgres",
    password=os.environ["DB_PASSWORD"]
)

# -------------------------
# Load baseline vs adjusted results
# -------------------------
query = """
SELECT
    b.label AS baseline_label,
    a.label AS adjusted_label,
    COUNT(*) AS count
FROM classified_numbers_baseline b
JOIN classified_numbers_adjusted a USING (number)
GROUP BY b.label, a.label
ORDER BY b.label, a.label;
"""

df = pd.read_sql(query, conn)

# -------------------------
# Basic impact metrics
# -------------------------
total_records = pd.read_sql(
    "SELECT COUNT(*) AS total FROM numbers;", conn
)["total"][0]

changed_records = df[df["baseline_label"] != df["adjusted_label"]]["count"].sum()

# -------------------------
# Output
# -------------------------
print("Semantic policy comparison")
print("----------------------------")
print(df)
print()
print(f"Total records: {total_records}")
print(f"Records with changed classification: {changed_records}")
print(f"Change ratio: {changed_records / total_records:.4f}")
