import numpy as np
import pandas as pd

df = pd.read_csv("Automobile_data.csv")

# 1
print("First 5 rows :\n", df.head())
print("Last 5 rows :\n", df.tail())

# 2
df.replace({'?': np.NaN, "n.a.": np.NaN}, inplace=True)
df.to_csv("Automated_data(cleaned).csv", index=False)

# 3

