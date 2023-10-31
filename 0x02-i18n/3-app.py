#!/usr/bin/env python3
"""Basic flask app to return a page"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """_summary_

    Returns:
            _type_: _description_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the locale from the request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello_world():
    """function to return index page"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
