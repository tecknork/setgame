from flask import Flask
from .config import config_by_name
from .util.log import Log
import logging


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    Log.base_config(logging.INFO)
    return app
