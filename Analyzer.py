import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

currency = "USD"
metric = "Close"

start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

crypto = ['BTC', 'ETH', 'LTC', 'SOL']
colnames = []

first = True

for ticker in crypto:
  data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
  if first:
    combined = data[[metric]].copy()
    colnames.append(ticker)
    combined.columns = colnames
    first = False
  else:
    combined = combined.join(data[metric])
    colnames.append(ticker)
    combined.columns = colnames


combined = combined.pct_change().corr(method="pearson")

sns.heatmap(combined, annot=True, cmap="rocket")
#plt.show()
plt.savefig('graph.png') #saves plot into a png