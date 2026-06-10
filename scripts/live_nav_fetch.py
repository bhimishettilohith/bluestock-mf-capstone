"""
Bluestock Mutual Fund Analytics Capstone

Script: live_nav_fetch.py
Purpose: Fetches live NAV data from external APIs and updates mutual fund records.
"""
import pandas as pd
import requests
from pathlib import Path

# Create output folder
output_folder = Path("data/raw/live_nav")
output_folder.mkdir(parents=True, exist_ok=True)

# Scheme codes
schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():
    try:
        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = output_folder / f"{scheme_name}.csv"
        nav_df.to_csv(output_file, index=False)

        print(f"SUCCESS: {scheme_name} saved")
        print(f"Rows: {len(nav_df)}")
        print("-" * 50)

    except Exception as e:
        print(f"ERROR fetching {scheme_name}: {e}")

print("\nLive NAV fetch completed.")