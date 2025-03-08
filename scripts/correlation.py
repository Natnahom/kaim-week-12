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
def granger_causality_test(sentiment_scores, stock_returns):
    """
    Perform Granger causality test between sentiment and stock returns.
    """
    data = pd.DataFrame({'Sentiment': sentiment_scores, 'Returns': stock_returns})
    granger_test = grangercausalitytests(data[['Returns', 'Sentiment']], maxlag=5, verbose=False)
    return granger_test
