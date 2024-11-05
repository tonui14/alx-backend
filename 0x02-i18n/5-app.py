#!/usr/bin/env python3
"""
5-app.py
A Flask application with Babel, internationalization (i18n), and mocked user login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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

def get_user():
    """
    Retrieve the user based on the 'login_as' URL parameter.
    Returns:
        dict or None: The user dictionary or None if not found.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request():
    """
    Before request handler that sets the user in flask.g.user if logged in.
    """
    g.user = get_user()

@app.route('/')
def index() -> str:
    """
    Render the 5-index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

