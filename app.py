from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Decision Tree Air Quality Predictor is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [list(data.values())]
    prediction = model.predict(features)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
