CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    fund_house TEXT NOT NULL,
    category TEXT,
    plan TEXT,
    risk_grade TEXT
);


CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT NOT NULL,
    nav_date DATE NOT NULL,
    nav REAL NOT NULL,
    daily_return REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,

    amfi_code TEXT NOT NULL,

    investor_id TEXT,

    transaction_date DATE,

    transaction_type TEXT,

    amount REAL,

    units REAL,

    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code TEXT NOT NULL,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,

    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,

    aum_crore REAL,
    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_sip (
    sip_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code TEXT NOT NULL,

    sip_date DATE,

    sip_amount REAL,

    units_allocated REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

