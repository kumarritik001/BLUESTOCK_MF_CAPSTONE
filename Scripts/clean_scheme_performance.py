from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

scheme = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "07_scheme_performance.csv"
)

print(scheme.shape)


return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in return_cols:
    scheme[col] = pd.to_numeric(
        scheme[col],
        errors="coerce"
    )



print("\nInvalid Numeric Values:")

for col in return_cols:
    print(
        col,
        ":",
        scheme[col].isna().sum()
    )

negative_sharpe = scheme[
    scheme["sharpe_ratio"] < 0
]

print(
    "Negative Sharpe Ratio Schemes:",
    len(negative_sharpe)
)


print(
    negative_sharpe[
        ["amfi_code",
         "scheme_name",
         "sharpe_ratio"]
    ].head()
)

scheme = scheme.sort_values(
    by=["amfi_code"]
)


invalid_expense = scheme[
    (scheme["expense_ratio_pct"] < 0.1) |
    (scheme["expense_ratio_pct"] > 2.5)
]

print(
    "Expense Ratio Outliers:",
    len(invalid_expense)
)



print("\nMissing Values")

print(
    scheme.isnull().sum()
)

duplicate_codes = (
    scheme["amfi_code"]
    .duplicated()
    .sum()
)

print(
    "Duplicate AMFI Codes:",
    duplicate_codes
)

output_file = (
    BASE_DIR /
    "Data" /
    "processed" /
    "scheme_performance_clean.csv"
)

scheme.to_csv(
    output_file,
    index=False
)

print(
    "Saved:",
    output_file
)