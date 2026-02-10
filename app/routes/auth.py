from flask import Blueprint, request, jsonify
from app.services.auth_services import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "JSON invalido"}), 400

    if "email" not in data or "password" not in data:
        return jsonify({"error": "Falta email ou password"}), 400

    user = authenticate_user(data["email"], data["password"])

    try:
        register_user(data["email"], data["password"])
        return jsonify({"message": "Usuario criado", "user": user}), 201
    except ValueError:
        return jsonify({"message": "Usuario ja existe"}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "no data provided"}), 400

    if "email" not in data or "password" not in data:
        return jsonify({"message": "email and password are required"}), 400

    user = authenticate_user(data["email"], data["password"])
    
    if user:
        return jsonify({"message": "Login feito com sucesso", "user": user}), 200

    return jsonify({"message": "Credenciais invalidas"}), 401


