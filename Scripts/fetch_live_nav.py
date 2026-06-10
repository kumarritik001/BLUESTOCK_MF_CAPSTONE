"""
Mutual Fund Analytics Capstone

Author: Ritik Kumar

Description:
Mutual fund performance and risk analytics.
"""

from pathlib import Path
import requests
import pandas as pd

scheme_code = 120841

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

BASE_DIR = Path(__file__).resolve().parent.parent
output_file = BASE_DIR / "Data" / "raw" / "Kotak_Bluechip_nav.csv"

df.to_csv(output_file, index=False)

print("Saved successfully")
