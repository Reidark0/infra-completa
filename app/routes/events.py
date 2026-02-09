from flask import Blueprint, request, jsonify
from app.services.events_services import  create_event, list_events, update_event, delete_event

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["POST"])
def create():
    data = request.get_json()

    if not data:
        return jsonify({"message": "no data provided"}), 400

    required_fields = ["email", "title", "start_time", "end_time"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400
    
    try:
        event = create_event(data["email"], data)
        return jsonify(event), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@events_bp.route("/events", methods=["GET"])
def list_all():
    user_email = request.args.get("email")
    
    if not user_email:
        return jsonify({"message": "email parameter is required"}), 400
    
    events = list_events(user_email)
    return jsonify(events), 200


@events_bp.route("/events/<int:event_id>", methods=["PUT"])
def update(event_id):
    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({"message": "email is required"}), 400

    event = update_event(event_id, data["email"], data)

    if not event:
        return jsonify({"message": "Evento nao encontrado"}), 404
    
    return jsonify(event), 200


@events_bp.route("/events/<int:event_id>", methods=["DELETE"])
def delete(event_id):
    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({"message": "email is required"}), 400
    
    success = delete_event(event_id, data["email"])

    if success:
        return "", 204
    
    return jsonify({"message": "event not found"}), 404
