import pytest
import pandas as pd
from scripts.load_stock_data import *
from scripts.calculate_and_visualize import *

def test_load_stock_data():
    # Test loading stock data
    stock_data = load_stock_data("../../Data/yfinance_data/AAPL_historical_data.csv")
    assert isinstance(stock_data, pd.DataFrame)
    assert not stock_data.empty

def test_calculate_indicators():
    # Test calculating technical indicators
    stock_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02'],
        'Open': [100, 105],
        'High': [110, 115],
        'Low': [95, 100],
        'Close': [105, 110],
        'Volume': [1000, 2000]
    })
    stock_data = calculate_indicators(stock_data)
    assert 'SMA_20' in stock_data.columns
    assert 'RSI' in stock_data.columns