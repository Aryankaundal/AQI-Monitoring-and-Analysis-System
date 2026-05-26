import requests
import streamlit as st


def get_coordinates(city_name, api_key):
    """
    Fetch latitude and longitude using
    OpenWeather Geocoding API.
    """

    try:
        url = (
            f"http://api.openweathermap.org/geo/1.0/direct"
            f"?q={city_name},IN&limit=1&appid={api_key}"
        )

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if len(data) > 0:

                return (
                    float(data[0]["lat"]),
                    float(data[0]["lon"])
                )

            st.warning(
                f"No geolocation data found for {city_name}"
            )

            return None, None

        st.error(
            f"Geocoding API error "
            f"{response.status_code}: {response.text}"
        )

        return None, None

    except Exception as e:

        st.error(
            f"Error fetching coordinates: {e}"
        )

        return None, None