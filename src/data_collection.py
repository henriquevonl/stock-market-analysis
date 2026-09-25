import os
import pandas as pd
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("FINANCIAL_DATA_API_KEY")

BASE_URL = "https://financialdata.net/api/v1/stock-prices"


def get_stock_prices(ticker, max_records=1000, start_date=None):
    """
    Retrieve historical stock prices from the Financial Data API.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol, e.g. "MSFT".

    max_records : int
        Maximum number of records to retrieve.

    start_date : date, optional
        Only return records after this date.

    Returns
    -------
    pandas.DataFrame
        Historical stock price data.
    """

    # Daily/incremental update:
    # We only need the first API response because the newest
    # records are returned first.
    if start_date is not None:

        params = {
            "identifier": ticker,
            "key": API_KEY,
            "offset": 0
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data)

        if df.empty:
            return df

        df["date"] = pd.to_datetime(df["date"]).dt.date
        start_date = pd.to_datetime(start_date).date()

        df = df[df["date"] > start_date]

        return df

    # Historical download:
    # Retrieve multiple pages when we need a large dataset.
    all_data = []
    offset = 0
    limit = 300

    while len(all_data) < max_records:

        params = {
            "identifier": ticker,
            "key": API_KEY,
            "offset": offset
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        if not data:
            break

        all_data.extend(data)
        offset += limit

        if len(data) < limit:
            break

    df = pd.DataFrame(all_data)

    return df.head(max_records)