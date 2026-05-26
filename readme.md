# Air Quality Analysis & Forecasting System

A web-based Air Quality Index (AQI) monitoring and forecasting application developed using Python and Streamlit. The system provides real-time air quality insights, pollutant analysis, trend visualization, and machine learning-based forecasting for Indian cities.

## Live Demo
https://air-quality-analysis-olnmtutzp5vszazg8t8xny.streamlit.app/

---

## Features

### Real-Time AQI Monitoring
- Fetches live AQI data for Indian cities
- Tracks major pollutants:
  - PM2.5
  - PM10
  - NO₂
  - SO₂
  - CO
  - O₃
- Displays AQI categories with health impact indicators
- Provides pollutant-wise analysis and recommendations

### AQI Forecasting using Machine Learning
- Predicts AQI trends using Polynomial Regression
- Supports forecasting for configurable periods
- Uses historical pollutant data for training
- Generates prediction confidence ranges

### Multi-City Comparative Analysis
- Compare AQI across multiple cities
- Rank cities based on pollution levels
- Interactive visualizations using Plotly
- Comparative pollutant trend analysis

### Interactive Dashboard
- Dynamic charts and graphs
- User-friendly interface with Streamlit
- Real-time data refresh functionality
- Visual representation of environmental trends

---

## Tech Stack

**Frontend**
- Streamlit

**Programming Language**
- Python

**Libraries**
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib

**API Integration**
- OpenWeatherMap Air Pollution API

---

## Machine Learning Implementation

The forecasting module uses Polynomial Regression to identify AQI trends based on historical air quality data.

### Workflow:
1. Collect historical AQI and pollutant values
2. Perform preprocessing and feature extraction
3. Train Polynomial Regression model
4. Generate future AQI predictions
5. Display results with visual trend analysis

---

## Project Structure

```bash
AQI-Analysis/
│
├── app.py
├── .env
├── .env.example
├── scripts/
│   └── requirements.txt
│
└── README.md
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/aqi-analysis.git
cd aqi-analysis
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r scripts/requirements.txt
```

### Configure API Key

Create a `.env` file and add:

```env
OPENWEATHER_API_KEY=your_api_key
```

### Run Application

```bash
streamlit run app.py
```

Application will launch on:

```bash
http://localhost:8501
```

---

## AQI Categories

| AQI Range | Category |
|------------|-----------|
| 0–50 | Good |
| 51–100 | Moderate |
| 101–150 | Unhealthy for Sensitive Groups |
| 151–200 | Unhealthy |
| 201–300 | Very Unhealthy |
| 301+ | Hazardous |

---

## Future Improvements

- Deep learning-based AQI prediction models
- Geographic heatmap visualization
- Health recommendation system
- Mobile application integration
- Weather parameter correlation analysis

---

## Applications

- Environmental monitoring
- Pollution trend analysis
- Public health awareness
- Smart city initiatives
- Research and data analysis

---

## Acknowledgements

- OpenWeatherMap API
- Streamlit
- Python open-source ecosystem

---

## License

This project is developed for educational and research purposes.