from flask import Flask
from flask_jwt_extended import JWTManager
from .models import setup_db, db
from .routes import init_app as init_routes


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    # Usa la URI de tu propia base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # cambia esto por tu propia llave secreta
    app.config['JWT_SECRET_KEY'] = 'tu_llave_secreta_jwt'
    jwt = JWTManager(app)
    setup_db(app)
    with app.app_context():
        db.create_all()  # Esto creará las tablas definidas en tus modelos
    init_routes(app)

    return app
