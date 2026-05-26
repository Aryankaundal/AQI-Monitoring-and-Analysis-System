import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

APP_TITLE = "🌍 AtmosAI"
APP_SUBTITLE = "Environmental Intelligence & Predictive Health Analytics Platform"

DEFAULT_FORECAST_DAYS = 7
DEFAULT_HISTORICAL_DAYS = 30


SUPPORTED_CITIES = [

    "Delhi",
    "Mumbai",
    "Bangalore",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow",
    "Bhopal",
    "Patna",
    "Chandigarh",
    "Surat",
    "Kanpur",
    "Nagpur",
    "Visakhapatnam",
    "Coimbatore",
    "Indore",
    "Thiruvananthapuram"

]

