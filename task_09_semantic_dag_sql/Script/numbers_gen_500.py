import pandas as pd

OUTPUT_FILE = "numbers_500.csv"

df = pd.DataFrame({
    "number": range(1, 501)
})

df.to_csv(OUTPUT_FILE, index=False)

print(f"Generated {len(df)} rows → {OUTPUT_FILE}")