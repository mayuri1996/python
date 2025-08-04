from flask import Blueprint, Flask, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from db_models import registration

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return jsonify({"error": "Email and password are required"}), 400
    
    user = registration.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    if user is None:
        return jsonify({"error": "Invalid email or password"}), 401
    
    access_token = create_access_token(identity=str(user.id))
    return jsonify({"message": "Login successful", "access_token": access_token,"userId":user.id}), 201
