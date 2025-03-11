import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Price Prediction and Sentiment Analysis"), className="text-center mb-4")
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("Sentiment:"),
            dcc.Input(id='sentiment-input', type='number', placeholder='Enter sentiment value', className='form-control'),
            html.Label("FinBERT Sentiment:"),
            dcc.Input(id='finbert-sentiment-input', type='number', placeholder='Enter FinBERT sentiment value', className='form-control'),
            dbc.Button('Get Prediction', id='predict-button', n_clicks=0, color='primary', className='mt-2'),
            html.Div(id='prediction-output', className='mt-3')
        ], width=6),

        dbc.Col([
            html.Label("Headline for Sentiment Analysis:"),
            dcc.Input(id='headline-input', type='text', placeholder='Enter headline here', className='form-control'),
            dbc.Button('Analyze Sentiment', id='sentiment-button', n_clicks=0, color='success', className='mt-2'),
            html.Div(id='sentiment-output', className='mt-3')
        ], width=6),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='prediction-graph'), width=12)
    ], className='mt-4')
], fluid=True)

# Define the callback for prediction
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    Input('sentiment-input', 'value'),
    Input('finbert-sentiment-input', 'value')
)
def update_prediction(n_clicks, sentiment, finbert_sentiment):
    if n_clicks > 0:
        if sentiment is not None and finbert_sentiment is not None:
            features = [sentiment, finbert_sentiment]
            # Call the Flask API for prediction
            response = requests.post('http://localhost:5000/predict', json={"features": features})
            if response.status_code == 200:
                prediction = response.json().get('prediction', [None])[0]
                return f"Predicted Value: {prediction}"
            else:
                return "Error: Could not get prediction from the API."
        else:
            return "Please enter both sentiment and FinBERT sentiment values."
    return ""

# Define the callback for sentiment analysis
@app.callback(
    Output('sentiment-output', 'children'),
    Input('sentiment-button', 'n_clicks'),
    Input('headline-input', 'value')
)
def analyze_sentiment(n_clicks, headline):
    if n_clicks > 0:
        if headline:
            # Call the Flask API for sentiment analysis
            response = requests.post('http://localhost:5000/sentiment', json={"headline": headline})
            if response.status_code == 200:
                sentiment_result = response.json()
                return f"Sentiment: {sentiment_result.get('sentiment')}, Score: {sentiment_result.get('score')}"
            else:
                return "Error: Could not get sentiment from the API."
        else:
            return "Please enter a headline for sentiment analysis."
    return ""

# Callback for the prediction graph
@app.callback(
    Output('prediction-graph', 'figure'),
    Input('predict-button', 'n_clicks'),
    Input('sentiment-input', 'value'),
    Input('finbert-sentiment-input', 'value')
)
def update_graph(n_clicks, sentiment, finbert_sentiment):
    if n_clicks > 0 and sentiment is not None and finbert_sentiment is not None:
        features = [sentiment, finbert_sentiment]
        response = requests.post('http://localhost:5000/predict', json={"features": features})
        if response.status_code == 200:
            prediction = response.json().get('prediction', [0])[0]
            # Create a bar chart
            fig = go.Figure(data=[
                go.Bar(name='Input Sentiment', x=['Sentiment', 'FinBERT Sentiment'], y=[sentiment, finbert_sentiment]),
                go.Bar(name='Predicted Value', x=['Predicted'], y=[prediction])
            ])
            fig.update_layout(barmode='group', title='Sentiment and Prediction Visualization')
            return fig
    return go.Figure()  # Return an empty figure if no data

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)