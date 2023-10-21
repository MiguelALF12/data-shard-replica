from datetime import timedelta
import os


class Config:
    """Base config."""
    SECRET_KEY = str(os.urandom(16))
    JWT_SECRET_KEY = str(os.urandom(16))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=5)
    MONGO_URI = "mongodb://127.0.0.1:27117,127.0.0.1:27118/MyDatabase"  # Your DB URI
