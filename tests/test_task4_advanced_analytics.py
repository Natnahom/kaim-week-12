import pytest
import pandas as pd
from scripts.advanced_analytics import analyze_sentiment_vader, perform_topic_modeling

def test_analyze_sentiment_vader():
    # Test VADER sentiment analysis
    sentiment, score = analyze_sentiment_vader("Stock prices rise")
    assert -1 <= score <= 1  # VADER score ranges from -1 (most negative) to 1 (most positive)
    assert isinstance(sentiment, float)  # Sentiment is a float value (compound score)

def test_perform_topic_modeling():
    # Test topic modeling
    data = pd.DataFrame({
        'headline': ['Stock prices rise', 'Market crashes', 'Investors are optimistic']
    })
    lda_model, vectorizer = perform_topic_modeling(data, num_topics=2)
    assert lda_model is not None
    assert vectorizer is not None
    assert len(lda_model.components_) == 2 