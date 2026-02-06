from app import create_app

def test_register_user_success():
    app = create_app()
    client = app.test_client()

    response = client.post("/register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    assert response.status_code == 201
    assert response.json["message"] == "Usuario criado"

def rest_login_user_success():
    app = create_app()
    client = app.test_client()

    client.post("/register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    response = client.post("/login", json={
        "email":"user@test.com",
        "password":"123456"
    })

    assert response.status_code == 200
    assert response.jason["message"] == "Login feito com sucesso"

def test_login_user_wrong_password():
    app = create_app()
    client = app.test_client()

    client.post("register", json={
        "email":"user@test.com",
        "password":"123456"
    })

    response = client.post("/login", json={
        "email":"user@test.com",
        "password":"wrong"
    })

    assert response.status_code == 401

def test_register_missing_password():
    app = create_app()
    client = app.test_client()

    response = client.post("/register", json={
        "email":"user@test.com"
    })

    assert response.status_code == 400