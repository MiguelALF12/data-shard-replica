from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import User
from ..models import db


def get_all_users():
    return [u.serialize for u in User.query.all()]


def get_user(user_id):
    return User.query.get(user_id).serialize


def create_user(name, email, password):
    password_hash = generate_password_hash(password)
    new_user = User(name=name, email=email, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize


def update_user(user_id, name=None, email=None):
    user = User.query.get(user_id)
    if name:
        user.name = name
    if email:
        user.email = email
    db.session.commit()
    return user.serialize


def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return True


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return access_token
    else:
        return None
