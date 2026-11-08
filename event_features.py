import pandas as pd
import numpy as np

# Load event dataset
df = pd.read_csv("Dataset/event_data.csv")

# Convert date and time columns
df["event_date"] = pd.to_datetime(df["event_date"])

# Extract date features
df["event_day"] = df["event_date"].dt.day
df["event_month"] = df["event_date"].dt.month
df["event_weekday"] = df["event_date"].dt.dayofweek

# Weekend indicator
df["is_weekend"] = (
    df["event_weekday"] >= 5
).astype(int)

# Convert attendance into a numerical feature
df["attendance_log"] = np.log1p(
    df["expected_attendance"]
)

# Select useful features
features = [
    "depot",
    "event_type",
    "expected_attendance",
    "attendance_log",
    "distance_km",
    "event_day",
    "event_month",
    "event_weekday",
    "is_weekend"
]

event_features = df[features]

# Save processed data
event_features.to_csv(
    "Dataset/event_features.csv",
    index=False
)

print("Event feature engineering completed!")
print(event_features.to_string(index=False))