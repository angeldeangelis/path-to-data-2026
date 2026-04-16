import pandas as pd

BASE_FILE = "traffic_base.csv"
OUTPUT_FILE = "traffic_readings.csv"

df_base = pd.read_csv(BASE_FILE, parse_dates=["reading_time"])

dfs = []

for sensor_id in range(1, 11):
    df = df_base.copy()

    df["sensor_id"] = sensor_id
    df["vehicle_count"] += sensor_id * 3
    df["avg_speed_kmh"] -= sensor_id * 1
    df["occupancy_pct"] += sensor_id * 2

    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

df_final.to_csv(OUTPUT_FILE, index=False)

print(f"Generated {len(df_final)} rows → {OUTPUT_FILE}")