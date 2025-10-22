# commonconst.py

# Import necessary libraries
import os
import re
from pathlib import Path
import pandas as pd
import requests
import subprocess
import plotly.express as px
import streamlit as st

# Constants
BASE_FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"


def _load_api_key() -> str:
    # 1) Environment variable
    env_key = os.getenv("WEATHER_API_KEY")
    if env_key:
        return env_key

    # 2) src/secrets.py (WEATHER_API_KEY or API_KEY)
    try:
        from . import secrets as _secrets  # type: ignore
        if getattr(_secrets, "WEATHER_API_KEY", None):
            return _secrets.WEATHER_API_KEY  # type: ignore
        if getattr(_secrets, "API_KEY", None):
            return _secrets.API_KEY  # type: ignore
    except Exception:
        pass

    # 3) .secrete file at repo root with a line like: API_KEY = "..."
    try:
        root_dir = Path(__file__).resolve().parent.parent
        secrete_path = root_dir / ".secrete"
        if secrete_path.exists():
            text = secrete_path.read_text()
            match = re.search(r'API_KEY\s*=\s*["\']([^"\']+)["\']', text)
            if match:
                return match.group(1)
    except Exception:
        pass

    return ""


API_KEY = _load_api_key()

# Paths resolved relative to this file so local runs work from any CWD
BASE_DIR = Path(__file__).resolve().parent
FORECAST_DIR = BASE_DIR / "forecast"
CSV_FILE = FORECAST_DIR / "weather_forecast.csv"

# Shared functions
def get_api_url(city, days=14):
    return f"{BASE_FORECAST_URL}?key={API_KEY}&q={city}&days={days}"
def read_csv():
    if CSV_FILE.exists():
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame()