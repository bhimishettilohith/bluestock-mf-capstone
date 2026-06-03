-- 1. Total Funds

SELECT COUNT(*) AS total_funds
FROM dim_fund;

-- 2. Total NAV Records

SELECT COUNT(*) AS total_nav_records
FROM fact_nav;

-- 3. Top 5 Funds by AUM

SELECT
    amfi_code,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 4. Average NAV

SELECT
    AVG(nav) AS average_nav
FROM fact_nav;

-- 5. Transactions by State

SELECT
    state,
    COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 6. Funds with Expense Ratio < 1%

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

--------------------------------------------------

-- 7. Average Return by Category

SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM dim_fund d
JOIN fact_performance p
ON d.amfi_code = p.amfi_code
GROUP BY category
ORDER BY avg_return DESC;

--------------------------------------------------

-- 8. Top 5 Funds by Sharpe Ratio

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

--------------------------------------------------

-- 9. Average Transaction Amount

SELECT
    AVG(amount_inr) AS avg_transaction
FROM fact_transactions;

--------------------------------------------------

-- 10. Benchmark Index Summary

SELECT
    index_name,
    AVG(close_value) AS avg_close
FROM dim_benchmark
GROUP BY index_name;