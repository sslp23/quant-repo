import numpy as np
import pandas as pd
from data_retrieve import *

def kelly(portfolio, portfolio_size=10_000):

    #calculate daily returns
    portfolio['Daily Return'] = portfolio['Adj Close'].pct_change()

    # Calculate the expected return (mean of daily returns)
    expected_return = portfolio['Daily Return'].mean()

    # Calculate the variance of daily returns
    variance = portfolio['Daily Return'].var()

    # Apply Kelly formula
    kelly_fraction = expected_return / variance

    optimal_allocation = portfolio_size * kelly_fraction
    #print(optimal_allocation, kelly_fraction, variance, expected_return)
    return pd.DataFrame({
        "Expected Return (Daily)": expected_return,
        "Variance": variance,
        "Kelly Fraction": kelly_fraction,
        "Optimal Allocation": optimal_allocation
    }, index=[0])

def test_kelly():
    #example strat -> long only BTC
    ticker = 'BOVA11.SA'
    data = get_data([ticker], st='2022-09-01', end='2024-12-16')
    portfolio = data[ticker]['Adj Close'].reset_index()#.columns
    portfolio.columns = ['Date', 'Adj Close']
    kelly(portfolio)