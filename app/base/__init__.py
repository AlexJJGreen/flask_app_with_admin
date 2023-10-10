from flask import Blueprint

bp = Blueprint(
    "base",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/",
)

from app.main import routes
