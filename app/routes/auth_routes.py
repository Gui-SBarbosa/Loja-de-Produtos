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
from app.services.auth_service import (
    authenticate_user,
    register_user
)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    errors = UserRegisterSchema().validate(data)

    if errors:
        return jsonify(errors), 400

    success, result, status = register_user(data)
    if not success:
        return jsonify(result), status

    user = result
    return jsonify({
        "success": True,
        "message": "Cadastro realizado com sucesso",
        "user": UserResponseSchema().dump(user)
    }), status

@auth_bp.route('/login', methods=['GET'])
def login():
    data = request.get_json()

    errors = UserLoginSchema().validate(data)

    if errors:
        return jsonify(errors), 400

    success, result, status = authenticate_user(data)

    if not success:
        return jsonify(result), status

    return jsonify({
        "success": True,
        "message": "Login realizado com sucesso",
        **result
    }), status