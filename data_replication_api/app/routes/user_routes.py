from flask import Blueprint, request, jsonify
from ..controllers.user_controller import (
    get_all_users, get_user, create_user, update_user, delete_user, authenticate
)
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/test', methods=['GET'])
def test_api():
    return jsonify({'message': 'La api funciona correctamente'}), 200


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def fetch_users():
    users = get_all_users()
    return jsonify(users)


@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def fetch_user(user_id):
    user = get_user(user_id)
    return jsonify(user)


@user_bp.route('/users', methods=['POST'])
@jwt_required()
def post_user():
    data = request.get_json()
    user = create_user(data['name'], data['email'])
    return jsonify(user), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def put_user(user_id):
    data = request.get_json()
    user = update_user(user_id, data.get('name'), data.get('email'))
    return jsonify(user)


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def remove_user(user_id):
    success = delete_user(user_id)
    return jsonify({'success': success})


@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user = create_user(data['name'], data['email'], data['password'])
    return jsonify(user), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate(data['email'], data['password'])
    if token:
        return jsonify({'access_token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
