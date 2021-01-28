from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mi = Migrate()


def create_app():
    app = Flask(__name__)
    # load config file settings

    db.init_app(app)
    mi.init_app(app, db)

    # add blueprints

    return app
