from flask import Flask
from app.routes.auth import auth_bp
from app.routes.events import events_bp
from app.routes.health import health_bp
from app.config import Config
from app.extensions import db

def create_app(config_class=Config, config_override=None):
    app = Flask(__name__)
    app.config.from_object(config_class)
    if config_override:
        app.config.update(config_override)
    print(f"SQLALCHEMY_DATABASE_URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    db.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(health_bp)
    
    return app