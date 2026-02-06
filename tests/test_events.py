from app import create_app

def register_and_login(client):
    client.post("/register", json={
        "email": "user@test.com",
        "password": "123456"
    })


def test_create_and_list_events():
    app = create_app()
    client = app.test_client()

    register_and_login(client)

    response = client.post("/events", json={
        "email": "user@test.com",
        "title": "Meeting",
        "description": "Team meeting",
        "start_time": "2026-02-10T10:00",
        "end_time": "2026-02-10T11:00"
    })

    assert response.status_code == 201

    response = client.get("/events", query_string={
        "email": "user@test.com"
    })

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["title"] == "Meeting"


def test_update_event():
    app = create_app()
    client = app.test_client()

    register_and_login(client)

    response = client.post("/events", json={
        "email": "user@test.com",
        "title": "Old title",
        "description": "",
        "start_time": "2026-02-10T10:00",
        "end_time": "2026-02-10T11:00"
    })

    assert response.status_code == 201

    response = client.put("/events/1", json={
        "email": "user@test.com",
        "title": "New title"
    })

    assert response.status_code == 200
    assert response.json["title"] == "New title"


def test_delete_event():
    app = create_app()
    client = app.test_client()

    register_and_login(client)

    response = client.post("/events", json={
        "email": "user@test.com",
        "title": "Temp event",
        "description": "",
        "start_time": "2026-02-10T10:00",
        "end_time": "2026-02-10T11:00"
    })

    assert response.status_code == 201

    response = client.delete("/events/1", json={
        "email": "user@test.com"
    })

    assert response.status_code == 204