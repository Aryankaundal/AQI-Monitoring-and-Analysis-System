import requests
import streamlit as st
from datetime import datetime


def parse_aqi_data(data, city_name):
    """Parse API response into structured format"""

    aqi_info = data['list'][0]

    return {
        'city': city_name,
        'aqi': aqi_info['main']['aqi'],
        'pm2_5': aqi_info['components'].get('pm2_5', 0),
        'pm10': aqi_info['components'].get('pm10', 0),
        'no2': aqi_info['components'].get('no2', 0),
        'o3': aqi_info['components'].get('o3', 0),
        'co': aqi_info['components'].get('co', 0),
        'so2': aqi_info['components'].get('so2', 0),
        'timestamp': datetime.now()
    }


def fetch_aqi_data(lat, lon, city_name, api_key):
    """Fetch AQI data from OpenWeatherMap Air Pollution API"""

    url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return parse_aqi_data(data, city_name)

        st.warning(
            f"API returned status code {response.status_code} "
            f"for {city_name}"
        )

        return None

    except Exception as e:
        st.error(f"Error fetching data for {city_name}: {e}")
        return None


def get_aqi_category(aqi):
    """Convert AQI number to environmental severity level"""

    categories = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }

    return categories.get(aqi, "Unknown")


def get_aqi_color(aqi):
    """Get dashboard color based on AQI severity"""

    colors = {
        1: "#00E400",
        2: "#FFFF00",
        3: "#FF7E00",
        4: "#FF0000",
        5: "#8F3F97"
    }

    return colors.get(aqi, "#808080")