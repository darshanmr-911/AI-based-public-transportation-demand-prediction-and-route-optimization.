import pandas as pd

df = pd.read_csv("Dataset/actual_route_passengers_HRH_RMN.csv")

print("\n===== DATASET SUMMARY =====")
print(df.info())

print("\n===== PASSENGERS BY DEPOT =====")
print(df.groupby("depot")["total_passengers"].agg(
    ["count", "sum", "mean", "min", "max"]
))

print("\n===== PASSENGERS BY SERVICE TYPE =====")
print(df.groupby("service_type")["total_passengers"].agg(
    ["count", "mean", "sum"]
).sort_values("mean", ascending=False))

print("\n===== TOP 10 ROUTES =====")
print(
    df.groupby(["depot", "from", "to"])["total_passengers"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())