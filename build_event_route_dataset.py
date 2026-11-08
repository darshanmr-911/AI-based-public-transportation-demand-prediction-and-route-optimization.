import pandas as pd

routes = pd.read_csv(
    "Dataset/actual_route_passengers_HRH_RMN.csv"
)

events = pd.read_csv(
    "Dataset/event_data.csv"
)

# Connect each event with routes from its depot
df = routes.merge(
    events,
    on="depot",
    how="inner",
    validate="many_to_many"
)

# Add useful event features
df["event_date"] = pd.to_datetime(df["event_date"])
df["event_weekday"] = df["event_date"].dt.day_of_week
df["is_weekend"] = (
    df["event_weekday"] >= 5
).astype(int)

df["event_duration_hours"] = (
    pd.to_timedelta(df["end_time"] + ":00")
    - pd.to_timedelta(df["start_time"] + ":00")
).dt.total_seconds() / 3600

# Keep actual baseline and simulated event information separate
df = df.rename(columns={
    "total_passengers": "baseline_monthly_passengers"
})

df["baseline_data_type"] = "ACTUAL"
df["event_data_type"] = "SIMULATED"

output = "Dataset/event_route_scenarios.csv"

df.to_csv(output, index=False)

print("Event-route dataset created!")
print("Total scenario rows:", len(df))

print("\nScenarios by depot:")
print(df.groupby("depot").size())

print("\nScenarios by event:")
print(df.groupby(["depot", "event_name"]).size())

print("\nSaved to:", output)