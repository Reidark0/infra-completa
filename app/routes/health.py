from flask import Blueprint, jsonify
from app.extensions import db
from sqlalchemy import text

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200

@health_bp.route("/health/live", methods=["GET"])
def liveness():
    return jsonify({"status": "alive"}), 200

@health_bp.route("/health/ready", methods=["GET"])
def readiness():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "ready"}), 200
    except Exception:
        return jsonify({"status": "not ready"}), 503