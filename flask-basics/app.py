from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)  # Load the vectorizer from the file

with open("model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)  # Load the trained model from the file    

@app.route('/')
def home():
    return "Welcome to the flask App!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from the request
    text = data['message']
    
    vect_text = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(vect_text)
    return jsonify({"prediction": prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)