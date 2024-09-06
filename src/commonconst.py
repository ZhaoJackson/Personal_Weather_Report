# commonconst.py

# Import necessary libraries
import os
import pandas as pd
import requests
import subprocess
import plotly.express as px
import streamlit as st

# Constants
API_KEY = "aada7722255a438cbc6203101243108"
BASE_FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"
CSV_FILE = os.path.join("src", "forecast", "weather_forecast.csv")

# Shared functions
def get_api_url(city, days=14):
    return f"{BASE_FORECAST_URL}?key={API_KEY}&q={city}&days={days}"
def read_csv():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame()