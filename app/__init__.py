from flask import Flask
from app.routes.auth import auth_bp
from app.routes.events import events_bp
from app.routes.health import health_bp
from app.config import Config
from app.extensions import db
from flask_cors import CORS

def create_app(config_class=Config, config_override=None):
    app = Flask(__name__)
    app.config.from_object(config_class)
    if config_override:
        app.config.update(config_override)
    print(f"SQLALCHEMY_DATABASE_URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    db.init_app(app)
    
    CORS(app, resources={
        r"/*": {
            "origins": [
                "http://localhost:3000",      # Vite/CRA local
                "http://localhost:5173",      # Vite padrão
                "http://localhost:30007"      # caso front esteja no k8s
            ],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
            }
        })

    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(health_bp)
    
    
    return app