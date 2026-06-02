Shape: (322, 8)

Columns: ['amfi_code', 'stock_symbol', 'stock_name', 'sector', 'weight_pct', 'market_value_cr', 'current_price_inr', 'portfolio_date']

Data Types:
amfi_code              int64
stock_symbol             str
stock_name               str
sector                   str
weight_pct           float64
market_value_cr      float64
current_price_inr    float64
portfolio_date           str
dtype: object

First 5 Rows:
   amfi_code stock_symbol                stock_name       sector  weight_pct  market_value_cr  current_price_inr portfolio_date
0     119551    POWERGRID    Power Grid Corporation    Utilities       13.85           737.09            6011.08     2025-12-31
1     119551     HDFCBANK             HDFC Bank Ltd      Banking       11.19            88.97            1074.65     2025-12-31
2     119551       GRASIM     Grasim Industries Ltd  Diversified        9.90           208.45            5964.59     2025-12-31
3     119551      DRREDDY  Dr. Reddy's Laboratories       Pharma        4.76           161.32            3748.82     2025-12-31
4     119551   ASIANPAINT          Asian Paints Ltd       Paints       10.25           725.90            1321.45     2025-12-31

Missing Values:
amfi_code            0
stock_symbol         0
stock_name           0
sector               0
weight_pct           0
market_value_cr      0
current_price_inr    0
portfolio_date       0
dtype: int64

Duplicate Rows: 0

Sectors:
<StringArray>
[     'Utilities',        'Banking',    'Diversified',         'Pharma',
         'Paints',        'Telecom',             'IT',     'Automobile',
           'NBFC',         'Cement',         'Energy', 'Consumer Goods',
           'FMCG', 'Infrastructure']
Length: 14, dtype: str