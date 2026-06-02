Shape: (40, 19)

Columns: ['amfi_code', 'scheme_name', 'fund_house', 'category', 'plan', 'return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct', 'benchmark_3yr_pct', 'alpha', 'beta', 'sharpe_ratio', 'sortino_ratio', 'std_dev_ann_pct', 'max_drawdown_pct', 'aum_crore', 'expense_ratio_pct', 'morningstar_rating', 'risk_grade']

Data Types:
amfi_code               int64
scheme_name               str
fund_house                str
category                  str
plan                      str
return_1yr_pct        float64
return_3yr_pct        float64
return_5yr_pct        float64
benchmark_3yr_pct     float64
alpha                 float64
beta                  float64
sharpe_ratio          float64
sortino_ratio         float64
std_dev_ann_pct       float64
max_drawdown_pct      float64
aum_crore               int64
expense_ratio_pct     float64
morningstar_rating      int64
risk_grade                str
dtype: object

First 5 Rows:
   amfi_code                                   scheme_name       fund_house  ... expense_ratio_pct morningstar_rating  risk_grade
0     119551     SBI Bluechip Fund - Regular Plan - Growth  SBI Mutual Fund  ...              1.54                  4    Moderate
1     119552      SBI Bluechip Fund - Direct Plan - Growth  SBI Mutual Fund  ...              0.66                  3    Moderate
2     119598    SBI Small Cap Fund - Regular Plan - Growth  SBI Mutual Fund  ...              1.43                  5   Very High
3     119599     SBI Small Cap Fund - Direct Plan - Growth  SBI Mutual Fund  ...              0.72                  4   Very High
4     119120  SBI Magnum Gilt Fund - Regular Plan - Growth  SBI Mutual Fund  ...              0.77                  5         Low

[5 rows x 19 columns]

Missing Values:
amfi_code             0
scheme_name           0
fund_house            0
category              0
plan                  0
return_1yr_pct        0
return_3yr_pct        0
return_5yr_pct        0
benchmark_3yr_pct     0
alpha                 0
beta                  0
sharpe_ratio          0
sortino_ratio         0
std_dev_ann_pct       0
max_drawdown_pct      0
aum_crore             0
expense_ratio_pct     0
morningstar_rating    0
risk_grade            0
dtype: int64

Duplicate Rows: 0

Scheme_name:
<StringArray>
[            'SBI Bluechip Fund - Regular Plan - Growth',
              'SBI Bluechip Fund - Direct Plan - Growth',
            'SBI Small Cap Fund - Regular Plan - Growth',
             'SBI Small Cap Fund - Direct Plan - Growth',
          'SBI Magnum Gilt Fund - Regular Plan - Growth',
             'HDFC Top 100 Fund - Regular Plan - Growth',
              'HDFC Top 100 Fund - Direct Plan - Growth',
    'HDFC Mid-Cap Opportunities Fund - Regular - Growth',
     'HDFC Mid-Cap Opportunities Fund - Direct - Growth',
          'HDFC Short Term Debt Fund - Regular - Growth',
            'ICICI Pru Bluechip Fund - Regular - Growth',
             'ICICI Pru Bluechip Fund - Direct - Growth',
              'ICICI Pru Midcap Fund - Regular - Growth',
     'ICICI Pru Value Discovery Fund - Regular - Growth',
              'ICICI Pru Liquid Fund - Regular - Growth',
        'Nippon India Large Cap Fund - Regular - Growth',
         'Nippon India Large Cap Fund - Direct - Growth',
        'Nippon India Small Cap Fund - Regular - Growth',
                        'Nippon India ETF Nifty 50 BeES',
  'Nippon India Gilt Securities Fund - Regular - Growth',
                'Kotak Bluechip Fund - Regular - Growth',
         'Kotak Emerging Equity Fund - Regular - Growth',
                'Kotak Flexicap Fund - Regular - Growth',
                  'Kotak Liquid Fund - Regular - Growth',
                 'Axis Bluechip Fund - Regular - Growth',
                  'Axis Bluechip Fund - Direct - Growth',
                   'Axis Midcap Fund - Regular - Growth',
                'Axis Small Cap Fund - Regular - Growth',
         'ABSL Frontline Equity Fund - Regular - Growth',
                'ABSL Small Cap Fund - Regular - Growth',
                   'ABSL Liquid Fund - Regular - Growth',
            'UTI Nifty 50 Index Fund - Regular - Growth',
                   'UTI Mid Cap Fund - Regular - Growth',
                 'UTI Flexi Cap Fund - Regular - Growth',
         'Mirae Asset Large Cap Fund - Regular - Growth',
 'Mirae Asset Emerging Bluechip Fund - Regular - Growth',
         'Mirae Asset Tax Saver Fund - Regular - Growth',
            'DSP Top 100 Equity Fund - Regular - Growth',
                    'DSP Midcap Fund - Regular - Growth',
                 'DSP Small Cap Fund - Regular - Growth']
Length: 40, dtype: str

Unique Fund Houses:
<StringArray>
[         'SBI Mutual Fund',         'HDFC Mutual Fund',
      'ICICI Prudential MF',          'Nippon India MF',
        'Kotak Mahindra MF',         'Axis Mutual Fund',
 'Aditya Birla Sun Life MF',          'UTI Mutual Fund',
           'Mirae Asset MF',          'DSP Mutual Fund']
Length: 10, dtype: str

Unique Categories:
<StringArray>
[      'Large Cap',       'Small Cap',            'Gilt',         'Mid Cap',
  'Short Duration',           'Value',          'Liquid',       'Index/ETF',
       'Flexi Cap',           'Index', 'Large & Mid Cap',            'ELSS']
Length: 12, dtype: str