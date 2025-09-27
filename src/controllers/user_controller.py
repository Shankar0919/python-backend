from flask import request, jsonify
from validators.boolean_validator import is_boolean
from validators.date_validator import is_valid_date
from services.user_service import transform_user_data

users = {}

def create_user():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400
    if not is_boolean(data.get("active", "true")):
        return jsonify({"error": "Invalid boolean"}), 400
    if not is_valid_date(data.get("dob", "")):
        return jsonify({"error": "Invalid date"}), 400

    user_id = str(len(users) + 1)
    data["id"] = user_id
    transformed = transform_user_data(data)
    users[user_id] = transformed
    return jsonify({"message": "User created", "data": transformed}), 201

def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if "active" in data and not is_boolean(data["active"]):
        return jsonify({"error": "Invalid boolean"}), 400
    if "dob" in data and not is_valid_date(data["dob"]):
        return jsonify({"error": "Invalid date"}), 400
    existing = users[user_id]
    existing.update(data)
    updated = transform_user_data(existing)
    users[user_id] = updated
    return jsonify({"message": "User updated", "data": updated}), 200

def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"message": "User deleted", "data": deleted}), 200
