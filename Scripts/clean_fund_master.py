"""
Mutual Fund Analytics Capstone

Author: Ritik Kumar

Description:
Mutual fund performance and risk analytics.
"""

from pathlib import Path
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load fund master
fund_master = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "01_fund_master.csv"
)

print("Shape:", fund_master.shape)

# Remove duplicate rows
duplicates = fund_master.duplicated().sum()
print("Duplicate rows:", duplicates)

fund_master = fund_master.drop_duplicates()

# Remove duplicate AMFI codes if any
duplicate_codes = fund_master["amfi_code"].duplicated().sum()
print("Duplicate AMFI codes:", duplicate_codes)

# Strip whitespace from text columns
text_cols = fund_master.select_dtypes(include="object").columns

for col in text_cols:
    fund_master[col] = fund_master[col].astype(str).str.strip()

# Missing values summary
print("\nMissing Values:")
print(fund_master.isnull().sum())

# Save cleaned file
output_path = (
    BASE_DIR /
    "Data" /
    "processed" /
    "fund_master_clean.csv"
)

fund_master.to_csv(
    output_path,
    index=False
)

print(f"\nSaved: {output_path}")