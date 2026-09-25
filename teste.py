from src.data_collection import get_stock_prices

df = get_stock_prices("MSFT")

print(df.head())
print(df.shape)