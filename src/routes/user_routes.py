from flask import Blueprint
from controllers.user_controller import create_user, update_user, delete_user

user_bp = Blueprint("user_routes", __name__)

user_bp.add_url_rule("/create", methods=["POST"], view_func=create_user)
user_bp.add_url_rule("/update/<user_id>", methods=["PUT"], view_func=update_user)
user_bp.add_url_rule("/delete/<user_id>", methods=["DELETE"], view_func=delete_user)
