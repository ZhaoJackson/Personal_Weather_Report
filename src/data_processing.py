# data_processing.py

from src.commonconst import *

# Function to fetch weather data
def fetch_weather_data(city, days=14):
    url = get_api_url(city, days)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_data = data['forecast']['forecastday']
        weather_list = []
        for day in forecast_data:
            weather_info = {
                "Date": day['date'],
                "Temperature": day['day']['avgtemp_c'],
                "Description": day['day']['condition']['text'],
                "Rain_Probability": day['day']['daily_chance_of_rain']
            }
            weather_list.append(weather_info)
        return pd.DataFrame(weather_list)
    else:
        st.error("Error fetching data from Weather API")
        return pd.DataFrame()