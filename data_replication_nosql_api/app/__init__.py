from flask import Flask
from flask_pymongo import PyMongo

# Initialize PyMongo
mongo = PyMongo()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('instance.config.Config')

    # Initialize app for PyMongo
    mongo.init_app(app)

    with app.app_context():
        from .routes import user_routes  # Import routes

        app.register_blueprint(user_routes.user_bp)  # Register blueprints

        return app
