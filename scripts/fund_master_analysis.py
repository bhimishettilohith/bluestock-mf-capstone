
"""
Bluestock Mutual Fund Analytics Capstone

Script: fund_master_analysis.py
Purpose: Analyzes mutual fund master data including fund categories, fund houses, benchmark indices, and scheme attributes.

"""
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Houses")
print(df["fund_house"].unique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())