from flask import render_template
from . import main
from ..requests import get_sources, get_articles


@main.route("/")
def index():
    """
    View root page function that returns the index page
    """

    sources = get_sources()
    title = "News from the most Reputable Sources"

    return render_template("index.html", title=title, sources=sources)


@main.route("/articles/<id>")
def articles(id):
    """
    function that returns the articles
    """

    articles = get_articles(id)
    title = f"{id}"

    return render_template("articles.html", title=title, articles=articles)
