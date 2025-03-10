import pytest
import pandas as pd
from scripts.correlation import analyze_sentiment_vader, granger_causality_test

def test_analyze_sentiment_vader():
    # Test sentiment analysis
    sentiment = analyze_sentiment_vader("Stock prices rise")
    assert isinstance(sentiment, float)
    assert -1 <= sentiment <= 1

def test_calculate_daily_returns():
    # Test calculating daily returns
    stock_data = pd.DataFrame({
        'Close': [100, 105, 110]
    })
    returns = granger_causality_test(stock_data)
    assert returns.tolist() == [0.0, 1.0, 1.5476]