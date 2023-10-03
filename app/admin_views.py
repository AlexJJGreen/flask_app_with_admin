from flask_admin.contrib.sqla import ModelView
from . import admin, db
from .models import User


def admin_views():
    admin.add_view(ModelView(User, db.session))
