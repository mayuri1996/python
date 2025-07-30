from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
from flask_sqlalchemy import SQLAlchemy
from db_models import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from registration import regisration_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration from config.py file
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Load the trained model and vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)  # Load the vectorizer from the file

with open("model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)  # Load the trained model from the file    

# @app.route('/')
# def home():
#     return "Welcome to the flask App!"

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()  # Get the JSON data from the request
#     text = data['message']
#     user = data.get('user_name', 'Anonymous')
    
#     vect_text = loaded_vectorizer.transform([text])
#     prediction = loaded_model.predict(vect_text)

#     log = PredictionLog(user_name=user,message=text, prediction=prediction[0])
#     db.session.add(log)
#     db.session.commit()

#     return jsonify({"prediction": prediction[0]})

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

with app.app_context():
    db.create_all()

# Register(add) the registration blueprint
app.register_blueprint(regisration_bp, url_prefix='/auth')    

if __name__ == '__main__':
    app.run(debug=True)