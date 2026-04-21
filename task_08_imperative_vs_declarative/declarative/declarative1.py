import pandas as pd

df = pd.DataFrame({"number": [1, 2, 3, 4, 5, 6]})

df["is_even"] = df["number"] % 2 == 0

print(df)