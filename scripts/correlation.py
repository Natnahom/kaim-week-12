import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Sentiment analysis with VADER
def analyze_sentiment_vader(headline):
    """
    Analyze sentiment using VADER.
    """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(headline)['compound']

# Granger causality test
def granger_causality_test(sentiment_scores, stock_returns):
    """
    Perform Granger causality test between sentiment and stock returns.
    """
    data = pd.DataFrame({'Sentiment': sentiment_scores, 'Returns': stock_returns})
    granger_test = grangercausalitytests(data[['Returns', 'Sentiment']], maxlag=5, verbose=False)
    return granger_test
