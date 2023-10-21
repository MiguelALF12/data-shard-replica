from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers.user_controllers import create_user, get_users, get_user, update_user, delete_user, authenticate

user_bp = Blueprint('user_bp', __name__)

# ... other routes ...


@user_bp.route('/test', methods=['GET'])
def test_api():
    return jsonify({'message': 'La api funciona correctamente'}), 200


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def fetch_users():
    return get_users()


@user_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def fetch_user(user_id):
    return get_user(user_id)


@user_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
def change_user(user_id):
    data = request.get_json()
    return update_user(user_id, data)


@user_bp.route('/<user_id>', methods=['DELETE'])
@jwt_required()
def remove_user(user_id):
    return delete_user(user_id)

# ... other imports ...


@user_bp.route('/signup', methods=['POST'])
def register_user():
    data = request.get_json()
    user = create_user(data['name'], data['id'], data['password'], data['phoneNumber'], data['address'],data['occupation'] )
    return jsonify(user), 201


@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    token = authenticate(data['id'], data['password'])
    if token:
        return jsonify({'access_token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
