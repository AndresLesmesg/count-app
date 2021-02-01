from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.settings.development import Config

from app.count.views import view as count_view

db = SQLAlchemy()
mi = Migrate()


def create_app():
    app = Flask(__name__, static_folder="static")
    # load Config object from settings
    app.config.from_object(Config)
    db.init_app(app)
    mi.init_app(app, db)

    # add blueprints
    app.register_blueprint(count_view)
    return app
