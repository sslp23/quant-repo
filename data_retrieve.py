import yfinance as yf

# Define a function to fetch historical data for multiple financial symbols
# Parameters:
# - symbols: a list of stock or asset symbols to retrieve data for
# - st: the start date for the data retrieval (default is '2021-09-01')
# - end: the end date for the data retrieval (default is '2024-11-21')
# Returns:
# - A dictionary where keys are symbols and values are DataFrames containing the historical data
def get_data(symbols: list, st='2021-09-01', end='2024-11-21') -> dict:
    data = {}  # Initialize an empty dictionary to store the data

    # Iterate over the list of symbols
    for symbol in symbols:
        print(symbol)  # Print the current symbol being processed
        # Fetch historical data for the current symbol using yfinance (yf) library
        # and store it in the dictionary with the symbol as the key
        data[symbol] = yf.download(symbol, start=st, end=end) 
        
    return data  # Return the dictionary containing the downloaded data