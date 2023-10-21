from flask import Flask
# from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from .models import setup_db, mongo
from .routes import init_app as init_routes
from flask_cors import CORS

# Initialize PyMongo
# mongo = PyMongo()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config.from_object('instance.config.Config')

    # Initialize app for PyMongo
    # mongo.init_app(app)
    setup_db(app)

    # with app.app_context():
    #     from .routes import user_routes  # Import routes

    #     app.register_blueprint(user_routes.user_bp)  # Register blueprints
    init_routes(app)
    jwt = JWTManager(app)

    return app
