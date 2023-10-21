from bson import ObjectId
from . import mongo
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, name, id, password, phoneNumber, address, occupation, user_id=None):
        self.id = id
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.phoneNumber = phoneNumber
        self.address = address
        self.occupation = occupation
        self.user_id = user_id

    def save(self):
        print("collections: ", mongo.db)
        user_collection = mongo.db.users
        user_data = {
            "name": self.name,
            "id": self.id,
            "password_hash": self.password_hash,
            "phoneNumber": self.phoneNumber,
            "address": self.address,
            "occupation": self.occupation
        }
        result = user_collection.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def validate_login(id, password):
        user_collection = mongo.db.users
        user = user_collection.find_one({"id": id})
        print(user, check_password_hash(user['password_hash'], password))
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
