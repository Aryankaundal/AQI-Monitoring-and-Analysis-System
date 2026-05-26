import numpy as np
import pandas as pd

from datetime import datetime, timedelta

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def generate_historical_data(city_data, days=30):
    """
    Generate simulated historical environmental data
    for predictive analytics.
    """

    np.random.seed(hash(city_data['city']) % 2**32)

    dates = [
        datetime.now() - timedelta(days=i)
        for i in range(days, 0, -1)
    ]

    base = city_data['pm2_5']

    trend = np.linspace(
        base * 0.8,
        base * 1.2,
        days
    )

    seasonal = 20 * np.sin(
        np.linspace(0, 4 * np.pi, days)
    )

    noise = np.random.normal(0, 15, days)

    pm25_history = trend + seasonal + noise

    pm25_history = np.maximum(pm25_history, 10)

    return pd.DataFrame({
        'date': dates,
        'pm2_5': pm25_history,
        'city': city_data['city']
    })


def forecast_aqi(historical_df, days_ahead=7):
    """
    Forecast future PM2.5 concentration using
    polynomial regression.
    """

    historical_df['day_num'] = range(
        len(historical_df)
    )

    X = historical_df[['day_num']].values

    y = historical_df['pm2_5'].values

    poly = PolynomialFeatures(degree=2)

    X_poly = poly.fit_transform(X)

    model = LinearRegression()

    model.fit(X_poly, y)

    future_days = np.array([
        [len(historical_df) + i]
        for i in range(days_ahead)
    ])

    future_poly = poly.transform(future_days)

    forecast = model.predict(future_poly)

    last_date = historical_df['date'].max()

    forecast_dates = [
        last_date + timedelta(days=i + 1)
        for i in range(days_ahead)
    ]

    forecast_df = pd.DataFrame({
        'date': forecast_dates,
        'pm2_5_forecast': np.maximum(forecast, 10),
        'city': historical_df['city'].iloc[0]
    })

    return forecast_df


def calculate_forecast_confidence(forecast_df):
    """
    Generate a simulated confidence score
    for predictive analytics.
    """

    confidence = np.random.randint(82, 96)

    return confidence