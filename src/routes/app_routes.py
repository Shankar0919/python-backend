from flask import Blueprint
from controllers.user_controller import (
    create_user,
    update_user,
    delete_user,
    get_users,
)
from controllers.health_controller import health_check

app_bp = Blueprint("app", __name__)

# User routes
app_bp.add_url_rule("/api/users", "get_users", get_users, methods=["GET"])
app_bp.add_url_rule("/api/users/create", "create_user", create_user, methods=["POST"])
app_bp.add_url_rule("/api/users/update/<user_id>", "update_user", update_user, methods=["PUT"])
app_bp.add_url_rule("/api/users/delete/<user_id>", "delete_user", delete_user, methods=["DELETE"])

# Health route
app_bp.add_url_rule("/healthcheck", "health_check", health_check, methods=["GET"])
