from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    return app