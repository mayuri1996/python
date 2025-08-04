from flask import Flask,Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from db_models import registration


profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = int(get_jwt_identity())  # Get the user ID from the JWT token
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    user = registration.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404  # ✅ Error handled


    return jsonify({
        "data": {
            "id": user.id,
            "name": user.username,
            "email": user.email
        }
    }), 200 