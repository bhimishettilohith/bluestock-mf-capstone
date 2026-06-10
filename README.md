# Bluestock Mutual Fund Analytics Capstone

## Overview

The Bluestock Mutual Fund Analytics Capstone Project was developed as part of the Bluestock Fintech Data Analyst Internship Program. The objective of this project was to design and implement an end-to-end analytics platform for mutual fund data by integrating data engineering, financial analytics, risk assessment, visualization, automation, and portfolio optimization techniques.

The project covers the complete analytics lifecycle, beginning with data ingestion and cleaning, followed by database design, exploratory data analysis, performance evaluation, dashboard development, advanced risk analytics, portfolio optimization, documentation, and automation. In addition to the core requirements, bonus implementations such as Automated NAV Scheduling, Monte Carlo Simulation, and Markowitz Efficient Frontier Optimization were successfully completed.

---

# Project Objectives

- Build a robust ETL pipeline for mutual fund datasets.
- Create a structured SQLite database for storing and querying financial data.
- Perform exploratory data analysis to identify trends and patterns.
- Calculate industry-standard performance metrics.
- Develop an interactive Power BI dashboard.
- Implement advanced analytics and risk assessment techniques.
- Build a recommendation system based on investor risk appetite.
- Automate NAV updates through scheduled execution.
- Apply portfolio optimization and forecasting techniques.
- Maintain a professional, documented, and reproducible codebase.

---

# Technologies Used

## Programming & Analytics
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Database
- SQLite
- SQL

## Visualization
- Power BI

## Development & Version Control
- VS Code
- Git
- GitHub

## Automation
- Windows Task Scheduler

---

# Project Architecture

```text
Raw Mutual Fund Datasets
          │
          ▼
Data Ingestion & Validation
          │
          ▼
Data Cleaning & Transformation
          │
          ▼
SQLite Database Storage
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Performance Analytics
(CAGR, Sharpe Ratio, Sortino Ratio,
Alpha, Beta, Maximum Drawdown)
          │
          ▼
Advanced Analytics
(VaR, CVaR, Rolling Sharpe,
Cohort Analysis, SIP Continuity,
Recommendation Engine)
          │
          ▼
Power BI Dashboard
          │
          ▼
Portfolio Optimization & Forecasting
(Monte Carlo Simulation,
Efficient Frontier)
```

---

# Project Structure

```text
bluestock_mf_capstone/
├── README.md
├── run_pipeline.py
├── .gitignore
├── data/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
├── logs/
└── automation/
```

---

# Day-wise Work Completed

## Day 1 – Data Ingestion & ETL Pipeline

- Imported and validated mutual fund datasets.
- Built data ingestion workflows.
- Implemented ETL pipeline components.
- Developed NAV fetching utilities.
- Organized project directory structure.

### Deliverables
- Data ingestion pipeline
- AMFI validation script
- NAV fetch utility

---

## Day 2 – Data Cleaning & Database Design

- Cleaned missing and inconsistent records.
- Removed duplicates and standardized formats.
- Designed SQLite database schema.
- Loaded processed datasets into SQLite.
- Executed SQL-based validation queries.

### Deliverables
- Clean datasets
- SQLite database
- SQL schema
- SQL queries

---

## Day 3 – Exploratory Data Analysis

- NAV trend analysis
- SIP inflow analysis
- Investor demographic analysis
- Geographic investment analysis
- Category-wise investment trends
- Correlation analysis
- Industry folio growth analysis

### Deliverables
- EDA notebook
- Visualizations
- Business insights

---

## Day 4 – Fund Performance Analytics

Historical NAV data was transformed into return series and used to calculate risk-adjusted performance metrics.

### Metrics Calculated

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

### Deliverables

- Returns dataset
- CAGR report
- Sharpe Ratio report
- Sortino Ratio report
- Alpha/Beta report
- Maximum Drawdown report
- Fund Scorecard

---

## Day 5 – Interactive Power BI Dashboard

A four-page interactive dashboard was developed to provide business users with actionable insights.

### Dashboard Pages

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends

### Deliverables

- Power BI Dashboard (.pbix)
- Interactive slicers and filters
- KPI reporting pages

---

## Day 6 – Advanced Analytics & Risk Metrics

### Implementations

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Recommendation Engine
- Sector Concentration Analysis (HHI)

### Deliverables

- VaR & CVaR report
- Cohort analysis report
- SIP continuity report
- Recommendation engine
- Sector concentration report

---

## Day 7 – Documentation, Presentation & Deployment

- Final report preparation
- Presentation creation
- Script documentation using docstrings
- Folder-level README files
- GitHub repository organization
- Master pipeline runner implementation
- Final repository validation

### Deliverables

- Final_Report.pdf
- Bluestock_MF_Presentation.pptx
- Root README.md
- Folder-level README files
- run_pipeline.py

---

# Advanced Analytics

## Value at Risk (VaR) & CVaR

Implemented historical risk measurement techniques to estimate potential downside losses under adverse market conditions.

## Rolling Sharpe Ratio

Calculated 90-day rolling Sharpe Ratios to monitor changing risk-adjusted performance over time.

## Cohort Analysis

Grouped investors by first transaction year to identify investment behavior patterns.

## SIP Continuity Analysis

Identified at-risk investors based on SIP transaction gaps.

## Recommendation Engine

Recommended mutual funds according to investor risk appetite and performance metrics.

## Sector Concentration Analysis

Calculated Herfindahl-Hirschman Index (HHI) to evaluate portfolio concentration risk.

---

# Bonus Challenges Completed

## Automated NAV Scheduler

Developed a Python-based automated NAV update process using Windows Task Scheduler. Execution logs are maintained for monitoring and validation.

## Monte Carlo Simulation

Forecasted future NAV growth over a five-year horizon using probabilistic simulations and historical return distributions.

## Markowitz Efficient Frontier

Implemented Modern Portfolio Theory to identify optimal portfolio allocations that maximize risk-adjusted returns.

## Repository Documentation

Added script docstrings, folder-level README files, centralized execution workflow, and improved project maintainability.

---

# Dashboard Overview

The Power BI dashboard provides an interactive business intelligence solution for analyzing mutual fund performance and investor behavior.

### Features

- Interactive slicers
- Dynamic filtering
- Risk-return analysis
- Fund rankings
- Investor segmentation
- Market trend analysis

---

# Documentation & Automation

To improve maintainability and reproducibility:

- Added docstrings to all Python scripts.
- Created README files for major folders.
- Implemented run_pipeline.py.
- Maintained execution logs.
- Organized repository using Git and GitHub.

---

# Key Findings

- Equity-oriented funds demonstrated strong long-term growth potential.
- Risk-adjusted metrics provided deeper insights than returns alone.
- SIP investments significantly contributed to overall fund inflows.
- Investor activity was concentrated in major metropolitan regions.
- Portfolio concentration varied across categories.
- Monte Carlo simulations highlighted future growth opportunities and uncertainty.
- Efficient Frontier optimization improved risk-return trade-offs.

---

# Business Recommendations

- Encourage SIP-based investing.
- Promote diversification across sectors and categories.
- Use risk-adjusted metrics for fund evaluation.
- Personalize recommendations using investor profiles.
- Automate reporting and monitoring workflows.

---

# Future Enhancements

- Real-time API integration.
- Streamlit web application.
- Automated email reporting.
- Cloud deployment.
- Machine learning recommendation models.
- Advanced portfolio optimization techniques.

---

# How to Run the Project

## Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Pipeline

```bash
python run_pipeline.py
```

## Open Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# Final Deliverables

- ETL Pipeline
- SQLite Database
- SQL Schema & Queries
- EDA Notebook
- Performance Analytics Notebook
- Advanced Analytics Notebook
- Monte Carlo Simulation Notebook
- Efficient Frontier Notebook
- Power BI Dashboard
- Recommendation Engine
- Automated NAV Scheduler
- Final Report (PDF)
- Presentation (PPTX)
- GitHub Repository
- Folder-level README Files
- run_pipeline.py

---

# Author

**Bhimishetti Lohith**

Data Analyst Intern

Bluestock Fintech

June 2026
