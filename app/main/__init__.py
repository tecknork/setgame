from flask import Flask
from .config import config_by_name
from mongoengine import connect
from .util.log import Log
import logging


def create_app(config_name):
    """
    Create flask app this is the starter code
    :param config_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    Log.base_config(logging.INFO)
    connect_database(app.config)
    return app


def connect_database(config):
    """
    Creating database connection
    :param config:
    :return:
    """
    logging.info(config["MONGO_DATABASE_NAME"])
    logging.info(config["MONGO_DATABASE_HOST"])
    logging.info(config["MONGO_DATABASE_PORT"])
    
    connect(config["MONGO_DATABASE_NAME"], host=config["MONGO_DATABASE_HOST"], port=int(config["MONGO_DATABASE_PORT"]))
