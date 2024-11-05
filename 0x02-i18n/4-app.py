#!/usr/bin/env python3
"""
4-app.py
A Flask application with Babel and internationalization (i18n) support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

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
    Accept-Language header or from the 'locale' query parameter in the URL.
    Returns:
        str: The best match language code (either 'en' or 'fr').
    """
    # Check if 'locale' parameter is in the URL and if it's a valid locale
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Fallback to the default behavior (browser's Accept-Language header)
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render the 4-index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

