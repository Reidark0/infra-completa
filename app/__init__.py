from flask import Flask
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    app.register_blueprint(auth_bp)

    return app