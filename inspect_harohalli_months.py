import pandas as pd

file_path = "Dataset/Harohalli_Depot_12_Months.xlsx"

# Read workbook sheets
excel = pd.ExcelFile(file_path)

print("Available sheets:")
for sheet in excel.sheet_names:
    print("-", sheet)

# Inspect first 8 rows of every sheet
for sheet in excel.sheet_names:
    print(f"\n===== {sheet} =====")

    df = pd.read_excel(
        file_path,
        sheet_name=sheet,
        header=None,
        nrows=8
    )

    print(df.to_string(index=False, header=False))
    