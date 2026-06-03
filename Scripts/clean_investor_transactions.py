from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

transactions = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "08_investor_transactions.csv"
)

print(transactions.shape)
print(transactions.columns.tolist())

print(transactions["transaction_type"].value_counts(dropna=False))

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "LUMPSUM": "Lumpsum",
    "LUMP SUM": "Lumpsum",
    "PURCHASE": "Lumpsum",
    "REDEMPTION": "Redemption",
    "REDEEM": "Redemption"
}

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .replace(mapping)
)
print(transactions["transaction_type"].value_counts())

invalid_amounts = transactions[
    transactions["amount_inr"] <= 0
]

print("Invalid Amount Records:", len(invalid_amounts))

transactions["kyc_status"] = (
    transactions["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)


output_file = (
    BASE_DIR /
    "Data" /
    "processed" /
    "investor_transactions_clean.csv"
)

transactions.to_csv(
    output_file,
    index=False
)

print("Saved:", output_file)