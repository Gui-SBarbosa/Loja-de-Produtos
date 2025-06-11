from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

from app.extension import db
from app.models.user import User, RoleEnum
from app.schemas.user_schema import (
    UserLoginSchema,
    UserRegisterSchema,
    UserResponseSchema
)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    errors = UserRegisterSchema().validate(data)

    if errors:
        return jsonify(errors), 400

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if role not in RoleEnum.__members__:
        print(f"Role inválida: {role}")
        return jsonify({'error': 'Role inválida.'}), 400

    if User.query.filter((User.email == email)).first():
        return jsonify({'error': 'Email já existente. . .'}), 409

    user = User(
        name=name,
        email=email,
        role=RoleEnum(role)
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'Success': 'True',
        'message': 'Usuário criado com sucesso',
        'user': UserResponseSchema().dump(user)
    }), 201

@auth_bp.route('/login', methods=['GET'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    errors = UserLoginSchema().validate(data)

    if errors:
        return jsonify(errors), 400


    if not email or not password:
        print("Email e senha são obrigatórios.")
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        print("Email ou senha inválidos.")
        return jsonify({'error': 'Email ou senha inválidos'}), 401

    acess_token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role.name},
        expires_delta=timedelta(hours=2)
    )
    return jsonify({
        'success': True,
        'message': 'Login realizado com sucesso',
        'token': acess_token}), 200