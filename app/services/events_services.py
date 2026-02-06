_events - []
_event_id_counter = 1

def create_event(user_email, data):
    global _event_id_counter

    event = {
        "id": _event_id_counter,
        "user_email": user_email,
        "title": data["title"],
        "description": data.get("description", ""),
        "start_time": data["start_time"],
        "end_time": data["end_time"]
    }

    _events.append(event)
    _event_id_counter += 1
    
    return event


def list_events(user_email):
    return [event for event in _events if event["user_email"] == user_email]


def update_event(event_id, user_email, data):
    for event in _events:
        if event["id"] == event_id and event["user_email"] == user_email:
            event.update(data)
            return event
    return None


def delete_event(event_id, user_email):
    global _events
    _events = [
        event for event in _events
        if not (event["id"] == event_id and event["user_email"] == user_email)
    ]