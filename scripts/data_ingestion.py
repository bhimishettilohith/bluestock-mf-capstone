"""
Bluestock Mutual Fund Analytics Capstone

Script: data_ingestion.py
Purpose: Loads and validates raw mutual fund datasets.

"""
import pandas as pd
from pathlib import Path

# Path to raw data folder
data_path = Path("data/raw")

# Read all CSV files
csv_files = sorted(data_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    try:
        print("=" * 80)
        print(f"FILE: {file.name}")

        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")

print("\nData ingestion completed successfully.")