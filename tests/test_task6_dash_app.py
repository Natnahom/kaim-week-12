import pytest
from dash import Dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.testing import DashRerun

from api.dashDashboard.dash_app import app

@pytest.fixture
def dash_app():
    return app

def test_dash_app(dash_app, dash_duo):
    dash_duo.start_server(dash_app)

    # Test initial layout
    assert dash_duo.find_element("h1").text == "Stock Price Prediction and Sentiment Analysis"

    # Input test values
    dash_duo.find_element("#sentiment-input").send_keys("0.75")
    dash_duo.find_element("#finbert-sentiment-input").send_keys("0.65")
    dash_duo.find_element("#headline-input").send_keys("The company reported strong earnings growth this quarter.")

    # Simulate button clicks
    dash_duo.find_element("#predict-button").click()
    dash_duo.wait_for_text_to_equal("#prediction-output", "Predicted Value:", timeout=5)

    dash_duo.find_element("#sentiment-button").click()
    dash_duo.wait_for_text_to_equal("#sentiment-output", "Sentiment:", timeout=5)