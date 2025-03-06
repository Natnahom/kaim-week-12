import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import re
import os

# Basic EDA
def perform_eda(data):
    """
    Perform exploratory data analysis on the dataset.
    """
    # Descriptive statistics
    print("Descriptive Statistics:")
    print(data.describe())

    # Headline length analysis
    data['headline_length'] = data['headline'].apply(len)
    print("\nHeadline Length Statistics:")
    print(data['headline_length'].describe())

    # Plot headline length distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['headline_length'], bins=30, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()

    # Publisher analysis
    publisher_counts = data['publisher'].value_counts()
    print("\nTop Publishers by Article Count:")
    print(publisher_counts.head(10))

    # Plot top publishers
    plt.figure(figsize=(10, 6))
    publisher_counts.head(10).plot(kind='bar', color='skyblue')
    plt.title("Top 10 Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show()

    # Sentiment analysis
    data['sentiment'] = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    print("\nSentiment Analysis:")
    print(data['sentiment'].describe())

    # Plot sentiment distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['sentiment'], bins=30, kde=True, color='orange')
    plt.title("Distribution of Sentiment Scores")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

    # Word cloud for headlines
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(data['headline']))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Headlines")
    plt.show()

    # Topic modeling using LDA
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(data['headline'])
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(dtm)
    print("\nTop Topics from LDA:")
    for index, topic in enumerate(lda.components_):
        print(f"Topic #{index + 1}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])