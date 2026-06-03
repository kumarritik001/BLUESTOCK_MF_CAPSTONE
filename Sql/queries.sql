SELECT
    amfi_code,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
    strftime('%Y', month) AS year,
    SUM(inflow_amount) AS total_inflow
FROM fact_sip
GROUP BY year
ORDER BY year;

SELECT
    year,
    total_inflow,
    ROUND(
        (total_inflow -
         LAG(total_inflow) OVER (ORDER BY year))
         *100.0 /
         LAG(total_inflow) OVER (ORDER BY year),
         2
    ) AS yoy_growth_pct
FROM (
    SELECT
        strftime('%Y', month) AS year,
        SUM(inflow_amount) AS total_inflow
    FROM fact_sip
    GROUP BY year
);

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


SELECT
    d.category,
    ROUND(AVG(f.expense_ratio_pct), 2) AS avg_expense_ratio
FROM fact_performance f
JOIN dim_fund d
    ON f.amfi_code = d.amfi_code
GROUP BY d.category
ORDER BY avg_expense_ratio;


SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
WHERE sharpe_ratio < 0
ORDER BY sharpe_ratio;


SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC;


SELECT
    transaction_type,
    ROUND(SUM(amount), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;