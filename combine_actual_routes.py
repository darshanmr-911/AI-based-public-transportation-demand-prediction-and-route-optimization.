import pandas as pd

files = {
    "HRH": (
        "Dataset/Harohalli_Depot_12_Months.xlsx",
        "Depot Passenger Details",
        "2026-08-01"
    ),
    "RMN": (
        "Dataset/Ramanagara_Depot_12_Months.xlsx",
        "Oct-2026 Schedule-wise",
        "2026-10-01"
    )
}

all_data = []

for depot, (file, sheet, month) in files.items():
    df = pd.read_excel(file, sheet_name=sheet, header=2)

    # Find columns despite different header formatting
    def find_column(*words):
        for column in df.columns:
            name = str(column).lower().replace("\n", " ")
            if all(word.lower() in name for word in words):
                return column
        raise ValueError(f"Column not found: {words}")

    from_col = find_column("FROM")
    to_col = find_column("TO")
    service_col = find_column("SERVICE TYPE")
    interstate_col = find_column("INTERSTATE")
    shakthi_col = find_column("shakthi")
    total_col = find_column("total", "passenger")

    data = pd.DataFrame({
        "depot": depot,
        "source_month": month,
        "from": df[from_col],
        "to": df[to_col],
        "service_type": df[service_col],
        "interstate_type": df[interstate_col],
        "shakthi_passengers": pd.to_numeric(
            df[shakthi_col], errors="coerce"
        ),
        "total_passengers": pd.to_numeric(
            df[total_col], errors="coerce"
        )
    })

    data["non_shakthi_passengers"] = (
        data["total_passengers"] - data["shakthi_passengers"]
    )

    data = data.dropna(
        subset=["from", "to", "service_type", "total_passengers"]
    )

    data["data_type"] = "ACTUAL"
    all_data.append(data)

combined = pd.concat(all_data, ignore_index=True)

output = "Dataset/actual_route_passengers_HRH_RMN.csv"
combined.to_csv(output, index=False)

print("Combined dataset created!")
print("Total actual route records:", len(combined))
print("\nRecords by depot:")
print(combined["depot"].value_counts())
print("\nPassenger totals by depot:")
print(combined.groupby("depot")["total_passengers"].sum())
print("\nSaved to:", output)
