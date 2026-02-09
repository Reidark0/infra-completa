from app.extensions import db
from app.models import Event, User


def create_event(user_email, data):
    user = User.query.filter_by(email=user_email).first()

    if not User:
        raise ValueError("user not found")

    event = Event(
        title=data["title"],
        description=data.get("description", ""),
        start_time=data["start_time"],
        end_time=data["end_time"],
        user_id=id
        )

    db.session.add(event)
    db.session.commit()

    return event.to_dict()


def list_events(user_email):
    user = User.query.filter_by(email=user_email).first()
    
    if not user:
        return []

    events = Event.query.filter_by(user_id=user.id).all()
    return [event.to_dict() for event in events]


def update_event(event_id, user_email, data):
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return None
    
    event = Event.query.filter_by(id=event_id, user_id=user.id).first()

    if not event:
        return None

    for field in ["title", "description", "start_time", "end_time"]:
        if field in data:
            setattr(event, field, data[field])

    db.session.commit()
    return event.to_dict()


def delete_event(event_id, user_email):
    user = User.query.filter_by(email=user_email).first()
    
    if not user:
        return False
    
    event = Event.query.filter_by(id=event_id, user_id=user.id).first()

    if event:
        db.session.delete(event)
        db.session.commit()
        return True  
    
    return False