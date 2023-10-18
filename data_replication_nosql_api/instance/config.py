from datetime import timedelta
import os


class Config:
    """Base config."""
    SECRET_KEY = str(os.urandom(16))
    JWT_SECRET_KEY = str(os.urandom(16))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=5)
    MONGO_URI = "mongodb+srv://miguellopez:miguel3612@cluster0.2wwkh00.mongodb.net/DATA_REPLICATION_TEST?retryWrites=true&w=majority"  # Your DB URI
