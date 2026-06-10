"""
Mutual Fund Analytics Capstone

Author: Ritik Kumar

Description:
Mutual fund performance and risk analytics.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

nav = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "02_nav_history.csv"
)

print(nav.shape)
print(nav.head())
print(nav.columns.tolist())

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

print(nav["date"].dtype)

nav = nav.sort_values(
    by=["amfi_code", "date"]
)
duplicates = nav.duplicated().sum()

print("Duplicates:", duplicates)

nav = nav.drop_duplicates()

#holidays
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)
output_path = (
    BASE_DIR /
    "Data" /
    "processed" /
    "nav_history_clean.csv"
)

nav.to_csv(
    output_path,
    index=False
)

print("Saved:", output_path)