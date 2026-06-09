# Bluestock Mutual Fund Analytics Capstone

## Overview

The Bluestock Mutual Fund Analytics Capstone Project was developed as part of the Bluestock Fintech Data Analyst Internship Program. The objective of this project was to design and implement an end-to-end analytics platform for mutual fund data by integrating data engineering, financial analytics, risk assessment, visualization, and portfolio optimization techniques.

The project covers the complete analytics lifecycle, beginning with data ingestion and cleaning, followed by database design, exploratory data analysis, performance evaluation, dashboard development, advanced risk analytics, and portfolio optimization. In addition to the core requirements, bonus implementations such as automated NAV scheduling, Monte Carlo simulation, and Markowitz Efficient Frontier optimization were successfully completed.

---

# Project Objectives

The primary objectives of this project were:

* Build a robust ETL pipeline for mutual fund datasets.
* Create a structured SQLite database for storing and querying financial data.
* Perform exploratory data analysis to identify trends and patterns.
* Calculate fund performance metrics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown.
* Develop an interactive Power BI dashboard for business users.
* Implement advanced analytics including Value at Risk (VaR), Conditional VaR (CVaR), cohort analysis, and recommendation systems.
* Explore portfolio optimization and forecasting techniques through bonus challenges.
* Maintain a clean and well-documented codebase using Git and GitHub.

---

# Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### Database

* SQLite
* SQL

### Visualization

* Power BI

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

# Project Structure

```text
bluestock_mf_capstone/
├── automation/
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── logs/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   ├── 05_advanced_analytics.ipynb
│   ├── 06_monte_carlo_simulation.ipynb
│   └── 07_efficient_frontier.ipynb
├── reports/
├── scripts/
├── sql/
├── dashboard/
└── README.md
```

---

# Day 1 – Data Ingestion & ETL Pipeline

The first phase focused on collecting and organizing mutual fund datasets. Raw datasets were imported using Pandas, validated, and stored in a structured project directory. A live NAV extraction script was also developed to fetch mutual fund NAV information from external APIs.

### Deliverables

* Data ingestion pipeline
* AMFI validation script
* Live NAV fetch utility
* Raw dataset repository

---

# Day 2 – Data Cleaning & Database Design

During this phase, extensive preprocessing was performed on the mutual fund datasets. Missing values, duplicates, inconsistent formats, and data quality issues were addressed. A relational SQLite database was designed and populated with cleaned datasets to support analytical queries.

### Deliverables

* Clean NAV dataset
* Clean transaction dataset
* SQLite database schema
* SQL analytical queries
* Database integration

---

# Day 3 – Exploratory Data Analysis

The exploratory analysis phase focused on understanding mutual fund industry trends, investor behavior, category performance, and transaction patterns. Multiple visualizations were created to uncover meaningful business insights.

### Key Analyses

* NAV trend analysis
* SIP inflow analysis
* Investor demographic analysis
* Geographic transaction distribution
* Category-wise investment trends
* Correlation analysis
* Industry folio growth analysis

### Deliverables

* EDA notebook
* Business insight visualizations
* Analytical summary report

---

# Day 4 – Fund Performance Analytics

This phase focused on evaluating the performance of mutual funds using widely accepted financial metrics. Historical NAV data was transformed into return series and used to calculate risk-adjusted performance indicators.

### Metrics Calculated

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown

A composite fund scorecard was developed to rank funds based on overall performance and risk-adjusted returns.

### Deliverables

* Returns dataset
* Alpha/Beta report
* Sharpe Ratio report
* Sortino Ratio report
* Maximum Drawdown report
* Fund Scorecard

---

# Day 5 – Interactive Power BI Dashboard

A four-page interactive Power BI dashboard was developed to provide decision-makers with a user-friendly interface for exploring mutual fund analytics.

### Dashboard Pages

### Industry Overview

Provides a high-level view of industry assets under management, SIP inflows, folio growth, and fund house performance.

### Fund Performance

Displays risk-return relationships, fund scorecards, benchmark comparisons, and performance rankings.

### Investor Analytics

Explores investor demographics, geographic investment patterns, transaction types, and investment behavior.

### SIP & Market Trends

Analyzes SIP growth trends, category inflows, market participation, and industry expansion metrics.

### Deliverables

* Power BI dashboard (.pbix)
* Interactive slicers and filters
* Multi-page analytical reporting interface

---

# Day 6 – Advanced Analytics & Risk Metrics

Advanced analytical models were developed to assess risk, identify investor patterns, and support investment recommendations.

### Implementations

### Value at Risk (VaR) & Conditional VaR (CVaR)

Historical VaR and CVaR calculations were performed to estimate potential downside risk under adverse market conditions.

### Rolling Sharpe Ratio

Rolling 90-day Sharpe Ratios were calculated to evaluate changing risk-adjusted performance over time.

### Investor Cohort Analysis

Investors were grouped based on their first investment year to study investment behavior across cohorts.

### SIP Continuity Analysis

Transaction frequency and investment consistency were analyzed to identify investors at risk of discontinuing SIP contributions.

### Recommendation Engine

A rule-based recommendation system was developed to suggest suitable mutual funds based on investor risk appetite.

### Sector Concentration Analysis

Herfindahl-Hirschman Index (HHI) calculations were performed to evaluate portfolio concentration risk.

### Deliverables

* VaR & CVaR report
* Rolling Sharpe analysis
* Cohort analysis report
* SIP continuity report
* Recommendation engine
* Sector concentration report

---

# Automate NAV Scheduler

An automated NAV update system was implemented using Python and Windows Task Scheduler. The system periodically executes NAV update scripts and records execution logs for monitoring and auditing purposes.

### Features

* Automated execution
* Scheduled NAV updates
* Execution logging
* Error handling

---

#  Monte Carlo Simulation

A Monte Carlo simulation framework was developed to forecast future NAV values over a five-year period. Historical return distributions were used to generate multiple possible future scenarios and estimate the range of potential outcomes.

### Benefits

* Future NAV forecasting
* Risk assessment
* Scenario analysis
* Investment uncertainty visualization

---

#  Markowitz Efficient Frontier

Modern Portfolio Theory was applied to construct an Efficient Frontier using selected mutual funds. Thousands of portfolios were simulated to identify optimal asset allocations that maximize returns while minimizing portfolio risk.

### Outputs

* Portfolio return analysis
* Portfolio risk analysis
* Sharpe Ratio optimization
* Optimal portfolio allocation

---

# Key Findings

* Equity-oriented mutual funds generated higher long-term returns but exhibited greater volatility.
* Several funds demonstrated strong risk-adjusted performance through high Sharpe and Sortino Ratios.
* Investor participation increased significantly through SIP investments.
* Portfolio concentration risk varied considerably across fund categories.
* Certain investor cohorts displayed higher average investment amounts and retention rates.
* Monte Carlo simulations indicated substantial long-term growth potential for selected funds.
* Efficient Frontier optimization identified portfolio allocations capable of improving risk-return trade-offs.

---

# Business Recommendations

* Promote SIP-based investing to improve investor retention.
* Encourage diversification to reduce concentration risk.
* Use risk-adjusted metrics alongside returns when evaluating funds.
* Leverage recommendation systems to personalize investor experiences.
* Implement automated reporting and monitoring solutions for portfolio management.

---

# Future Enhancements

Potential improvements include:

* Real-time dashboard refresh using APIs.
* Machine learning-based fund recommendation models.
* Automated email reporting systems.
* Streamlit-based web application deployment.
* Advanced portfolio optimization techniques.
* Integration with cloud-based data pipelines.

---

# How to Run the Project

### Clone Repository

```bash
git clone <repository_url>
cd bluestock_mf_capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Run Recommendation Engine

```bash
python scripts/recommender.py
```

### Open Dashboard

Open the Power BI dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# Author

**Bhimishetti Lohith**

Data Analyst Intern

Bluestock Fintech

June 2026

#
