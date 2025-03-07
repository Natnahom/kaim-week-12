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

## Author
- Natnahom Asfaw
- 06/03/2025