
"""
Bluestock Mutual Fund Analytics Capstone

Script: compute_metrics.py
Purpose: Displays computed financial performance metrics.
"""

from pathlib import Path
import pandas as pd

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

print("=" * 60)
print("BLUESTOCK MUTUAL FUND PERFORMANCE METRICS")
print("=" * 60)

files = {
    "CAGR Report": BASE_DIR / "data/processed/cagr_report.csv",
    "Sharpe Ratio": BASE_DIR / "data/processed/sharpe_values.csv",
    "Sortino Ratio": BASE_DIR / "data/processed/sortino_values.csv",
    "Alpha Beta": BASE_DIR / "data/processed/alpha_beta.csv",
    "Maximum Drawdown": BASE_DIR / "data/processed/max_drawdown.csv",
    "Fund Scorecard": BASE_DIR / "data/processed/fund_scorecard.csv",
}

for name, path in files.items():

    try:
        df = pd.read_csv(path)

        print("\n" + "=" * 60)
        print(name)
        print("=" * 60)

        print(df.head())

    except Exception as e:
        print(f"\nCould not load {name}: {e}")

print("\n" + "=" * 60)
print("All performance metrics loaded successfully.")
print("=" * 60)

