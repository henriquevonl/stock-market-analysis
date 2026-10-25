import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def insert_stock_data(df):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO stock_prices (
            trading_symbol,
            date,
            open,
            high,
            low,
            close,
            volume
        )
        VALUES %s
        ON CONFLICT (trading_symbol, date)
        DO NOTHING;
    """

    data = [
        (
            row["trading_symbol"],
            row["date"],
            row["open"],
            row["high"],
            row["low"],
            row["close"],
            row["volume"]
        )
        for _, row in df.iterrows()
    ]

    execute_values(cursor, query, data)


    connection.commit()

    cursor.close()
    connection.close()


def get_latest_date(ticker):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT MAX(date)
        FROM stock_prices
        WHERE trading_symbol = %s;
    """

    cursor.execute(query, (ticker,))

    latest_date = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return latest_date



def get_stock_symbols():
    connection = get_connection()

    query = """
        SELECT trading_symbol
        FROM dim_stock
        ORDER BY trading_symbol;
    """

    cursor = connection.cursor()
    cursor.execute(query)

    symbols = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return symbols