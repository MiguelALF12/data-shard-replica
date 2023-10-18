from bson import ObjectId
from . import mongo
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    def __init__(self, name, email, password, telefono, direccion, ocupacion, user_id=None):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.telefono = telefono
        self.direccion = direccion
        self.ocupacion = ocupacion
        self.user_id = user_id

    def save(self):
        print("collections: ", mongo.db)
        user_collection = mongo.db.users
        user_data = {
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "ocupacion": self.ocupacion
        }
        result = user_collection.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def validate_login(email, password):
        user_collection = mongo.db.users
        user = user_collection.find_one({"email": email})
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
