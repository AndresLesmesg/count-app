import os


BASE_DIR = os.getcwd()


class Config():
    SECRET_KEY = os.getenv('SECRET_VALUE')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + 'dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
