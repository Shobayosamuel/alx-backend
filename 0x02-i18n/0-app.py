#!/usr/bin/env python3
"""Basic flask app to return a page"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """function to return index page"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
