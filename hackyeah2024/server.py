import folium
import streamlit as st
from osmnx import distance, features_from_bbox, geocoder, graph_from_bbox, routing
from streamlit_folium import st_folium

bounding_box = {'min_lat': 49.174522, 'max_lat': 50.526524, 'min_lon': 19.076385, 'max_lon': 21.432953}


@st.cache_resource
def get_graph():
    return graph_from_bbox(
        bbox=(bounding_box['max_lat'], bounding_box['min_lat'], bounding_box['min_lon'], bounding_box['max_lon']),
        network_type='bike',
        simplify=False,
        retain_all=True,
    )


@st.cache_data
def get_route_points(start, end):
    G = get_graph()
    orig = geocoder.geocode(start)
    dest = geocoder.geocode(end)
    o, _ = distance.nearest_nodes(G, orig[1], orig[0], return_dist=True)
    d, _ = distance.nearest_nodes(G, dest[1], dest[0], return_dist=True)
    # print(o, d)
    route = routing.shortest_path(G, o, d)
    points = [G.nodes[x] for x in route]
    return [(x['y'], x['x']) for x in points]


def plot_route(map_, route_pts):
    route = folium.PolyLine(locations=route_pts, weight=2)
    map_.add_child(route)
    return map


@st.cache_data
def get_localities():
    print('Fetching localities')
    x = tuple(
        features_from_bbox(
            bbox=(bounding_box['max_lat'], bounding_box['min_lat'], bounding_box['min_lon'], bounding_box['max_lon']),
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

    # center on Liberty Bell, add marker
    map_ = folium.Map(
        max_bounds=True,
        location=[0.5 * (49.174522 + 50.526524), 0.5 * (19.944544 + 21.432953)],
        zoom_start=9,
        tiles='OpenStreetMap',
        min_lon=19.076385,
        max_lon=21.432953,
        min_lat=49.174522,
        max_lat=50.526524,
    )
    marker = folium.Marker([50.049683, 19.944544], popup='Kraków', tooltip='Kraków')
    map_.add_child(marker)

    route_pts = get_route_points(origin, destination)

    plot_route(map_, route_pts)

    with cont2:
        # call to render Folium map in Streamlit
        _st_data = st_folium(map_, width=725)


if __name__ == '__main__':
    run_server()
