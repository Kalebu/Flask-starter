from logging import debug
from flask import Flask
from app.models import db
from app.cms import cms_bp
from app.auth import auth_bp
from app.home import home_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db, render_as_batch=True)

    # Regestering blueprints
    app.register_blueprint(cms_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
