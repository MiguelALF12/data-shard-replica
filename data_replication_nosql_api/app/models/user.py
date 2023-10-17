from bson import ObjectId
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    def __init__(self, username, email, password, user_id=None):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.user_id = user_id

    def save(self):
        user_collection = mongo.db.users
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash
        }
        result = user_collection.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def validate_login(username, password):
        user_collection = mongo.db.users
        user = user_collection.find_one({"username": username})
        if user and check_password_hash(user['password_hash'], password):
            return user
        else:
            return None

    @staticmethod
    def update(user_id, data):
        user_collection = mongo.db.users
        result = user_collection.update_one(
            {'_id': ObjectId(user_id)}, {"$set": data})
        return result.modified_count

    @staticmethod
    def delete(user_id):
        user_collection = mongo.db.users
        result = user_collection.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count

    @staticmethod
    def find_all():
        user_collection = mongo.db.users
        users = user_collection.find()
        return users

    @staticmethod
    def find_one(user_id):
        user_collection = mongo.db.users
        user = user_collection.find_one({'_id': ObjectId(user_id)})
        return user
