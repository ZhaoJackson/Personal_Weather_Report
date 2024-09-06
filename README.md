# 🌦️ Weather Forecast and Outfit Recommendation App
A Streamlit app that provides a 14-day weather forecast for a selected city and recommends outfits based on the weather conditions using the Llama3 model. The app retrieves weather data using an API, generates outfit suggestions using the Llama3 model, and displays an interactive dashboard.

# 🚀 Features
1. 🌦️ Fetches 14-day weather forecast for any city from 'Weatherapi.com'
2. 👗 Uses Llama3 to suggest outfits based on the weather forecast, including temperature, rain probability, and conditions.
3. 📊 Interactive dashboard where users can select a city and view detailed weather and outfit suggestions for each day.
4. 🗂️ CSV caching for weather and outfit data, so results are saved and reused for each session.

# 🏗️ Project Structure
```
weather-report-app/
|--- app.py                             # Main entry point for the Streamlit app
|--- LICENSE
|--- README.md
|--- requirements.txt                   # Python dependencies
|--- src/
|    |--- commonconst.py                # Contains all constants, API keys, and common imports
|    |--- data_processing.py            # Handles fetching and processing weather data
|    |--- llama3.py                     # Generates outfit suggestions using Llama3 model
|    |--- weather_processing.py         # Combines weather and outfit processing
|    |--- streamlit_app.py              # Streamlit app functions for dashboard creation
|    |--- forecast/
|        |--- weather_forecast.csv      # CSV file to store weather and outfit data
```

# 📝 Instructions
1. 🛠️ Clone the repository
```
$ git clone https://github.com/yourusername/weather-report-app.git
```
2. 📁 Navigate to the project directory
```
$ cd weather-report-app
```
3. 📦 Install the required dependencies
Ensure you have Python 3.9+ and pip installed on your machine. Then install the requirements:
```
$ pip install -r requirements.txt
```
4. 🏃 Run the app
```
$ streamlit run app.py
```
5. 🌐 Open the app in your browser by visiting http://localhost:8501/.

# 🎮 Usage
- 🏙️ Enter a city name in the sidebar to fetch a 14-day weather forecast.
- 👕 The app will generate outfit suggestions for each day based on the forecast, such as suggesting an umbrella or raincoat when rain is expected.
- 📊 The dashboard displays a bar chart of the temperatures for the next 14 days.
- 📅 Select any day from the dropdown to view the outfit suggestion for that specific date.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

# 🛠️ Technologies
- Python 3.8+
- Streamlit - Interactive web apps in Python
- Pandas - Data manipulation and analysis
- Requests - Fetching data from external APIs
- Plotly - Interactive plots and visualizations
- Subprocess - Running Llama3 CLI for outfit suggestions