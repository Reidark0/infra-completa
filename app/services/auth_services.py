from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models import User


def register_user(email: str, password: str):
    if User.query.filter_by(email=email).first():
        raise ValueError("Usuário já existe")

    user = User(
        email=email,
        password_hash = generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()

    return user.to_dict()

def authenticate_user(email: str, password:str) -> bool:
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return None

    if check_password_hash(user.password_hash, password):
        return user.to_dict()
    
    return None
