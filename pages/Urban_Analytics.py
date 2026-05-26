import streamlit as st

from config.settings import *

from services.aqi_service import (
    fetch_aqi_data
)

from services.geocoding_service import (
    get_coordinates
)

from utils.charts import (
    create_city_comparison_chart
)

st.set_page_config(
    page_title="Urban Analytics",
    layout="wide"
)


def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("🏙️ Urban Analytics")

st.caption(
    "Comparative atmospheric intelligence across urban regions."
)

st.markdown("---")

all_data = []

for city in SUPPORTED_CITIES:

    lat, lon = get_coordinates(
        city,
        API_KEY
    )

    if lat and lon:

        data = fetch_aqi_data(
            lat,
            lon,
            city,
            API_KEY
        )

        if data:
            all_data.append(data)

chart = create_city_comparison_chart(
    all_data
)

st.plotly_chart(
    chart,
    width="stretch"
)