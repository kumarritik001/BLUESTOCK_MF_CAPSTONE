Shape: (32778, 13)

Columns: ['investor_id', 'transaction_date', 'amfi_code', 'transaction_type', 'amount_inr', 'state', 'city', 'city_tier', 'age_group', 'gender', 'annual_income_lakh', 'payment_mode', 'kyc_status']

Data Types:
investor_id               str
transaction_date          str
amfi_code               int64
transaction_type          str
amount_inr              int64
state                     str
city                      str
city_tier                 str
age_group                 str
gender                    str
annual_income_lakh    float64
payment_mode              str
kyc_status                str
dtype: object

First 5 Rows:
  investor_id transaction_date  amfi_code transaction_type  amount_inr  ... age_group  gender annual_income_lakh payment_mode kyc_status
0   INV003054       2024-01-01     119092              SIP        1834  ...       56+  Female               77.1          UPI   Verified
1   INV002952       2024-01-01     148567       Redemption      392882  ...     18-25    Male                7.1       Cheque   Verified
2   INV003420       2024-01-01     118636              SIP         912  ...     36-45    Male               47.2      Mandate   Verified
3   INV003436       2024-01-01     118634              SIP        1102  ...     36-45  Female               54.4       Cheque    Pending
4   INV004691       2024-01-01     119094          Lumpsum        8682  ...     26-35    Male               14.5  Net Banking    Pending

[5 rows x 13 columns]

Missing Values:
investor_id           0
transaction_date      0
amfi_code             0
transaction_type      0
amount_inr            0
state                 0
city                  0
city_tier             0
age_group             0
gender                0
annual_income_lakh    0
payment_mode          0
kyc_status            0
dtype: int64

Duplicate Rows: 0


State:
<StringArray>
[     'Telangana',         'Punjab',        'Haryana',    'Maharashtra',
          'Delhi', 'Madhya Pradesh',        'Gujarat',      'Rajasthan',
  'Uttar Pradesh',      'Karnataka',    'West Bengal',     'Tamil Nadu']
Length: 12, dtype: str

City:
<StringArray>
[ 'Hyderabad',   'Amritsar',  'Faridabad',     'Mumbai',      'Noida',
     'Bhopal',     'Nashik', 'Chandigarh',  'Ahmedabad',     'Jaipur',
       'Agra',     'Mysore',    'Kolkata', 'Coimbatore',   'Gurugram',
     'Indore',    'Chennai',    'Udaipur',      'Surat',  'Bangalore',
       'Pune',  'New Delhi',     'Kanpur',    'Lucknow']
Length: 24, dtype: str

City tier:
<StringArray>
['T30', 'B30']
Length: 2, dtype: str

Age_group:
<StringArray>
['56+', '18-25', '36-45', '26-35', '46-55']
Length: 5, dtype: str

Payment_mode:
<StringArray>
['UPI', 'Cheque', 'Mandate', 'Net Banking']
Length: 4, dtype: str

KYC_status:
<StringArray>
['Verified', 'Pending']
Length: 2, dtype: str