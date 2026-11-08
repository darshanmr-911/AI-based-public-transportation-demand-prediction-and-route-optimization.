import pandas as pd
import numpy as np

routes = pd.read_csv(
    "Dataset/actual_route_passengers_HRH_RMN.csv"
)

events = pd.read_csv(
    "Dataset/event_data.csv"
)

# Assumed percentage of event attendees using public transport
# These are scenario assumptions, not measured values.
EVENT_USAGE_RATE = 0.30

# Assumed share of public transport attendees using buses
BUS_USAGE_RATE = 0.70

# Estimate event-related bus passengers
events["estimated_bus_passengers"] = (
    events["expected_attendance"]
    * EVENT_USAGE_RATE
    * BUS_USAGE_RATE
).round().astype(int)

# Allocate event passengers across routes in the same depot.
# Allocation is proportional to each route's baseline passengers.
results = []

for _, event in events.iterrows():

    depot_routes = routes[
        routes["depot"] == event["depot"]
    ].copy()

    total_baseline = depot_routes["total_passengers"].sum()

    depot_routes["event_name"] = event["event_name"]
    depot_routes["event_date"] = event["event_date"]

    depot_routes["estimated_event_passengers"] = (
        event["estimated_bus_passengers"]
        * depot_routes["total_passengers"]
        / total_baseline
    ).round().astype(int)

    depot_routes["data_type"] = "SIMULATED_ESTIMATE"

    results.append(depot_routes)

output = pd.concat(results, ignore_index=True)

output.to_csv(
    "Dataset/event_impact_estimates.csv",
    index=False
)

print("===== EVENT IMPACT ESTIMATION =====")
print(
    events[
        ["depot", "event_name", "expected_attendance",
         "estimated_bus_passengers"]
    ].to_string(index=False)
)

print("\n===== ESTIMATED PASSENGERS BY EVENT =====")
print(
    output.groupby(
        ["depot", "event_name"]
    )["estimated_event_passengers"].sum()
)

print("\nSaved: Dataset/event_impact_estimates.csv")
