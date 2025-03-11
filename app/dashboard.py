import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlit App
def main():
    st.title("Financial News and Stock Analysis Dashboard")

    # Load data
    data = pd.read_csv("notebooks/merged_data.csv")
    data['date'] = pd.to_datetime(data['date']).dt.tz_localize(None)

    # Sidebar filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", [data['date'].min().date(), data['date'].max().date()])
    stock_symbol = st.sidebar.selectbox("Select Stock Symbol", data['stock'].unique())
    sentiment_score = st.sidebar.slider("Select Sentiment Score Range", -1.0, 1.0, (-1.0, 1.0))

    # Filter data
    filtered_data = data[
        (data['date'] >= pd.Timestamp(date_range[0])) & 
        (data['date'] <= pd.Timestamp(date_range[1])) & 
        (data['stock'] == stock_symbol) & 
        (data['sentiment'].between(sentiment_score[0], sentiment_score[1]))
    ]

    # Data Summary
    st.header("Data Summary")
    st.write(filtered_data.describe())

    # Sentiment Trends
    st.header("Sentiment Trends")
    fig = px.line(filtered_data, x='date', y='sentiment', title="Sentiment Over Time")
    st.plotly_chart(fig)

    # Sentiment Distribution
    st.header("Sentiment Distribution")
    fig = px.histogram(filtered_data, x='sentiment', nbins=30, title="Sentiment Score Distribution")
    st.plotly_chart(fig)

    # Stock Price Movements
    st.header("Stock Price Movements")
    fig = px.bar(
        filtered_data, 
        x='date', 
        y='Close', 
        title="Stock Price Over Time",
        color='Close',  # Color by Close price
        labels={'Close': 'Stock Price'},
        height=400
    )

    # Optionally, you can sort the dates for better visualization
    fig.update_xaxes(type='category')  # Treat x-axis as categorical for better spacing
    st.plotly_chart(fig)

    # Correlation Heatmap
    st.header("Correlation Heatmap")
    corr_matrix = filtered_data[['sentiment', 'daily_return']].corr()
    fig = px.imshow(corr_matrix, text_auto=True, title="Correlation Between Sentiment and Stock Returns")
    st.plotly_chart(fig)

    # Stock Comparison
    st.header("Stock Performance Comparison")
    comparison_symbols = st.multiselect("Select Stocks to Compare", data['stock'].unique(), default=[stock_symbol])
    comparison_data = data[data['stock'].isin(comparison_symbols)]
    comparison_fig = px.line(comparison_data, x='date', y='Close', color='stock', title="Stock Price Comparison")
    st.plotly_chart(comparison_fig)

    # Download Filtered Data
    st.header("Download Filtered Data")
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

if __name__ == "__main__":
    main()