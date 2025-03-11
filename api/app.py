from flask import Flask, request, jsonify
import pickle
# from scripts.advanced_analytics import analyze_sentiment_vader

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
    prediction = model.predict([data['features']])
    return jsonify({"prediction": prediction.tolist()})

@app.route("/")
def home():
    return "Stock Price Prediction API"
# @app.route("/sentiment", methods=["POST"])
# def sentiment():
#     """
#     Analyze sentiment of a given headline.
#     """
#     headline = request.json['headline']
#     sentiment, score = analyze_sentiment_vader(headline)
#     return jsonify({"sentiment": sentiment, "score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)