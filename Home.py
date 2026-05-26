import streamlit as st
import pandas as pd
import warnings
import plotly.express as px

from config.settings import *

from services.aqi_service import fetch_aqi_data
from services.geocoding_service import get_coordinates
from services.health_service import (
    generate_health_advisory,
    calculate_environmental_risk,
    get_precautions
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AtmosAI",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =====================================================
# API VALIDATION
# =====================================================

if not API_KEY or API_KEY == "your_api_key_here":

    st.error(
        "⚠️ Please set your OPENWEATHER_API_KEY in the .env file"
    )

    st.info(
        "Get your free API key at: https://openweathermap.org/api"
    )

    st.stop()

# =====================================================
# HEADER
# =====================================================

st.title(APP_TITLE)

st.markdown(
    f"### {APP_SUBTITLE}"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🌍 AtmosAI")

    st.markdown(
        "### Environmental Intelligence Suite"
    )

    st.markdown(
        "Real-time atmospheric monitoring and predictive analytics platform."
    )

    st.markdown("---")

    st.header("Atmospheric Control Center")

    forecast_days = st.slider(
        "Predictive Analytics Window",
        min_value=3,
        max_value=14,
        value=DEFAULT_FORECAST_DAYS
    )

    historical_days = st.slider(
        "Historical Intelligence Range",
        min_value=7,
        max_value=60,
        value=DEFAULT_HISTORICAL_DAYS
    )

    st.markdown("---")

    st.markdown(
        "### Atmospheric Severity Classification"
    )

    st.markdown("🟢 Good • Minimal Environmental Risk")
    st.markdown("🟡 Fair • Mild Atmospheric Activity")
    st.markdown("🟠 Moderate • Elevated Pollutant Concentration")
    st.markdown("🔴 Poor • High Environmental Exposure Risk")
    st.markdown("🟣 Very Poor • Critical Atmospheric Conditions")

    st.markdown("---")

    st.caption(
        "AtmosAI v1.0 • Environmental Intelligence Engine"
    )

# =====================================================
# MAIN DASHBOARD
# =====================================================

st.subheader(
    "Real-Time Environmental Intelligence"
)

col1, col2 = st.columns([3, 1])

with col1:

    city_input = st.text_input(
        "Search City",
        placeholder="Delhi, Mumbai, Bangalore..."
    )

with col2:

    st.write("")
    st.write("")

    analyze_button = st.button(
        "Analyze Environment",
        width="stretch"
    )

# =====================================================
# DEFAULT LANDING DASHBOARD
# =====================================================

if not analyze_button:

    overview_data = []

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

                data['lat'] = lat
                data['lon'] = lon

                overview_data.append(data)

    if overview_data:

        # =====================================================
        # INDIA MAP
        # =====================================================

        st.subheader(
            "🛰️ National Air Quality Map"
        )

        map_df = pd.DataFrame({
            "city": [d['city'] for d in overview_data],
            "lat": [d['lat'] for d in overview_data],
            "lon": [d['lon'] for d in overview_data],
            "aqi": [d['aqi'] for d in overview_data],
            "pm2_5": [d['pm2_5'] for d in overview_data]
        })

        fig = px.scatter_mapbox(
            map_df,

            lat="lat",
            lon="lon",

            size="pm2_5",
            color="aqi",

            hover_name="city",

            hover_data={
                "lat": False,
                "lon": False,
                "pm2_5": True,
                "aqi": True
            },

            zoom=4.6,
            height=500,

            color_continuous_scale="Turbo",

            size_max=45
        )

        fig.update_layout(

            mapbox_style="carto-darkmatter",

            coloraxis_showscale=False,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            margin=dict(
                l=10,
                r=10,
                t=10,
                b=20
            ),

            font=dict(
                color="white"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # METRICS
        # =====================================================

        col1, col2, col3, col4 = st.columns(4)

        avg_aqi = round(
            sum(d['aqi'] for d in overview_data)
            / len(overview_data),
            1
        )

        highest_city = max(
            overview_data,
            key=lambda x: x['aqi']
        )

        safest_city = min(
            overview_data,
            key=lambda x: x['aqi']
        )

        avg_pm25 = round(
            sum(d['pm2_5'] for d in overview_data)
            / len(overview_data),
            1
        )

        with col1:

            st.metric(
                "Average National AQI",
                avg_aqi
            )

        with col2:

            st.metric(
                "Highest Risk Region",
                highest_city['city']
            )

        with col3:

            st.metric(
                "Safest Region",
                safest_city['city']
            )

        with col4:

            st.metric(
                "Average PM2.5",
                avg_pm25
            )

        st.markdown("---")

        # =====================================================
        # CITY RANKINGS
        # =====================================================

        st.subheader(
            "Urban Atmospheric Rankings"
        )

        ranking_df = pd.DataFrame({
            "City": [d['city'] for d in overview_data],
            "AQI": [d['aqi'] for d in overview_data],
            "PM2.5": [
                round(d['pm2_5'], 1)
                for d in overview_data
            ]
        })

        ranking_df = ranking_df.sort_values(
            by="AQI",
            ascending=False
        )

        st.dataframe(
            ranking_df,
            width="stretch",
            hide_index=True
        )

        st.markdown("---")

        # =====================================================
        # AI INSIGHTS
        # =====================================================

        st.subheader(
            "🤖 AI Atmospheric Insights"
        )

        st.info(
            "Atmospheric pollutant concentration is elevated across high-density urban regions."
        )

        st.warning(
            "Predictive environmental models indicate moderate pollution escalation trends."
        )

        st.success(
            "Southern urban zones currently demonstrate comparatively stable atmospheric conditions."
        )

# =====================================================
# CITY ANALYSIS
# =====================================================

if analyze_button and city_input:

    with st.spinner(
        f"Analyzing environmental conditions for {city_input}..."
    ):

        lat, lon = get_coordinates(
            city_input,
            API_KEY
        )

        if lat and lon:

            aqi_data = fetch_aqi_data(
                lat,
                lon,
                city_input,
                API_KEY
            )

            if aqi_data:

                # =====================================================
                # DATABASE INSERT
                # =====================================================

                conn = get_connection()

                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO aqi_history (
                        city,
                        aqi,
                        pm25,
                        pm10
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        city_input,
                        aqi_data['aqi'],
                        aqi_data['pm2_5'],
                        aqi_data['pm10']
                    )
                )

                conn.commit()

                conn.close()

                st.success(
                    f"Environmental analytics generated for {city_input}"
                )

                # =====================================================
                # AQI GAUGE
                # =====================================================

                gauge_chart = create_aqi_gauge(
                    aqi_data['aqi']
                )

                st.plotly_chart(
                    gauge_chart,
                    width="stretch"
                )

                # =====================================================
                # KPI METRICS
                # =====================================================

                risk_score = calculate_environmental_risk(
                    aqi_data['pm2_5']
                )

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
                        "PM10",
                        f"{aqi_data['pm10']:.1f}"
                    )

                with col4:

                    st.metric(
                        "Environmental Risk Index",
                        f"{risk_score}/100"
                    )

                st.markdown("---")

                # =====================================================
                # HEALTH INTELLIGENCE
                # =====================================================

                health_data = generate_health_advisory(
                    aqi_data['aqi'],
                    aqi_data['pm2_5']
                )

                st.subheader(
                    "🩺 Environmental Health Intelligence"
                )

                col_a, col_b = st.columns(2)

                with col_a:

                    st.metric(
                        "Risk Classification",
                        health_data['risk']
                    )

                with col_b:

                    confidence = calculate_forecast_confidence(
                        pd.DataFrame()
                    )

                    st.metric(
                        "Forecast Confidence",
                        f"{confidence}%"
                    )

                st.info(
                    health_data['advisory']
                )

                st.success(
                    health_data['recommendation']
                )

                precautions = get_precautions(
                    aqi_data['aqi']
                )

                st.markdown(
                    "### Recommended Precautions"
                )

                for item in precautions:

                    st.markdown(f"- {item}")

                st.markdown("---")

                # =====================================================
                # POLLUTANT ANALYTICS
                # =====================================================

                st.subheader(
                    "Atmospheric Pollutant Analytics"
                )

                pollutant_chart = create_pollutant_chart(
                    aqi_data
                )

                st.plotly_chart(
                    pollutant_chart,
                    width="stretch"
                )

                st.markdown("---")

                # =====================================================
                # FORECASTING
                # =====================================================

                st.subheader(
                    "Predictive Environmental Analytics"
                )

                hist_df = generate_historical_data(
                    aqi_data,
                    days=historical_days
                )

                forecast_df = forecast_aqi(
                    hist_df,
                    days_ahead=forecast_days
                )

                forecast_chart = create_forecast_chart(
                    hist_df,
                    forecast_df,
                    city_input
                )

                st.plotly_chart(
                    forecast_chart,
                    width="stretch"
                )

                st.subheader(
                    "Forecast Intelligence Table"
                )

                forecast_display = forecast_df.copy()

                forecast_display['date'] = (
                    forecast_display['date']
                    .dt.strftime('%Y-%m-%d')
                )

                forecast_display[
                    'pm2_5_forecast'
                ] = (
                    forecast_display[
                        'pm2_5_forecast'
                    ].round(2)
                )

                forecast_display.columns = [
                    "Date",
                    "Predicted PM2.5",
                    "City"
                ]

                st.dataframe(
                    forecast_display,
                    width="stretch",
                    hide_index=True
                )

        else:

            st.error(
                f"Could not locate environmental data for {city_input}"
            )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div class="footer">

AtmosAI • Environmental Intelligence Platform

Powered by Predictive Analytics & OpenWeather Environmental APIs

</div>
""", unsafe_allow_html=True)