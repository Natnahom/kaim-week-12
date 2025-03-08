import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer outside the function
analyzer = SentimentIntensityAnalyzer()

# Sentiment analysis with VADER
def analyze_sentiment_vader(headlines):
    """
    Analyze sentiment using VADER for a list of headlines.
    """
    return [analyzer.polarity_scores(headline)['compound'] for headline in headlines]

# Granger causality test
def granger_causality_test(sentiment_scores, stock_returns, maxlag=5, verbose=False):
    """
    Perform Granger causality test between sentiment and stock returns.
    
    Parameters:
    - sentiment_scores: List or Series of sentiment scores.
    - stock_returns: List or Series of stock returns.
    - maxlag: Maximum number of lags to test.
    - verbose: Whether to print detailed output.
    
    Returns:
    - p_values: Dictionary of p-values for each lag tested.
    """
    # Create DataFrame and drop NaN values
    data = pd.DataFrame({'Sentiment': sentiment_scores, 'Returns': stock_returns}).dropna()
    
    if data.empty:
        raise ValueError("No data available after dropping NaN values.")
    
    # Perform Granger causality test
    granger_test = grangercausalitytests(data[['Returns', 'Sentiment']], maxlag=maxlag, verbose=verbose)
    
    # Extract p-values
    p_values = {lag: granger_test[lag][0]['ssr_ftest'][1] for lag in granger_test.keys()}
    
    return p_values
