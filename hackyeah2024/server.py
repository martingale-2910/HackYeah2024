import folium
import streamlit as st

from streamlit_folium import st_folium

def run_server():
    st.title('Rowerem przez Małopolskę')

    # center on Liberty Bell, add marker
    map = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    marker = folium.Marker([39.949610, -75.150282], popup='Liberty Bell', tooltip='Liberty Bell')
    marker.add_to(map)

    # call to render Folium map in Streamlit
    st_data = st_folium(map, width=725)


if __name__ == '__main__':
    run_server()
