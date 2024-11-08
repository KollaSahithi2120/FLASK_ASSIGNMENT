import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secure_secret_key'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_URI') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URI') or 'postgresql://username:password@localhost:5432/app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
