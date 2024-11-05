#!/usr/bin/env python3
"""
1-app.py
A basic Flask application with Babel support for internationalization.
"""

from flask import Flask, render_template
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

@app.route('/')
def index() -> str:
    """
    Render the 1-index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

