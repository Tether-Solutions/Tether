import pandas as pd
import yfinance as yf

df = yf.Ticker("ETH-USD").history( period="2mo", interval = "5m")

df.to_csv('HourlyPriceData.csv')
print(df)