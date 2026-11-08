import pandas as pd

file_path = "Dataset/Ramanagara_Depot_Passengers.xlsx"

df = pd.read_excel(file_path, header=2)

print("Total rows:", len(df))

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())
