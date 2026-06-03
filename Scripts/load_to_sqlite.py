from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

# Create SQLite database
engine = create_engine(
    f"sqlite:///{BASE_DIR}/Data/db/bluestock_mf.db"
)

fund_df = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "fund_master_clean.csv"
)

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

nav_df = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "nav_history_clean.csv"
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")

txn_df = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "investor_transactions_clean.csv"
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")

perf_df = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "scheme_performance_clean.csv"
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")




from sqlalchemy import text

with engine.connect() as conn:

    result = conn.execute(
        text(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
    )

    print("\nTables in Database:")

    for row in result:
        print(row[0])