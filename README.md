# This is week-12 of 10 academy

# Task 1: Git and GitHub + Exploratory Data Analysis (EDA)

## Overview
This task focuses on setting up a Python environment, using Git for version control, and performing Exploratory Data Analysis (EDA) on a financial news dataset. The goal is to analyze the dataset to uncover insights about headlines, publishers, publication trends, and sentiment.

## Project Structure
The project is organized as follows:

├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md

## Setup Instructions
1. Prerequisites
Python 3.8 or higher

2. Clone the Repository

3. Set Up the Python Environment
Create a virtual environment and install the required dependencies:

- python -m venv venv
- `venv\Scripts\activate`
- pip install -r requirements.txt

4. Install Required Libraries
The required libraries are listed in requirements.txt. Install them using:

## Usage
1. Running the EDA Script
- Follow the analysis.ipynb

- python notebooks/task1_eda.py
2. Key Functionalities
The script performs the following analyses:

- Descriptive Statistics:

Basic statistics for headline lengths.

Number of articles per publisher.

Trends in publication dates.

- Text Analysis:

Sentiment analysis using TextBlob.

Word cloud generation for headlines.

Topic modeling using Latent Dirichlet Allocation (LDA).

- Visualizations:

Distribution of headline lengths.

Top publishers by article count.

Sentiment score distribution.

Word cloud of headlines.

3. Output
The script generates the following outputs:

Plots: Saved in the notebooks/

Topic Modeling Results: Printed in the console.

Sentiment Scores: Added as a new column in the dataset.

## Detailed Analysis
1. Descriptive Statistics
Headline Length: Analyze the distribution of headline lengths.

Publisher Activity: Identify the most active publishers.

Publication Trends: Analyze trends in publication frequency over time.

2. Text Analysis
Sentiment Analysis: Quantify the sentiment (positive, negative, neutral) of headlines.

Word Cloud: Visualize the most frequent words in headlines.

Topic Modeling: Identify key topics in the headlines using LDA.

3. Visualizations
Headline Length Distribution: Histogram of headline lengths.

Publisher Activity: Bar chart of top publishers.

Sentiment Distribution: Histogram of sentiment scores.

Word Cloud: Visual representation of frequent words.

# Task 2: Quantitative Analysis using PyNance and TA-Lib

## Overview
This task focuses on performing quantitative analysis on stock price data using TA-Lib for technical indicators and PyNance for financial metrics. The goal is to calculate and visualize key technical indicators such as Simple Moving Average (SMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD) to analyze stock price movements.

## Setup Instructions
1. Prerequisites
Python 3.8 or higher

2. Clone the Repository

3. Set Up the Python Environment
Create a virtual environment and install the required dependencies:

- python -m venv venv
- `venv\Scripts\activate`
- pip install -r requirements.txt

4. Install Required Libraries
The required libraries are listed in requirements.txt. Install them using:

- pip install -r requirements.txt

## Usage
1. Running the Technical Analysis Script

- Follow the quantitativeAnalysis.ipynb

2. Key Functionalities
The script performs the following analyses:

- Data Loading:

Load stock price data into a pandas DataFrame.

- Technical Indicators:

Calculate SMA (Simple Moving Average), RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence).

- Visualizations:

Generate candlestick charts with SMA.

Plot RSI and MACD indicators.

3. Output
The script generates the following outputs:

Plots: Saved in the notebooks/ directory.

Technical Indicators: Added as new columns in the stock price DataFrame.

## Detailed Analysis
1. Data Loading
The stock price data is loaded from a CSV file.

The data includes columns for Date, Open, High, Low, Close, and Volume.

2. Technical Indicators
SMA (Simple Moving Average): A 20-day moving average is calculated to identify trends.

RSI (Relative Strength Index): Used to identify overbought or oversold conditions.

MACD (Moving Average Convergence Divergence): Used to identify momentum trends.

3. Visualizations
Candlestick Chart with SMA: Visualizes stock price movements with a 20-day SMA overlay.

RSI Chart: Plots the RSI values to identify overbought or oversold conditions.

MACD Chart: Plots the MACD line and signal line to identify momentum trends.

# Task 3: Correlation Between News Sentiment and Stock Movement

## Overview
This task focuses on analyzing the correlation between financial news sentiment and stock price movements. The goal is to:

Align news sentiment data with stock price data by date.

Perform sentiment analysis on news headlines.

Calculate daily stock returns.

Determine the correlation between news sentiment and stock price movements.

## Setup Instructions

1. Clone the Repository

2. Set Up the Python Environment
Create a virtual environment and install the required dependencies:

- `venv\Scripts\activate`

3. Install Required Libraries
The required libraries are listed in requirements.txt. Install them using:

- pip install -r requirements.txt

## Usage
1. Running the Correlation Analysis Script
The main script for Task 3 is located in src/task3_correlation_analysis.py. To run the script:

- Follow the correlationAnalysis.ipynb

2. Key Functionalities
The script performs the following analyses:

- Data Alignment:

Align news sentiment data with stock price data by date.

- Sentiment Analysis:

Perform sentiment analysis on news headlines using TextBlob and VADER.

- Stock Returns Calculation:

Calculate daily stock returns based on closing prices.

- Correlation Analysis:

Compute the Pearson correlation coefficient between sentiment scores and stock returns.

3. Output
The script generates the following outputs:

- Plots: Saved in the notebooks/ directory.

- Correlation Results: Printed in the console.

## Detailed Analysis
1. Data Alignment
News sentiment data and stock price data are aligned by date to ensure each news item matches the corresponding stock trading day.

2. Sentiment Analysis
- TextBlob: Used for basic sentiment analysis.

- VADER: Used for financial sentiment analysis, providing more accurate sentiment scores for financial text.

3. Stock Returns Calculation
Daily stock returns are calculated as the percentage change in closing prices.

4. Correlation Analysis
The Pearson correlation coefficient is calculated to measure the strength and direction of the relationship between sentiment scores and stock returns.

# Task 4: Advanced Analytics and Machine Learning
## Overview
This task focuses on performing advanced analytics and building machine learning models to predict stock price movements using financial news sentiment and technical indicators. The goal is to:

Perform advanced sentiment analysis using FinBERT.

Conduct topic modeling using Latent Dirichlet Allocation (LDA).

Detect significant market events (e.g., earnings announcements, mergers).

Build and evaluate predictive models using machine learning algorithms.

## Setup Instructions
1. Prerequisites
Python 3.8 or higher

2. Clone the Repository

3. Set Up the Python Environment
Create a virtual environment and install the required dependencies:

- `venv\Scripts\activate`
- pip install -r requirements.txt

4. Install Required Libraries
The required libraries are listed in requirements.txt. Install them using:

- pip install -r requirements.txt

1. Running the Advanced Analytics Script

- Follow the advanced_analyticsAnalysis.ipynb

2. Key Functionalities
The script performs the following analyses:

- Advanced Sentiment Analysis:

Use FinBERT for financial sentiment analysis.

- Topic Modeling:

Apply Latent Dirichlet Allocation (LDA) to uncover hidden topics in headlines.

- Event Detection:

Detect significant market events using keyword-based approaches.

- Predictive Modeling:

Build machine learning models (e.g., Random Forest, LSTM) to predict stock price movements.

Evaluate models using cross-validation and hyperparameter tuning.

3. Output
The script generates the following outputs:

- Plots: Saved in the notebooks/ directory.

- Model Performance Metrics: Printed in the console.

- Topic Modeling Results: Printed in the console.

## Detailed Analysis
1. Advanced Sentiment Analysis
FinBERT: A pre-trained NLP model for financial sentiment analysis was used to classify headlines into Positive, Negative, or Neutral categories.

Aspect-Based Sentiment Analysis (ABSA): Performed to analyze sentiments related to specific aspects of a company (e.g., earnings, management).

2. Topic Modeling
Latent Dirichlet Allocation (LDA): Applied to identify key topics in the headlines.

Keywords: Extracted using TF-IDF and RAKE.

3. Event Detection
Significant market events (e.g., earnings announcements, mergers) were detected using keyword-based approaches.

4. Predictive Modeling
Features: Sentiment scores, technical indicators (e.g., SMA, RSI, MACD, sentiment, finbert_sentiment), and topic distributions.

- Algorithms: Random Forest, Gradient Boosting, and LSTM were used for prediction.

- Evaluation: Models were evaluated using cross-validation and hyperparameter tuning.

## Author
- Natnahom Asfaw
- 06/03/2025