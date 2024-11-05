#!/usr/bin/env python3
"""
A basic Flask application with Babel for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Configuration for Babel-supported languages and timezone."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

# Instantiate Babel at the module level
babel = Babel(app)

@app.route('/')
def index() -> str:
    """
    Render the index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

