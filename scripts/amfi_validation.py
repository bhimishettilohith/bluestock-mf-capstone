"""
Bluestock Mutual Fund Analytics Capstone

Script: amfi_validation.py
Purpose: Validates AMFI codes and verifies mutual fund scheme information.

"""
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Fund Master Codes: {len(master_codes)}")
print(f"NAV History Codes: {len(nav_codes)}")
print(f"Missing Codes: {len(missing_codes)}")

if len(missing_codes) == 0:
    print("SUCCESS: All AMFI codes exist in NAV history.")
else:
    print(missing_codes)