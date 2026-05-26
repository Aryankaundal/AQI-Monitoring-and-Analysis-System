def generate_health_advisory(aqi_level, pm25):
    """
    Generate environmental health recommendations
    based on AQI severity and PM2.5 concentration.
    """

    if aqi_level == 1:
        return {
            "status": "Excellent",
            "risk": "Low",
            "advisory": (
                "Air quality is considered safe for outdoor "
                "activities and prolonged exposure."
            ),
            "recommendation": (
                "Normal outdoor activity is recommended."
            )
        }

    elif aqi_level == 2:
        return {
            "status": "Fair",
            "risk": "Moderate",
            "advisory": (
                "Minor atmospheric pollutants detected. "
                "Sensitive individuals should remain cautious."
            ),
            "recommendation": (
                "Outdoor activity is generally safe."
            )
        }

    elif aqi_level == 3:
        return {
            "status": "Moderate",
            "risk": "Elevated",
            "advisory": (
                "Elevated PM2.5 concentration detected. "
                "Sensitive groups may experience discomfort."
            ),
            "recommendation": (
                "Reduce prolonged outdoor exposure."
            )
        }

    elif aqi_level == 4:
        return {
            "status": "Poor",
            "risk": "High",
            "advisory": (
                "High atmospheric pollution levels detected. "
                "Respiratory discomfort may occur."
            ),
            "recommendation": (
                "Avoid outdoor exercise and wear masks outdoors."
            )
        }

    else:
        return {
            "status": "Hazardous",
            "risk": "Critical",
            "advisory": (
                "Severe environmental conditions detected. "
                "Potential health impacts likely."
            ),
            "recommendation": (
                "Stay indoors and minimize outdoor exposure."
            )
        }


def calculate_environmental_risk(pm25):
    """
    Calculate environmental risk index.
    """

    risk_score = min(int(pm25 * 1.5), 100)

    return risk_score


def get_precautions(aqi_level):
    """
    Generate safety precautions based on AQI severity.
    """

    precautions = {
        1: [
            "Outdoor activities are safe.",
            "Minimal environmental risk detected."
        ],

        2: [
            "Sensitive groups should remain cautious.",
            "Monitor prolonged outdoor exposure."
        ],

        3: [
            "Limit intense outdoor workouts.",
            "Hydration is recommended."
        ],

        4: [
            "Use protective masks outdoors.",
            "Avoid prolonged outdoor exposure.",
            "Children and elderly should remain indoors."
        ],

        5: [
            "Avoid outdoor activities completely.",
            "Use air purification indoors if available.",
            "High respiratory risk detected."
        ]
    }

    return precautions.get(aqi_level, [])