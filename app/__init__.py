from flask import Flask
from app.routes.auth import auth_bp
from app.routes.events import events_bp

def create_app():
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp)

    return app