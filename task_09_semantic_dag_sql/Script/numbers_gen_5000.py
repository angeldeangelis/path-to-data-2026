import pandas as pd

OUTPUT_FILE = "numbers_5000.csv"

df = pd.DataFrame({
    "number": range(1, 5001)
})

df.to_csv(OUTPUT_FILE, index=False)

print(f"Generated {len(df)} rows → {OUTPUT_FILE}")