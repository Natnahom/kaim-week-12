# Import libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(headline):
    """
    Perform sentiment analysis using VADER.
    """
    sentiment_score = analyzer.polarity_scores(headline)
    return sentiment_score['compound'], sentiment_score

# Topic Modeling with LDA
def perform_topic_modeling(data, num_topics=5):
    """
    Perform topic modeling using LDA.
    """
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(data['headline'])
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)
    return lda, vectorizer

# Event Detection
def detect_market_events(data, keywords):
    """
    Detect market events based on keywords.
    """
    data['event'] = data['headline'].apply(lambda x: any(keyword in x.lower() for keyword in keywords))
    return data

# Predictive Modeling
def build_predictive_model(data):
    """
    Build a predictive model for stock price movements.
    """
    features = data[['sentiment', 'finbert_sentiment']]
    target = data['daily_return']
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor()
    param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    y_pred = grid_search.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse}")
    return grid_search.best_estimator_
