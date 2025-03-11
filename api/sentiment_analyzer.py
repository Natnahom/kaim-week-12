from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(headline):
    """
    Perform sentiment analysis using VADER.
    """
    sentiment_score = analyzer.polarity_scores(headline)
    return sentiment_score['compound'], sentiment_score