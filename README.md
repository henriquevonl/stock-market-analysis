# Stock Market Analysis | Python, PostgreSQL & Power BI

An end-to-end financial data analytics project that automates stock market data collection, stores historical prices in PostgreSQL, and visualizes financial performance through interactive Power BI dashboards.

## Project Overview

This project analyzes stock performance across six sectors: Technology, Consumer, Financials, Industrials, Energy, and Healthcare.

Using Python, PostgreSQL, and Power BI, the project combines data collection, database management, financial analysis, and business intelligence into a single workflow.

### Key Features

- **Automated Data Collection:** Retrieves historical stock data through the [FinancialData.net Stock Prices API](https://financialdata.net/api/v1/stock-prices).
- **ETL Pipeline:** Processes financial data and stores it in PostgreSQL.
- **Incremental Updates:** Retrieves new records for existing companies and historical data for newly added companies.
- **Automated Execution:** Uses Windows Task Scheduler to run daily database updates.
- **Financial Analysis:** Calculates annualized returns, volatility, Sharpe ratio, and maximum drawdown.
- **Interactive Dashboard:** Power BI report with Overview, Sector, and Company views.

## Technologies

- **Python:** Pandas, Requests
- **Database:** PostgreSQL, SQL
- **Business Intelligence:** Power BI, DAX
- **Data Source:** FinancialData.net API


### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd stock-market-analysis
```

### 2. Set up the environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Configure the project

- Set up PostgreSQL and the required database table.
- Configure your API key and database credentials in a local `.env` file.

### 4. Run the pipeline

```powershell
python -m src.update_pipeline
```

The pipeline automatically loads historical data for new companies and updates existing records.

## Power BI Dashboard

The report provides three interactive views:

- **Overview:** High-level performance comparisons.
- **Sector Analysis:** Comparisons across industry sectors.
- **Company Analysis:** Individual stock performance.

<img width="590" height="337" alt="image" src="https://github.com/user-attachments/assets/e99bff95-ebe1-4e0b-ae01-d98a2241dc71" />

---

*Disclaimer: This project is for educational and analytical purposes only and does not constitute investment advice.*
