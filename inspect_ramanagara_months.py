import pandas as pd

file_path = "Dataset/Ramanagara_Depot_12_Months.xlsx"

# Display all sheet names
excel = pd.ExcelFile(file_path)

print("Available sheets:")
for sheet in excel.sheet_names:
    print("-", sheet)

# Preview first 8 rows of each sheet
for sheet in excel.sheet_names:
    print(f"\n===== {sheet} =====")

    df = pd.read_excel(
        file_path,
        sheet_name=sheet,
        header=None,
        nrows=8
    )

    print(df.to_string(index=False, header=False))