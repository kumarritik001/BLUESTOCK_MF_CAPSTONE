# Advanced Analytics Summary

## Project Overview

This report summarizes the advanced analytics performed on mutual fund datasets using NAV history, benchmark indices, and scheme performance data.

## Metrics Computed

### 1. Daily Returns

Formula:

daily_return = (NAV_t / NAV_t-1) - 1

Used as the base metric for all risk and performance calculations.

### 2. Annualized Returns

Formula:

Annualized Return = (1 + daily_return).prod()^(252/n) - 1

Used to compare funds on a yearly basis.

### 3. CAGR (Compound Annual Growth Rate)

Computed for:

* 1 Year
* 3 Years
* 5 Years

Formula:

CAGR = (Ending NAV / Starting NAV)^(1/Years) - 1

### 4. Sharpe Ratio

Risk-adjusted performance metric.

Formula:

Sharpe = (Rp - Rf) / σ

Where:

* Rp = Portfolio Return
* Rf = Risk-Free Rate (6.5%)
* σ = Standard Deviation of Returns

### 5. Sortino Ratio

Measures return relative to downside risk.

Formula:

Sortino = (Rp - Rf) / Downside Deviation

### 6. Alpha

Measures excess return over benchmark.

Positive Alpha indicates benchmark outperformance.

### 7. Beta

Measures fund sensitivity to benchmark movements.

Interpretation:

* Beta > 1 : More volatile than benchmark
* Beta < 1 : Less volatile than benchmark
* Beta = 1 : Moves with benchmark

### 8. Maximum Drawdown

Measures the maximum decline from a previous peak.

Formula:

Drawdown = NAV / Running Peak - 1

Max Drawdown = Minimum Drawdown

## Fund Ranking Methodology

Composite Fund Score:

* 40% CAGR
* 30% Sharpe Ratio
* 20% Sortino Ratio
* 10% Alpha

Funds were ranked based on the weighted score.

## Deliverables Generated

* annualized_returns.csv
* cagr_report.csv
* sharpe_values.csv
* sortino_values.csv
* alpha_beta.csv
* max_drawdown.csv
* fund_rankings.csv

## Key Findings

* Risk-adjusted metrics provide better insights than absolute returns alone.
* CAGR helps identify long-term wealth creators.
* Sharpe and Sortino highlight consistency of returns.
* Alpha identifies benchmark-beating schemes.
* Maximum Drawdown quantifies downside risk.
* Composite ranking helps compare funds across multiple dimensions.

## Conclusion

Advanced analytics were successfully performed on the mutual fund dataset. Performance, risk, benchmark comparison, and ranking metrics were generated and stored for further dashboarding and reporting.
