import pandas as pd

df = pd.DataFrame({"number": [3, 4, 7, 10, 12, 15]})

is_even = df["number"] % 2 == 0
is_small = df["number"] < 10

df["label"] = "ODD"
df.loc[is_even & is_small, "label"] = "SMALL_EVEN"
df.loc[is_even & ~is_small, "label"] = "LARGE_EVEN"

print(df)
