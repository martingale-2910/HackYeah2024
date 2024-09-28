import dash_leaflet as dl
from dash import Dash, html
from flask import Flask


def run_selenium():
    pass


def run_flask():
    app = Flask("E-commerce Fraudometer")
    app.add_url_rule('/analyze/<url>', 'show_user', lambda url: f"<p>Analyzing url {url}")
    app.run(debug=True)


def run_dash():
    # A few cities in Denmark.
    cities = [dict(title="Aalborg", position=[57.0268172, 9.837735]),
            dict(title="Aarhus", position=[56.1780842, 10.1119354]),
            dict(title="Copenhagen", position=[55.6712474, 12.5237848])]

    # Create example app.
    app = Dash()
    app.layout = html.Div([
        dl.Map(children=[dl.TileLayer()] + [dl.Marker(**city) for city in cities],
            style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, id="map"),
    ])

    app.run_server()
