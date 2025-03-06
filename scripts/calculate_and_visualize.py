import plotly.graph_objects as go
import numpy as np

# Calculate technical indicators
def calculate_indicators(stock_data):
    """
    Calculate technical indicators without TA-Lib.
    """
    # Simple Moving Average (SMA)
    stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()

    # Relative Strength Index (RSI)
    delta = stock_data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))

    # Moving Average Convergence Divergence (MACD)
    stock_data['EMA_12'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
    stock_data['EMA_26'] = stock_data['Close'].ewm(span=26, adjust=False).mean()
    stock_data['MACD'] = stock_data['EMA_12'] - stock_data['EMA_26']
    stock_data['MACD_signal'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()
    stock_data['MACD_hist'] = stock_data['MACD'] - stock_data['MACD_signal']

    # Average True Range (ATR)
    stock_data['H-L'] = stock_data['High'] - stock_data['Low']
    stock_data['H-PC'] = abs(stock_data['High'] - stock_data['Close'].shift(1))
    stock_data['L-PC'] = abs(stock_data['Low'] - stock_data['Close'].shift(1))
    stock_data['TR'] = stock_data[['H-L', 'H-PC', 'L-PC']].max(axis=1)
    stock_data['ATR'] = stock_data['TR'].rolling(window=14).mean()

    return stock_data

# Visualize stock data with indicators
def visualize_stock_data(stock_data):
    """
    Visualize stock data with technical indicators using Plotly.
    """
    fig = go.Figure()

    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name="Candlestick"
    ))

    # SMA
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['SMA_20'],
        name="SMA 20",
        line=dict(color='blue', width=2)
    ))

    # MACD
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['MACD'],
        name="MACD",
        line=dict(color='green', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['MACD_signal'],
        name="MACD Signal",
        line=dict(color='red', width=2)
    ))

    # RSI
    fig_rsi = go.Figure()
    fig_rsi.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['RSI'],
        name="RSI",
        line=dict(color='purple', width=2)
    ))

    # Layout
    fig.update_layout(title="Stock Price with Technical Indicators", xaxis_title="Date", yaxis_title="Price")
    fig_rsi.update_layout(title="RSI", xaxis_title="Date", yaxis_title="RSI Value")

    # Show plots
    fig.show()
    fig_rsi.show()
