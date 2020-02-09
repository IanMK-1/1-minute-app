from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing the flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
