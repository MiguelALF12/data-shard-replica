from flask_pymongo import PyMongo

mongo = PyMongo()


def setup_db(app):
    mongo.init_app(app)
    return mongo
