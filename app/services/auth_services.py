from werkzeug.security import generate_password_hash, check_password_hash

_users = {}

def register_user(email: str, password: str):
    if email in _users:
        raise ValueError("Usuário já existe")

    password_hash = generate_password_hash(password)
    _users[email] = password_hash

def authenticate_user(email: str, password:str) -> bool:
    if email not in _users:
        return False

    return check_password_hash(_users[email], password)
