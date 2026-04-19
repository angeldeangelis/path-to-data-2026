import pandas as pd


def apply_policy(df: pd.DataFrame, policy: pd.Series) -> pd.DataFrame:
    df = df.copy()


    df["traffic_state"] = "FREE_FLOW"

    congested = (
        (df["avg_speed_kmh"] < policy["min_speed_congested"])
        | (df["occupancy_pct"] > policy["max_occupancy_congested"])
    )

    dense = (
        (df["avg_speed_kmh"] < policy["min_speed_dense"])
        | (df["vehicle_count"] > policy["max_vehicle_dense"])
    )

    for state in policy["priority_order"]:
        if state == "CONGESTED":
            df.loc[congested, "traffic_state"] = "CONGESTED"
        elif state == "DENSE":
            df.loc[dense & ~congested, "traffic_state"] = "DENSE"

    df["policy_version"] = policy["policy_version"]

    return df