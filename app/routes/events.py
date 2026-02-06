from flask import Blueprint, request, jsonify
from app.services.events_service import  create_event, list_events, update_event, delete_event

events_bp = Blueprint("events", __name__)

@event_bp.route("/events", methods=["POST"])
def create():
    data = request.get_json()
    event = create_event(data["email"], data)
    return jsonify(event), 201


@event_bp.route("/events", methods=["GET"])
def list_all():
    user_email = request.args.get("email")
    events = list_events(user_email)
    return jsonify(events), 200


@event_bp.route("/events/<int:event_id>", methods=["PUT"])
def update():
    data = request.get_json()
    event = update_event(event_id, data["email"], data)

    if not event:
        return jsonify({"message": "event not found"}), 404
    
    return jsonify(event), 200


@event_bp.route("/events/<int:event_id>", methods=["DELETE"])
def delete(event_id):
    data = request.get_json()
    delete_event(event_id, data["email"])
    return "", 204
