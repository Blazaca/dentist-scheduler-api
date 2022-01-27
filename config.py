import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:NKd#!a$Ff58X@localhost:5432/scheduler-api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False