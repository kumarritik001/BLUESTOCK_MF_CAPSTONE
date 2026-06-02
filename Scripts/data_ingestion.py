import pandas as pd

from pathlib import Path

"""BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "Data" / "raw" / "09_portfolio_holdings.csv"

df = pd.read_csv(file_path)
"""
""" print("\n" + "="*50)
print("01_fund_master.csv")
print("="*50)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum()) """


#print("\nColumns:")
#print(df.columns.tolist())

"""print("\nScheme_name:")
print(df['scheme_name'].unique())

print("\nUnique Fund Houses:")
print(df['fund_house'].unique())

 
print("\nUnique Categories:")
print(df['category'].unique())


print("\nUnique Risk Grades:")
print(df['risk_category'].unique())

print("\nUnique Risk Grades:")
print(df['risk_category'].unique())"""
"""
print("\nState:")
print(df['state'].unique())

print("\nCity:")
print(df['city'].unique())

print("\nCity tier:")
print(df['city_tier'].unique())

print("\nAge_group:")
print(df['age_group'].unique())

print("\nPayment_mode:")
print(df['payment_mode'].unique())

print("\nKYC_status:")
print(df['kyc_status'].unique())"""

#print(df['sector'].unique())
#print("\nSectors:")




#validating amfi codes that exists in fund master also exists in nav history

BASE_DIR = Path(__file__).resolve().parent.parent

fund_master = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "01_fund_master.csv"
)

nav_history = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "02_nav_history.csv"
)

master_codes = set(fund_master["amfi_code"].dropna().unique())
nav_codes = set(nav_history["amfi_code"].dropna().unique())

missing_in_nav = master_codes - nav_codes
missing_in_master = nav_codes - master_codes

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Codes in fund_master but missing in nav_history:", len(missing_in_nav))
print("Codes in nav_history but missing in fund_master:", len(missing_in_master))

if len(missing_in_nav) > 0:
    print("\nSample missing codes:")
    print(list(missing_in_nav)[:10])