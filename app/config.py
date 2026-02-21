import os

class Config:
    def get_db_password():
        secret_path = "/mnt/secrets/DB_PASSWORD"
        if os.path.exists(secret_path):
            with open(secret_path) as f:
                return f.read().strip()
        return os.getenv("DB_PASSWORD", "agenda_pass")  # fallback
    
    DB_USER = os.getenv("DB_USER", "agenda_user")
    DB_PASSWORD = get_db_password()
    DB_HOST = os.getenv("DB_HOST", "postgres")
    DB_NAME = os.getenv("DB_NAME", "agenda")
    
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False