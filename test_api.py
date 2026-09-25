import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("FINANCIAL_DATA_API_KEY")

url = "https://financialdata.net/api/v1/stock-prices"

params = {
    "identifier": "MSFT",
    "key": api_key
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

print(data[0])
print(df.head())
print(df.info())