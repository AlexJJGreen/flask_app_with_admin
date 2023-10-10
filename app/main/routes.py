from flask import render_template
from . import bp


@bp.route("/")
@bp.route("/index")
def index():
    page_title = "Home"
    return render_template("index.html", page_title=page_title)
