from flask import Flask, Blueprint, jsonify, request
from db_models import db, registration
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from werkzeug.security import generate_password_hash

regisration_bp = Blueprint('registration', __name__)

@regisration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('name')
    password = data.get('password')
    email = data.get('email')
    hashed_password = generate_password_hash(password)

    if not username or not password or not email:
        return jsonify({"error":"Missing required fields"}), 400
    
    if registration.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409
    
    new_user = registration(username=username, password=hashed_password, email=email)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201
    
    


