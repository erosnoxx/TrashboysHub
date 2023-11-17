from flask import Flask
from dynaconf import FlaskDynaconf
import logging


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    FlaskDynaconf(app, extensions_list=True)
    return app
