from flask import Flask, jsonify
from routes.user_routes import user_bp
from flasgger import Swagger
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/api/users")
    Swagger(app)

    @app.route("/healthcheck")
    def healthcheck():
        """Health check
        ---
        tags:
          - Health
        responses:
          200:
            description: Returns service status
        """
        return jsonify({"status": "ok", "message": "Python Backend Running"})

    return app


if __name__ == "__main__":
    env_name = os.getenv("APP_ENV", "local")
    env_path = os.path.join(os.path.dirname(__file__), "..", "env", f".env.{env_name}")
    load_dotenv(env_path)

    app = create_app()
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", host="127.0.0.1", port=5000)
