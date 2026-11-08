import pandas as pd

files = {
    "Harohalli": (
        "Dataset/Harohalli_Depot_12_Months.xlsx",
        "Depot Passenger Details"
    ),
    "Ramanagara": (
        "Dataset/Ramanagara_Depot_12_Months.xlsx",
        "Oct-2026 Schedule-wise"
    )
}

for depot, (file, sheet) in files.items():
    print(f"\n===== {depot} ACTUAL DATA =====")

    df = pd.read_excel(
        file,
        sheet_name=sheet,
        header=2
    )

    print("Rows:", len(df))
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 3 records:")
    print(df.head(3).to_string(index=False))