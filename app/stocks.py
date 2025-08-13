import yfinance as yf
import pandas as pd

cache = {}

def get_stocks_data(ticker: str, start: str = None, end: str= None):
    key = (ticker.upper(), start, end )

    if key in cache:
        print("Retrived from cache")
        return cache[key]

    df = yf.download(tickers=ticker, start=start, end=end, progress=False)

    if df is None or df.empty:
        raise ValueError("No data found. Please check ticker symbol and date range.")
    
    high = float(df["High"].max())
    low = float(df["Low"].min())
    average = float(df["Close"].mean())
    last_close = float(df["Close"].iloc[-1])

    result = {
        "ticker": ticker.upper(),
        "start": start,
        "end": end,
        "high": round(high, 2),
        "low": round(low, 2),
        "average": round(average, 2),
        "last_close": round(last_close, 2),
    }

    cache[key] = result
    return result