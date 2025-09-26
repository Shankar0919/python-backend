from flask import Flask, jsonify
from controllers.user_controller import user_bp
import os
from dotenv import load_dotenv
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/api/users")

    swagger_config = {
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.yaml',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    Swagger(app, config=swagger_config, template_file=os.path.join(os.path.dirname(__file__), "..", "docs", "api_spec.yaml"))

    @app.route("/")
    def health():
        return jsonify({
            "status": "ok",
            "env": os.getenv("FLASK_ENV"),
            "message": "Python Backend Running"
        })

    return app

if __name__ == "__main__":
    env_name = os.getenv("APP_ENV", "local")
    env_path = os.path.join(os.path.dirname(__file__), "..", "env", f".env.{env_name}")
    load_dotenv(env_path)

    app = create_app()
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG") == "1"

    app.run(debug=debug, host=host, port=port)
