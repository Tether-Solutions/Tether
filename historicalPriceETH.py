import pandas as pd
import yfinance as yf

df = yf.Ticker("ETH-USD").history(period="1mo", interval = "1d")


print(df)