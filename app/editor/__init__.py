from flask import Blueprint

bp = Blueprint(
    "editor",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/editor",
)

from . import routes
