from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView

# from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name="My Admin", template_mode="bootstrap3")
# login = LoginManager()
# login.login_view = "login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    # login.init_app(app)
    admin.init_app(app)

    from app.base import bp as base_bp

    app.register_blueprint(base_bp)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app


# Import models to avoid circular imports
from app import models

# Add admin views after model import
admin.add_view(ModelView(models.User, db.session))
