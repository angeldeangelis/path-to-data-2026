import os
import psycopg2
import pandas as pd


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="infra_db",
        user="postgres",
        password=os.environ["DB_PASSWORD"],
    )


def load_bridges():
    query = "SELECT * FROM bridges;"
    with get_connection() as conn:
        return pd.read_sql(query, conn)


def classify_bridge(row):
    if row["max_load"] < 80:
        return "CRITICAL"
    if row["year_built"] < 1990:
        return "OLD"
    return "OK"


def main():
    df = load_bridges()
    df["status"] = df.apply(classify_bridge, axis=1)
    print(df)


if __name__ == "__main__":
    main()
