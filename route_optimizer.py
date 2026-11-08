import pandas as pd
import math

# Load event impact estimates
df = pd.read_csv("Dataset/event_impact_estimates.csv")

# Assumed bus capacity
BUS_CAPACITY = 50

# Calculate buses required per route
df["buses_required"] = (
    df["estimated_event_passengers"] / BUS_CAPACITY
).apply(math.ceil)

# Prioritize routes with highest estimated demand
df = df.sort_values(
    ["depot", "estimated_event_passengers"],
    ascending=[True, False]
)

# Save optimization results
df.to_csv(
    "Dataset/route_optimization_results.csv",
    index=False
)

print("===== ROUTE OPTIMIZATION RESULTS =====")

for (depot, event), group in df.groupby(
    ["depot", "event_name"]
):
    print(f"\nDepot: {depot} | Event: {event}")

    print(
        group[
            ["from", "to", "estimated_event_passengers",
             "buses_required"]
        ].head(10).to_string(index=False)
    )

    print(
        "Total estimated buses:",
        group["buses_required"].sum()
    )

print("\nSaved: Dataset/route_optimization_results.csv")
