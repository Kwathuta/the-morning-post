from flask import render_template
from . import main
from ..requests import get_sources


@main.route("/")
def index():
    """
    View root page function that returns the index page
    """

    sources = get_sources()
    title = "News from the most Reputable Sources"

    return render_template("index.html", title=title, sources=sources)
