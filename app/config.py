import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://agenda_user:agenda_pass@localhost:5432/agenda"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

