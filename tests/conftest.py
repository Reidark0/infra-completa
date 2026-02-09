import pytest
from app import create_app
from app.extensions import db as _db
from sqlalchemy import text

@pytest.fixture(scope="function")
def app():
    app = create_app(config_override={
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg://agenda_user:agenda_pass@localhost:5432/agenda_test",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        
        try:
            _db.session.execute(text("SELECT 1"))
            _db.session.commit()
        except Exception as e:
            pytest.fail(f"Não conseguiu conectar no banco de teste: {e}")

        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope="function")
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def db(app):
    # Query em teste aqui
    return _db
