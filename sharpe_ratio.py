import numpy as np

def long_only_sharpe_ratio(df):
    daily_ret = df['Adj Close'].pct_change()
    
    #EXCESS DAILY -> STRAT RETURNS - FINANCING COSTS (RISK FREE)
    excess_ret = daily_ret - 0.04/252

    sharpe_ratio = np.sqrt(252)*np.mean(excess_ret)/np.std(excess_ret)
    return sharpe_ratio

def market_neutral_sharpe_ratio(df1, df2, instruments: list):
    suffixes = [a for a in instruments]
    df = df1.merge(df2, on='Date', suffixes=suffixes)

    daily_ret = df[[('Adj Close',suffixes[0]), ('Adj Close',suffixes[1])]].pct_change()
    
    net_ret = (daily_ret[('Adj Close',suffixes[0])]-daily_ret[('Adj Close',suffixes[1])])
    sharpe_ratio = np.sqrt(252)*np.mean(net_ret)/np.std(net_ret)
    return sharpe_ratio