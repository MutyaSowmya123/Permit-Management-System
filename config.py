import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'postgresql://postgres:Sowmya@123@localhost:5432/permits')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')
