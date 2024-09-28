import folium
import streamlit as st

from streamlit_folium import st_folium


def plot_route(map, route_pts):
    route=folium.PolyLine(locations=route_pts, weight=2)
    map.add_child(route)
    return map


def run_server():
    st.title('Rowerem przez Małopolskę')

    cont1 = st.container()

    with cont1:
        col1, col2 = st.columns(2)

        with col1:
            st.text_input("Skąd")

        with col2:
            st.text_input("Dokąd")

    cont2 = st.container()

    map_bound_coordinates=[
        (50.526524, 19.076385),
        (50.526524, 21.432953),
        (49.174522, 21.432953),
        (49.174522, 19.076385),
        (50.526524, 19.076385),
    ]

    # center on Liberty Bell, add marker
    map = folium.Map(
        max_bounds=True,
        location=[0.5*(49.174522 + 50.526524), 0.5*(19.944544 + 21.432953)],
        zoom_start=9,
        tiles='OpenStreetMap',
        min_lon=19.076385,
        max_lon=21.432953,
        min_lat=49.174522,
        max_lat=50.526524
    )
    marker = folium.Marker([50.049683, 19.944544], popup='Kraków', tooltip='Kraków')
    map.add_child(marker)

    map_bounds=folium.PolyLine(locations=map_bound_coordinates, weight=5)

    map.add_child(map_bounds)

    with cont2:
        # call to render Folium map in Streamlit
        st_data = st_folium(map, width=725)


if __name__ == '__main__':
    run_server()
