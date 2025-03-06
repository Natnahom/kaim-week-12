import talib
import plotly.graph_objects as go

# Calculate technical indicators
def calculate_indicators(stock_data):
    """
    Calculate technical indicators using TA-Lib.
    """
    stock_data['SMA_20'] = talib.SMA(stock_data['Close'], timeperiod=20)
    stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)
    stock_data['MACD'], stock_data['MACD_signal'], stock_data['MACD_hist'] = talib.MACD(
        stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    stock_data['ATR'] = talib.ATR(stock_data['High'], stock_data['Low'], stock_data['Close'], timeperiod=14)
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
