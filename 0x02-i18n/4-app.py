#!/usr/bin/env python3
"""
Flask application Module
with Babel for internationalization
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


def get_locale() -> str:
    """
    Determines the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel: Babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        The rendered HTML content of index.html.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
