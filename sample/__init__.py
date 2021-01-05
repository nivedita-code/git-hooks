# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from sample.utils import commands
from instance import config


def create_app(config_object=config):
    """ Create App."""
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_blueprints(app)
    register_commands(app)
    return app

def register_blueprints(app):
    pass

def register_commands(app):
    pass