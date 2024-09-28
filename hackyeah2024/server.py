import dash_leaflet as dl
from dash import Dash, html


def run_server():
    # # A few cities in Denmark.
    # cities = [dict(title="Aalborg", position=[57.0268172, 9.837735]),
    #         dict(title="Aarhus", position=[56.1780842, 10.1119354]),
    #         dict(title="Copenhagen", position=[55.6712474, 12.5237848])]

    # # Create example app.
    # app = Dash()
    # app.layout = html.Div([
    #     dl.Map(children=[dl.TileLayer()] + [dl.Marker(**city) for city in cities],
    #         style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, id="map"),
    # ])


    app = Dash()
    app.layout = dl.Map(dl.TileLayer(), center=[56, 10], zoom=6, style={'height': '50vh'})

    app.run_server()


if __name__ == "__main__":
    run_server()
