import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'postgresql://username:password@lUHJRpermits')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')
