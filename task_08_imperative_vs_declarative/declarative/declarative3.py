import pandas as pd 
df = pd.DataFrame({"number": [3, 4, 7, 10, 12, 15]})
is_even = df["number"] % 2 == 0
mult_3 = df["number"] % 3 == 0
is_large = df["number"] >= 10 
df["label"] = "NORMAL"
df.loc[mult_3 & is_even, "label"] = "CRITICAL"
df.loc[mult_3 & ~is_even, "label"] = "IMPORTANT"
df.loc[is_even & is_large, "label"] = "SECONDARY"
print(df)