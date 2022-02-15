import pandas as pd
import yfinance as yf

df = yf.Ticker("ETH-USD").history(period="2d", interval = "1d")


print(df)