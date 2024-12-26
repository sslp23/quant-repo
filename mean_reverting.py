import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint
from statsmodels.api import OLS
from sharpe_ratio import *
from data_retrieve import *

#applying mean reverting strategy between GLD and GDX
#long -> GLD
#short -> GDX

asset_1 = 'GLD'
asset_2 = 'GDX'

data = get_data([asset_1, asset_2], st='2006-05-23', end='2007-11-30')
df1 = data[asset_1]
df2 = data[asset_2]

df1.columns = df1.columns.get_level_values(0)
df2.columns = df2.columns.get_level_values(0)

df = df1.merge(df2, how='left', on='Date', suffixes=['_'+asset_1, '_'+asset_2])

df.sort_index(inplace=True)
trainset = np.arange(0, 252)
df = df.iloc[
    trainset,
]

## Run cointegration (Engle-Granger) test

coint_t, pvalue, crit_value = coint(df["Adj Close_"+asset_1], df["Adj Close_"+asset_2])
print(
    coint_t,
    pvalue,
    crit_value,
)

## Determine Hedge ratio

model = OLS(df["Adj Close_"+asset_1], df["Adj Close_"+asset_2])
results = model.fit()
hedgeRatio = results.params
print("Hedge Ratio")
print(hedgeRatio)

##  spread = GLD - hedgeRatio*GDX

spread = df["Adj Close_"+asset_1] - hedgeRatio[0] * df["Adj Close_"+asset_2]
print("Spread")
plt.plot(spread)
plt.show()