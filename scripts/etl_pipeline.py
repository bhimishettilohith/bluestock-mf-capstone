import pandas as pd
import sqlite3
from pathlib import Path

# Database path
db_path = Path("data/db/bluestock_mf.db")

conn = sqlite3.connect(db_path)

# Load cleaned files

dim_fund = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

fact_nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)

fact_transactions = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

fact_performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)

dim_benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

# Rename columns to match schema

fact_nav = fact_nav.rename(
    columns={"date": "nav_date"}
)

dim_benchmark = dim_benchmark.rename(
    columns={"date": "benchmark_date"}
)

# Load tables

dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

fact_nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

dim_benchmark.to_sql(
    "dim_benchmark",
    conn,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully")

conn.close()