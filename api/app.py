from flask import Flask, request, jsonify
import pickle
from sentiment_analyzer import analyze_sentiment_vader

# Load model
with open("notebooks/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Flask App
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict stock price movement based on sentiment and technical indicators.
    """
    data = request.json

    # Check if data is a list or a dictionary
    if isinstance(data, list):
        return jsonify({"error": "Expected a JSON object, but got a list."}), 400

    # Now data is assumed to be a dictionary
    features = data.get('features')
    if features is None:
        return jsonify({"error": "No features provided"}), 400

    # Ensure features is a list of values
    prediction = model.predict([features])  # Ensure features is in the correct shape
    return jsonify({"prediction": prediction.tolist()})

@app.route("/sentiment", methods=["POST"])
def sentiment():
    """
    Analyze sentiment of a given headline.
    """
    headline = request.json['headline']
    sentiment, score = analyze_sentiment_vader(headline)
    return jsonify({"sentiment": sentiment, "score": score})

@app.route("/")
def home():
    return "<h1 style=\"text-align:center;\">Stock Price Prediction API</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)