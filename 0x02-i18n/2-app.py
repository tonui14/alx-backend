#!/usr/bin/env python3
"""
2-app.py
A basic Flask application with Babel support for internationalization and language selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determine the best match for the user's preferred language from the browser's
    Accept-Language header.
    Returns:
        str: The best match language code (either 'en' or 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render the 2-index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

