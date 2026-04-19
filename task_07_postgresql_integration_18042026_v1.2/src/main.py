
from db import load_traffic_state, load_policy
from policy import apply_policy


def main():
    df_state = load_traffic_state()
    policy_df = load_policy("v1.0")

    if policy_df.empty:
        raise RuntimeError("Policy v1.0 not found")

    policy = policy_df.iloc[0]

    df_result = apply_policy(df_state, policy)

    print(df_result.shape)
    print(df_result["traffic_state"].value_counts())


if __name__ == "__main__":
    main()
