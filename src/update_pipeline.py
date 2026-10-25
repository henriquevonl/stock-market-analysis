from src.database import get_latest_date, insert_stock_data
from src.data_collection import get_stock_prices
import os


def update_stock(ticker):
    latest_date = get_latest_date(ticker)


    if latest_date is None:
        print(f"{ticker}: new company detected. Loading historical data...")

        new_data = get_stock_prices(
            ticker,
            max_records=1271
        )

        if new_data.empty:
            print(f"{ticker}: no historical data found.")
            return

        print(f"{ticker}: {len(new_data)} historical records retrieved.")

        insert_stock_data(new_data)

        print(f"{ticker}: historical data saved to database.")
        return 


    else:
        print(f"{ticker}: latest date in database = {latest_date}")

        new_data = get_stock_prices(
            ticker,
            start_date=latest_date
        )

        if new_data.empty:
            print(f"{ticker}: no new data.")
            return

        print(f"{ticker}: {len(new_data)} new records found.")

        insert_stock_data(new_data)

        print(f"{ticker}: database updated.")



if __name__ == "__main__":
    tickers = ["MSFT", "AAPL", "JPM", "JNJ", "XOM", "WMT", "AMZN", "BAC", "CAT", "CVX", "GE", "GOOG", "GS", "KO", "META", "NVDA", "PFE", "UNH", "TSLA", "MCD"]

    for ticker in tickers:
        try:
            update_stock(ticker)
        except Exception as e:
            print(f"Error updating {ticker}: {e}")

    os.system("pause")
