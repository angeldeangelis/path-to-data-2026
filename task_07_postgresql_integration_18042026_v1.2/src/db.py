import os
import psycopg2
import pandas as pd


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="traffic_db",
        user="postgres",
        password=os.environ["DB_PASSWORD"],
    )


def load_traffic_state():
    query = """
        SELECT
            sensor_id,
            reading_time,
            vehicle_count,
            avg_speed_kmh,
            occupancy_pct
        FROM traffic_reading;
    """
    with get_connection() as conn:
        return pd.read_sql(query, conn)


def load_policy(policy_version: str):
    query = """
        SELECT *
        FROM traffic_policy
        WHERE policy_version = %s;
    """
    with get_connection() as conn:
        return pd.read_sql(query, conn, params=(policy_version,))