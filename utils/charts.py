import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_aqi_gauge(aqi_level):
    """
    Create AQI gauge visualization.
    """

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=aqi_level,

        title={
            'text': "Environmental Severity Index"
        },

        gauge={
            'axis': {
                'range': [1, 5]
            },

            'bar': {
                'color': "#EF4444"
            },

            'steps': [
                {
                    'range': [1, 2],
                    'color': "#22C55E"
                },
                {
                    'range': [2, 3],
                    'color': "#EAB308"
                },
                {
                    'range': [3, 4],
                    'color': "#F97316"
                },
                {
                    'range': [4, 5],
                    'color': "#DC2626"
                }
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color': "white"},
        height=300
    )

    return fig


def create_pollutant_chart(aqi_data):
    """
    Create pollutant comparison chart.
    """

    pollutants = [
        'PM2.5',
        'PM10',
        'NO₂',
        'O₃',
        'CO',
        'SO₂'
    ]

    values = [
        aqi_data['pm2_5'],
        aqi_data['pm10'],
        aqi_data['no2'],
        aqi_data['o3'],
        aqi_data['co'] / 10,
        aqi_data['so2']
    ]

    df = pd.DataFrame({
        "Pollutant": pollutants,
        "Concentration": values
    })

    fig = px.bar(
        df,
        x="Pollutant",
        y="Concentration",
        color="Concentration",
        title="Atmospheric Pollutant Distribution"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return fig


def create_forecast_chart(hist_df, forecast_df, city_name):
    """
    Create predictive analytics visualization.
    """

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist_df['date'],
        y=hist_df['pm2_5'],
        mode='lines+markers',
        name='Historical Data'
    ))

    fig.add_trace(go.Scatter(
        x=forecast_df['date'],
        y=forecast_df['pm2_5_forecast'],
        mode='lines+markers',
        name='Forecast'
    ))

    fig.update_layout(
        title=f"Predictive Environmental Analytics — {city_name}",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=500
    )

    return fig


def create_city_comparison_chart(all_data):
    """
    Create multi-city AQI comparison chart.
    """

    cities = [d['city'] for d in all_data]

    aqi_values = [d['aqi'] for d in all_data]

    df = pd.DataFrame({
        "City": cities,
        "AQI": aqi_values
    })

    fig = px.bar(
        df,
        x="City",
        y="AQI",
        color="AQI",
        title="Multi-City Environmental Comparison"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return fig


def create_heatmap(all_data):
    """
    Create AQI heatmap visualization.
    """

    cities = [d['city'] for d in all_data]

    aqi_values = [d['aqi'] for d in all_data]

    df = pd.DataFrame({
        "City": cities,
        "AQI": aqi_values
    })

    fig = px.density_heatmap(
        df,
        x="City",
        y="AQI",
        z="AQI",
        color_continuous_scale="RdYlGn_r",
        title="Atmospheric Severity Heatmap"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=400
    )

    return fig