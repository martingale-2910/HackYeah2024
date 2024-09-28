from dash import Dash, html
from flask import Flask


def run_selenium():
    pass


def run_flask():
    app = Flask("E-commerce Fraudometer")
    app.add_url_rule('/analyze/<url>', 'show_user', lambda url: f"<p>Analyzing url {url}")
    app.run(debug=True)


def run_dash():
    app = Dash()
    app.layout = [html.Div(children='Hello World')]
    app.run(debug=True)
