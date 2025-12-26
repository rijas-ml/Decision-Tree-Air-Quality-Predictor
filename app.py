from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
