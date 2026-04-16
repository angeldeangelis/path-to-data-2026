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

def load_traffic():
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
    
def classify_traffic(df):
    df["traffic_state"] = "FREE_FLOW"

    congested = (
        (df["avg_speed_kmh"] < 20)
        | (df["occupancy_pct"] > 80)
    )

    dense = (
        (df["avg_speed_kmh"] < 40)
        | (df["vehicle_count"] > 50)
    )

    df.loc[dense, "traffic_state"] = "DENSE"
    df.loc[congested, "traffic_state"] = "CONGESTED"

    return df

def main():
    df = load_traffic()
    df = classify_traffic(df)
    print(df)

def main():
    df = load_traffic()
    df = classify_traffic(df)

    print(
        df[
            [
                "sensor_id",
                "reading_time",
                "vehicle_count",
                "avg_speed_kmh",
                "occupancy_pct",
                "traffic_state",
            ]
        ]
        .sort_values(["sensor_id", "reading_time"])
    )

if __name__ == "__main__":
    main()