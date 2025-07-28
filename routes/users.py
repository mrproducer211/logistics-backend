from flask import Blueprint, jsonify
import json
import os

user_bp = Blueprint("user", __name__)

DATA_PATH = os.path.join("data", "users.json")

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    if not os.path.exists(DATA_PATH):
        return jsonify({"success": False, "error": "User data not found"}), 404

    with open(DATA_PATH, 'r') as f:
        users = json.load(f)

    user_data = list(users.values())[0] if users else {}
    return jsonify({"success": True, "user": user_data}) 