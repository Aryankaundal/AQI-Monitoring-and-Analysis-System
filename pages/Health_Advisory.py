import streamlit as st

from config.settings import *

from services.aqi_service import (
    fetch_aqi_data
)

from services.geocoding_service import (
    get_coordinates
)

from services.health_service import (
    generate_health_advisory,
    get_precautions
)

st.set_page_config(
    page_title="Health Advisory",
    layout="wide"
)


def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("🩺 Health Advisory")

st.caption(
    "Environmental exposure analysis and healthcare recommendations."
)

st.markdown("---")

city = st.selectbox(
    "Select Urban Region",
    SUPPORTED_CITIES
)

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

    health = generate_health_advisory(
        data['aqi'],
        data['pm2_5']
    )

    st.metric(
        "Health Risk",
        health['risk']
    )

    st.warning(
        health['advisory']
    )

    st.success(
        health['recommendation']
    )

    precautions = get_precautions(
        data['aqi']
    )

    st.markdown("### Recommended Precautions")

    for item in precautions:

        st.markdown(f"- {item}")