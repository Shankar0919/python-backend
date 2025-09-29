from flask import Flask, jsonify
from routes.user_routes import user_bp
from flasgger import Swagger
from dotenv import load_dotenv
import os

# Load environment variables dynamically based on APP_ENV
app_env = os.environ.get("APP_ENV", "development")
dotenv_file = f".env.{app_env}"
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/api/users")

    swagger_config = {
        "headers": [],
        "specs": [{
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # include all routes
            "model_filter": lambda tag: True,  # include all models
        }],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }

    Swagger(app, config=swagger_config)

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
