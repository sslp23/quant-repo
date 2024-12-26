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

data = get_data(['GLD', 'GDX'], st='2006-05-23', end='2007-11-30')
df1 = data['GLD']
df2 = data['GDX']

df1.columns = df1.columns.get_level_values(0)
df2.columns = df2.columns.get_level_values(0)

df = df1.merge(df2, how='left', on='Date', suffixes=['_GLD', '_GDX'])

df.sort_index(inplace=True)
trainset = np.arange(0, 252)
df = df.iloc[
    trainset,
]

## Run cointegration (Engle-Granger) test

coint_t, pvalue, crit_value = coint(df["Adj Close_GLD"], df["Adj Close_GDX"])
print(
    coint_t,
    pvalue,
    crit_value,
)

## Determine Hedge ratio

model = OLS(df["Adj Close_GLD"], df["Adj Close_GDX"])
results = model.fit()
hedgeRatio = results.params
print("Hedge Ratio")
print(hedgeRatio)

##  spread = GLD - hedgeRatio*GDX

spread = df["Adj Close_GLD"] - hedgeRatio[0] * df["Adj Close_GDX"]
print("Spread")
plt.plot(spread)
plt.show()