import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SECRET_KEY =  os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PORT = "465"
    MAIL_USE_SSL = True
    FLASK_APP = "run.py"
    FLASK_ENV = "development"