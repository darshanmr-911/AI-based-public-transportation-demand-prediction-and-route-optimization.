import pandas as pd

# Load passenger dataset
passengers = pd.read_excel(
    "Dataset/Harohalli_Passenger_Details.xlsx",
    header=2
)

# Load event dataset
events = pd.read_csv("Dataset/event_data.csv")

print("\n===== PASSENGER DATA =====")
print("Rows:", len(passengers))
print("Columns:", passengers.columns.tolist())
print("\nMissing values:")
print(passengers.isnull().sum())

print("\n===== EVENT DATA =====")
print("Rows:", len(events))
print("Columns:", events.columns.tolist())
print("\nEvent records:")
print(events.to_string(index=False))

print("\n===== DEPOT INFORMATION =====")
print("Passenger depots:")
print(passengers["DEPOT"].dropna().unique())

print("\nEvent depots:")
print(events["depot"].unique())