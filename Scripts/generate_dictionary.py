from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

files = [
    "fund_master_clean.csv",
    "nav_history_clean.csv",
    "investor_transactions_clean.csv",
    "scheme_performance_clean.csv"
]

for file in files:

    df = pd.read_csv(BASE_DIR / "Data" / "processed" / file)

    print(f"\n{'='*50}")
    print(file)
    print('='*50)

    for col, dtype in zip(df.columns, df.dtypes):
        print(f"{col} | {dtype}")