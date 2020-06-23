import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_DATABASE_HOST = "localhost"
    MONGO_DATABASE_PORT = "27017"
    MONGO_DATABASE_NAME = "setsgame"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_DATABASE_HOST = "localhost"
    MONGO_DATABASE_PORT = "27017"
    MONGO_DATABASE_NAME = "setsgame_test"


class ProductionConfig(Config):
    DEBUG = False
    # when moved to cloud we will need this configuration
    MONGO_DATABASE_HOST = ""
    MONGO_DATABASE_PORT = ""
    MONGO_DATABASE_NAME = "setsgame"


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
