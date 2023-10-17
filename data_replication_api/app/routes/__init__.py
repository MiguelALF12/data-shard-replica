from flask import Blueprint
from .user_routes import user_bp


def init_app(app):
    app.register_blueprint(user_bp, url_prefix='/api')
