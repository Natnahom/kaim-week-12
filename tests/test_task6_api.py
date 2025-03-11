import pytest
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    # Test the /predict endpoint
    response = client.post('/predict', json={'features': [0.5, 100, 50, 0.2]})
    assert response.status_code == 200
    assert 'prediction' in response.json
    assert isinstance(response.json['prediction'], list)

def test_sentiment_endpoint(client):
    # Test the /sentiment endpoint
    response = client.post('/sentiment', json={'headline': 'Stock prices rise'})
    assert response.status_code == 200
    assert 'sentiment' in response.json
    assert 'score' in response.json
    assert isinstance(response.json['score'], (float, int))