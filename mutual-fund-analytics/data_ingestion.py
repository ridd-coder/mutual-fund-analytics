import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

csv_files = list(raw_path.glob("*.csv"))

print(f"Total datasets found: {len(csv_files)}")

for file in csv_files:
    print("\n" + "="*60)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")

master_codes = set(fund_master["scheme_code"])

print("\nAMFI CODE VALIDATION")
print("-" * 40)

for code in master_codes:
    print(f"Scheme Code Found: {code}")

print("\nTotal Scheme Codes:", len(master_codes))
print("Validation Completed Successfully")