from src.database import get_latest_date, insert_stock_data
from src.data_collection import get_stock_prices


def update_stock(ticker):
    latest_date = get_latest_date(ticker)

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