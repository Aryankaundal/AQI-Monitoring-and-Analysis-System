import streamlit as st

from config.settings import *

from services.aqi_service import (
    fetch_aqi_data,
    get_aqi_category
)

from services.geocoding_service import (
    get_coordinates
)

from services.health_service import (
    calculate_environmental_risk
)

from utils.charts import (
    create_aqi_gauge,
    create_pollutant_chart
)

st.set_page_config(
    page_title="Command Center",
    layout="wide"
)


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

st.title("🌍 Command Center")

st.caption(
    "Centralized atmospheric intelligence and live environmental monitoring."
)

st.markdown("---")

# =========================================
# CITY SELECT
# =========================================

city = st.selectbox(
    "Select Urban Region",
    SUPPORTED_CITIES
)

lat, lon = get_coordinates(
    city,
    API_KEY
)

if lat and lon:

    aqi_data = fetch_aqi_data(
        lat,
        lon,
        city,
        API_KEY
    )

    if aqi_data:

        risk = calculate_environmental_risk(
            aqi_data['pm2_5']
        )

        # =========================================
        # METRICS
        # =========================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "AQI Level",
                aqi_data['aqi']
            )

        with col2:
            st.metric(
                "PM2.5",
                f"{aqi_data['pm2_5']:.1f}"
            )

        with col3:
            st.metric(
                "Risk Index",
                f"{risk}/100"
            )

        with col4:
            st.metric(
                "Severity",
                get_aqi_category(aqi_data['aqi'])
            )

        st.markdown("---")

        # =========================================
        # GAUGE
        # =========================================

        gauge = create_aqi_gauge(
            aqi_data['aqi']
        )

        st.plotly_chart(
            gauge,
            width="stretch"
        )

        # =========================================
        # POLLUTANTS
        # =========================================

        chart = create_pollutant_chart(
            aqi_data
        )

        st.plotly_chart(
            chart,
            width="stretch"
        )