# Stock Market Analysis | Python, PostgreSQL & Power BI

## Overview
An end-to-end data analytics project analyzing historical stock market data from **20 companies across 6 sectors**. The project uses Python for data extraction and processing, PostgreSQL for storage and analysis, and Power BI for visualization.

## Technologies
- **Python:** Pandas, Requests
- **Database:** PostgreSQL, SQL
- **Visualization:** Power BI, DAX
- **Automation:** Windows Task Scheduler
- **Data Source:** FinancialData.net API

## ETL Pipeline
1. **Extract:** Retrieve historical stock prices through an API.
2. **Transform:** Process data, check missing values and duplicates, validate prices, and correct 8 OHLC inconsistencies.
3. **Load:** Store data in PostgreSQL with constraints to prevent duplicate stock-date records.
4. **Update:** Fetch new records for existing companies and historical data for newly added companies.
5. **Automate:** Schedule daily pipeline execution.

## Data Quality
- **25,420 records** across 20 companies.
- No duplicate rows in the analyzed datasets.
- No negative prices or trading volumes.
- 8 OHLC inconsistencies manually corrected. These corrections improve internal consistency but are not independently verified against original market data.

## PostgreSQL Analysis
SQL views calculate:
- Daily and cumulative returns
- Annualized return and volatility
- Sharpe ratio
- Running maximum price and drawdown

## Power BI Dashboard
The interactive dashboard includes three views:
- **Overview:** Compare company performance.
- **Sector Analysis:** Explore performance by sector.
- **Company Analysis:** Examine individual stocks.

<img width="582" height="331" alt="image" src="https://github.com/user-attachments/assets/8aaac1f7-01f7-4c7c-a7af-ffad89e001fb" />


*Disclaimer: This project is for educational purposes and does not constitute financial advice.*
