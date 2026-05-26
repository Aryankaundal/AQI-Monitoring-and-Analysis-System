import streamlit as st

from config.settings import *

from services.aqi_service import (
    fetch_aqi_data
)

from services.geocoding_service import (
    get_coordinates
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Alert Center",
    layout="wide"
)

# =========================================
# LOAD CSS
# =========================================

def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =========================================
# HEADER
# =========================================

st.title("🚨 Alert Center")

st.caption(
    "Real-time atmospheric threat detection and environmental alert intelligence."
)

st.markdown("---")

# =========================================
# ALERTS
# =========================================

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

            with st.container(border=True):

                col1, col2 = st.columns([1, 5])

                with col1:

                    if data['aqi'] >= 4:
                        st.error("HIGH")

                    elif data['aqi'] == 3:
                        st.warning("MED")

                    else:
                        st.success("LOW")

                with col2:

                    st.subheader(city)

                    if data['aqi'] >= 4:

                        st.write(
                            "High environmental risk detected. "
                            "Outdoor exposure reduction recommended."
                        )

                    elif data['aqi'] == 3:

                        st.write(
                            "Elevated pollutant concentration detected. "
                            "Sensitive groups should remain cautious."
                        )

                    else:

                        st.write(
                            "Environmental conditions are currently stable."
                        )

                    st.metric(
                        "AQI Level",
                        data['aqi']
                    )