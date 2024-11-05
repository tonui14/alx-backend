#!/usr/bin/env python3
"""
0-app.py
A basic Flask web application with a single route that renders an HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Handle the root route and render an HTML template.
    Returns:
        str: The rendered HTML template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

