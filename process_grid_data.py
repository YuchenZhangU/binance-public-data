# %%
import pandas as pd
from datetime import datetime

# %%
cols = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']

# %%
df = pd.read_csv('./fetched/All.csv', names=cols)
df['Open time'] = (df['Open time']/1e3).map(lambda x:datetime.fromtimestamp(x))
df['Close time'] = (df['Close time']/1e3).map(lambda x:datetime.fromtimestamp(x))


df.to_pickle('./data/ETHBTC_2017_2021.pkl')


df = pd.read_pickle(file_name)

# store = pd.HDFStore('store.h5')
# store['df'] = df