from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/prediction_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
    user = data.get('user_name', 'Anonymous')
    
    vect_text = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(vect_text)

    log = PredictionLog(user_name=user,message=text, prediction=prediction[0])
    db.session.add(log)
    db.session.commit()

    return jsonify({"prediction": prediction[0]})

class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    message = db.Column(db.String(500))
    prediction = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)