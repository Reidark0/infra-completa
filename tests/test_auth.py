from app import create_app

def test_register_user_success(client):
    response = client.post("/register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    assert response.status_code == 201
    assert "user" in response.json


def test_login_user_success(client):
    client.post("/register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    response = client.post("/login", json={
        "email":"user@test.com",
        "password":"123456"
    })

    assert response.status_code == 200
    assert "user" in response.json


def test_login_user_wrong_password(client):
    client.post("register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    response = client.post("/login", json={
        "email":"user@test.com",
        "password":"wrong"
    })

    assert response.status_code == 401


def test_register_missing_password(client):
    response = client.post("/register", json={
        "email":"user@test.com"
    })

    assert response.status_code == 400