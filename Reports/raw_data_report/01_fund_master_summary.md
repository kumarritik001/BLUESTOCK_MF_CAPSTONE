--01_fund_master.csv

Shape: (40, 15)
Columns: ['amfi_code', 'fund_house', 'scheme_name', 'category', 'sub_category', 'plan', 'launch_date', 'benchmark',     'expense_ratio_pct', 'exit_load_pct', 'min_sip_amount', 'min_lumpsum_amount', 'fund_manager', 'risk_category', 'sebi_category_code']
Data Types:
    amfi_code               int64
    fund_house                str
    scheme_name               str
    category                  str
    sub_category              str
    plan                      str
    launch_date               str
    benchmark                 str
    expense_ratio_pct     float64
    exit_load_pct         float64
    min_sip_amount          int64
    min_lumpsum_amount      int64
    fund_manager              str
    risk_category             str
    sebi_category_code        str
    dtype: object

First 5 Rows:
   amfi_code       fund_house                                   scheme_name  ...   fund_manager risk_category sebi_category_code
0     119551  SBI Mutual Fund     SBI Bluechip Fund - Regular Plan - Growth  ...  Sohini Andani      Moderate               EC01
1     119552  SBI Mutual Fund      SBI Bluechip Fund - Direct Plan - Growth  ...  Sohini Andani      Moderate               EC01
2     119598  SBI Mutual Fund    SBI Small Cap Fund - Regular Plan - Growth  ...  R. Srinivasan     Very High               EC03
3     119599  SBI Mutual Fund     SBI Small Cap Fund - Direct Plan - Growth  ...  R. Srinivasan     Very High               EC03
4     119120  SBI Mutual Fund  SBI Magnum Gilt Fund - Regular Plan - Growth  ...   Dinesh Ahuja           Low               DC02

[5 rows x 15 columns]

Missing Values:
amfi_code             0
fund_house            0
scheme_name           0
category              0
sub_category          0
plan                  0
launch_date           0
benchmark             0
expense_ratio_pct     0
exit_load_pct         0
min_sip_amount        0
min_lumpsum_amount    0
fund_manager          0
risk_category         0
sebi_category_code    0
dtype: int64

Duplicate Rows: 0

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
['Equity', 'Debt']
Length: 2, dtype: str

Unique Sub Categories:
<StringArray>
[      'Large Cap',       'Small Cap',            'Gilt',         'Mid Cap',
  'Short Duration',           'Value',          'Liquid',       'Index/ETF',
       'Flexi Cap',           'Index', 'Large & Mid Cap',            'ELSS']
Length: 12, dtype: str

Unique Risk Grades:
<StringArray>
['Moderate', 'Very High', 'Low', 'High', 'Moderately High']
Length: 5, dtype: str
