"""
Mutual Fund Analytics Capstone

Author: Ritik Kumar

Description:
Mutual fund performance and risk analytics.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "scheme_performance_clean.csv"
)

rankings = pd.read_csv(
    BASE_DIR /
    "Data" /
    "processed" /
    "fund_rankings.csv"
)

df = performance.merge(
    rankings,
    on="amfi_code",
    how="left"
)

risk_profile = input(
    "Enter Risk Profile (Low/Moderate/High): "
).strip().lower()

if risk_profile == "low":

    recommendations = (
        df.sort_values(
            ["sharpe_ratio"],
            ascending=False
        )
        .head(3)
    )

elif risk_profile == "moderate":

    recommendations = (
        df.sort_values(
            ["fund_score"],
            ascending=False
        )
        .head(3)
    )

elif risk_profile == "high":

    recommendations = (
        df.sort_values(
            ["return_5yr_pct"],
            ascending=False
        )
        .head(3)
    )

else:

    print("Invalid Risk Profile")
    exit()

print("\nTop Recommended Funds\n")

cols = [
    "amfi_code",
    "fund_score",
    "sharpe_ratio"
]

available_cols = [
    c for c in cols
    if c in recommendations.columns
]

print(
    recommendations[
        available_cols
    ]
)