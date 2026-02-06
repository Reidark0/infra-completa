from flask import Blueprint, request, jsonify
from app.services.events_service import  create_event, list_events, update_event, delete_event

events_bp = Blueprint("events", __name__)