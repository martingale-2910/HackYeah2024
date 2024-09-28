import folium
import streamlit as st
from osmnx import distance, features_from_bbox, geocoder, graph_from_bbox, routing
from streamlit_folium import st_folium

bbox = {'min_lat': 49.880478, 'max_lat': 50.373496,
        'min_lon': 20.478516, 'max_lon': 21.242065}


@st.cache_resource
def get_graph():
    graph = graph_from_bbox(
        bbox=(bbox['max_lat'], bbox['min_lat'], bbox['min_lon'], bbox['max_lon']),
        network_type='bike',
        simplify=False,
        retain_all=True,
    )
    print('Constructed graph')
    return graph


@st.cache_data
def get_coords(locality):
    coords = geocoder.geocode(locality)
    print(f"Getting coords for {locality}")
    return coords


@st.cache_data
def get_marker(locality):
    coords = get_coords(locality)
    return folium.Marker([coords[1], coords[0]], popup=locality, tooltip=locality)


@st.cache_data
def get_route_points(start, end):
    g = get_graph()

    orig = get_coords(start)
    dest = get_coords(end)

    o, _ = distance.nearest_nodes(g, orig[1], orig[0], return_dist=True)
    d, _ = distance.nearest_nodes(g, dest[1], dest[0], return_dist=True)

    route = routing.shortest_path(g, o, d)
    points = [g.nodes[x] for x in route]

    print("Computed route")

    return [(x['y'], x['x']) for x in points]


@st.cache_data
def get_route(origin, destination):
    route_pts = get_route_points(origin, destination)
    print("Plotted route")
    return folium.PolyLine(locations=route_pts, weight=2)


# @st.cache_resource
# def get_map():
#     map_ = folium.Map(
#         max_bounds=True,
#         location=[0.5 * (bbox['min_lat'] + bbox['max_lat']), 0.5 * (bbox['min_lon'] + bbox['max_lon'])],
#         zoom_start=9,
#         tiles='OpenStreetMap',
#         min_lon=19.076385,
#         max_lon=21.432953,
#         min_lat=49.174522,
#         max_lat=50.526524,
#     )
#     print('Constructed map')
#     return map_


@st.cache_data
def get_localities():
    print('Fetching localities')
    x = tuple(
        features_from_bbox(
            bbox=(bbox['max_lat'], bbox['min_lat'], bbox['min_lon'], bbox['max_lon']),
            tags={'place': ['town', 'vilage']},
        )['name'].values
    )
    print('Fetched localities')
    return x


def run_server():
    st.title('Rowerem przez Małopolskę')

    localities = get_localities()

    cont1 = st.container()

    with cont1:
        col1, col2 = st.columns(2)

        with col1:
            origin = st.selectbox('Skąd', localities)

        with col2:
            destination = st.selectbox('Dokąd', localities)

    cont2 = st.container()

    with cont2:
        map_ = folium.Map(
            max_bounds=True,
            location=[0.5 * (bbox['min_lat'] + bbox['max_lat']), 0.5 * (bbox['min_lon'] + bbox['max_lon'])],
            zoom_start=9,
            tiles='OpenStreetMap',
            min_lon=19.076385,
            max_lon=21.432953,
            min_lat=49.174522,
            max_lat=50.526524)
        route = get_route(origin, destination)
        map_.add_child(route)
        origin_marker = get_marker(origin)
        map_.add_child(origin_marker)
        dest_marker = get_marker(destination)
        map_.add_child(dest_marker)
        _st_data = st_folium(map_, width=725)


if __name__ == '__main__':
    run_server()
