import streamlit as st

from config.settings import *

from services.aqi_service import (
    fetch_aqi_data
)

from services.geocoding_service import (
    get_coordinates
)

from ml.forecasting import (
    generate_historical_data,
    forecast_aqi,
    calculate_forecast_confidence
)

from utils.charts import (
    create_forecast_chart
)

st.set_page_config(
    page_title="Forecast Engine",
    layout="wide"
)


def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("📈 Forecast Engine")

st.caption(
    "AI-powered predictive atmospheric forecasting."
)

st.markdown("---")

city = st.selectbox(
    "Select Forecast Region",
    SUPPORTED_CITIES
)

forecast_days = st.slider(
    "Forecast Duration",
    3,
    14,
    7
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

    hist_df = generate_historical_data(
        data
    )

    forecast_df = forecast_aqi(
        hist_df,
        forecast_days
    )

    confidence = calculate_forecast_confidence(
        forecast_df
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Forecast Confidence",
            f"{confidence}%"
        )

    with col2:
        st.metric(
            "Forecast Window",
            f"{forecast_days} Days"
        )

    st.markdown("---")

    chart = create_forecast_chart(
        hist_df,
        forecast_df,
        city
    )

    st.plotly_chart(
        chart,
        width="stretch"
    )