# Data Dictionary

## dim_fund

| Column            | Type    | Description                          |
| ----------------- | ------- | ------------------------------------ |
| amfi_code         | INTEGER | Unique mutual fund scheme identifier |
| fund_house        | TEXT    | Mutual fund company                  |
| scheme_name       | TEXT    | Name of scheme                       |
| category          | TEXT    | Scheme category                      |
| sub_category      | TEXT    | Scheme sub-category                  |
| plan              | TEXT    | Regular or Direct                    |
| launch_date       | DATE    | Fund launch date                     |
| benchmark         | TEXT    | Benchmark index                      |
| expense_ratio_pct | REAL    | Expense ratio percentage             |
| risk_category     | TEXT    | Risk classification                  |

## fact_nav

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | INTEGER | Fund identifier |
| nav_date  | DATE    | NAV date        |
| nav       | REAL    | Net Asset Value |

## fact_transactions

| Column           | Type | Description                |
| ---------------- | ---- | -------------------------- |
| investor_id      | TEXT | Investor identifier        |
| transaction_date | DATE | Transaction date           |
| amount_inr       | REAL | Transaction amount         |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| state            | TEXT | Investor state             |
| kyc_status       | TEXT | Verified / Pending         |

## fact_performance

| Column         | Type | Description          |
| -------------- | ---- | -------------------- |
| return_1yr_pct | REAL | 1-Year return        |
| return_3yr_pct | REAL | 3-Year return        |
| return_5yr_pct | REAL | 5-Year return        |
| sharpe_ratio   | REAL | Risk-adjusted return |
| alpha          | REAL | Excess return        |
| beta           | REAL | Market sensitivity   |

## dim_benchmark

| Column         | Type | Description    |
| -------------- | ---- | -------------- |
| benchmark_date | DATE | Index date     |
| index_name     | TEXT | Benchmark name |
| close_value    | REAL | Closing value  |
