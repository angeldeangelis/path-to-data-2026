import pandas as pd

numbers = [4, 6, 8, 9, 10, 12, 15, 16, 18, 21, 24]
df = pd.DataFrame({"number": numbers})

EVEN = df["number"] % 2 == 0
MULT_3 = df["number"] % 3 == 0
MULT_4 = df["number"] % 4 == 0

STRONG = EVEN & MULT_4
WEAK = MULT_3 & ~EVEN

CRITICAL = STRONG & MULT_3
IMPORTANT = WEAK
SECONDARY = EVEN & ~STRONG
NORMAL = ~(CRITICAL | IMPORTANT | SECONDARY)

df["label"] = "NORMAL"
df.loc[CRITICAL, "label"] = "CRITICAL"
df.loc[IMPORTANT, "label"] = "IMPORTANT"
df.loc[SECONDARY, "label"] = "SECONDARY"

print(df)
