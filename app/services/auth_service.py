from datetime import timedelta
from sqlite3 import IntegrityError

from flask_jwt_extended import create_access_token

from app.models.user import User, RoleEnum
from app.extension import db


def register_user(data):
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not all([name, email, password, role]):
        return False, {'error': 'Todos os campos são obrigatórios'}, 400

    if len(password) < 8:
        return False, {'error': 'Senha deve ter pelo menos 8 caracteres'}, 400

    if User.query.filter((User.email == email)).first():
        return False, ({'error': 'Email já existente. . .'}), 409

    if role=="SELLER":
        if User.query.filter(User.name == name).first():
            return False, ({'error': 'Já existe uma loja com esse nome. . .'}), 409

    user = User(
        name=name,
        email=email,
        role=RoleEnum(role)
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return True, user, 201


def authenticate_user(data):
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return False, {'error': 'Todos os campos são obrigatórios'}, 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return False, {'error': 'Email ou senha incorretos'}, 401

    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role.name},
        expires_delta=timedelta(hours=2)
    )

    return True, {
        "access_token": access_token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role.name,
        }
    }, 200
