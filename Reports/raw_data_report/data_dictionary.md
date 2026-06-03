fund_master_clean.csv
==================================================
amfi_code | int64
fund_house | str
scheme_name | str
category | str
sub_category | str
plan | str
launch_date | str
benchmark | str
expense_ratio_pct | float64
exit_load_pct | float64
min_sip_amount | int64
min_lumpsum_amount | int64
fund_manager | str
risk_category | str
sebi_category_code | str

==================================================
nav_history_clean.csv
==================================================
amfi_code | int64
date | str
nav | float64

==================================================
investor_transactions_clean.csv
==================================================
investor_id | str
transaction_date | str
amfi_code | int64
transaction_type | str
amount_inr | int64
state | str
city | str
city_tier | str
age_group | str
gender | str
annual_income_lakh | float64
payment_mode | str
kyc_status | str

==================================================
scheme_performance_clean.csv
==================================================
amfi_code | int64
scheme_name | str
fund_house | str
category | str
plan | str
return_1yr_pct | float64
return_3yr_pct | float64
return_5yr_pct | float64
benchmark_3yr_pct | float64
alpha | float64
beta | float64
sharpe_ratio | float64
sortino_ratio | float64
std_dev_ann_pct | float64
max_drawdown_pct | float64
aum_crore | int64
expense_ratio_pct | float64
morningstar_rating | int64
risk_grade | str