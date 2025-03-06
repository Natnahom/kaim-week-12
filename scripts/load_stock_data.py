import pandas as pd

# Load stock data
def load_stock_data(file_path):
    """
    Load stock price data from the given file path.
    """
    try:
        stock_data = pd.read_csv(file_path)
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data.set_index('Date', inplace=True)
        print("Stock data loaded successfully!")
        return stock_data
    except Exception as e:
        print(f"Error loading stock data: {e}")
        return None