import numpy as np
import pandas as pd

df = pd.read_csv("Automobile_data.csv")

# 1
print("First 5 rows :\n", df.head(5))
print("\nLast 5 rows :\n", df.tail(5))

# 2
df.replace({'?': np.NaN, "n.a.": np.NaN}, inplace=True)
df.to_csv("Automated_data(cleaned).csv", index=False)
print("\nCleaned Automated Data Saved\n")

# 3
print("All BMW Cars details: \n")
print(df[df.company == "bmw"])

# 4
print("\nCount total cars per company: \n")
print(df.company.value_counts())

# 5
print("\nEach Company's Highest Price Car: \n")
print(df.groupby("company")[["company", "price"]].max())

# 6
print("\nAverage Mileage of each car making Company: \n")
print(df.groupby("company")[["company", "average-mileage"]].mean())

# 7

print("\nAfter Merging 2 Dataframes:\n")
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

df = pd.merge(carPriceDf, carsHorsepowerDf)
print(df)
