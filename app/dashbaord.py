# Import libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlit App
def main():
    st.title("Financial News and Stock Analysis Dashboard")
    
    # Load data
    data = pd.read_csv("../notebooks/merged_data.csv")
    
    # Sidebar filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", [data['date'].min(), data['date'].max()])
    stock_symbol = st.sidebar.selectbox("Select Stock Symbol", data['stock'].unique())
    sentiment_score = st.sidebar.slider("Select Sentiment Score Range", -1.0, 1.0, (-1.0, 1.0))
    
    # Filter data
    filtered_data = data[
        (data['date'] >= date_range[0]) & 
        (data['date'] <= date_range[1]) & 
        (data['stock'] == stock_symbol) & 
        (data['sentiment'].between(sentiment_score[0], sentiment_score[1]))
    ]
    
    # Sentiment Trends
    st.header("Sentiment Trends")
    fig = px.line(filtered_data, x='date', y='sentiment', title="Sentiment Over Time")
    st.plotly_chart(fig)
    
    # Stock Price Movements
    st.header("Stock Price Movements")
    fig = px.line(filtered_data, x='date', y='Close', title="Stock Price Over Time")
    st.plotly_chart(fig)
    
    # Correlation Heatmap
    st.header("Correlation Heatmap")
    corr_matrix = filtered_data[['sentiment', 'daily_return']].corr()
    fig = px.imshow(corr_matrix, text_auto=True, title="Correlation Between Sentiment and Stock Returns")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()