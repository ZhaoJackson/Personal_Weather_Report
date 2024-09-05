import requests
import pandas as pd
import plotly.express as px
import subprocess
import streamlit as st
import os

# API details
API_KEY = "aada7722255a438cbc6203101243108"
BASE_FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"
CSV_FILE = "weather_forecast.csv"

# Function to fetch weather data
def fetch_weather_data(city, days=14):
    url = f"{BASE_FORECAST_URL}?key={API_KEY}&q={city}&days={days}"
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

# Function to run the Llama3 model via Ollama CLI for outfit suggestions
def run_llama3(prompt):
    result = subprocess.run(['ollama', 'run', 'llama3'], input=prompt.encode(), stdout=subprocess.PIPE)
    return result.stdout.decode()

# Function to generate the prompt for the Llama3 model
def generate_outfit_prompt(weather_info):
    prompt = f"""
    1st. The weather forecast for {weather_info['Date']} shows a temperature of {weather_info['Temperature']}°C with {weather_info['Description']}.
    
    2nd. Based on this weather, please suggest an outfit.

    3rd. Is there a chance of rain? The rain probability is {weather_info['Rain_Probability']}%. Should I bring an umbrella or a raincoat?
    """
    return prompt

# Function to fetch weather data, generate outfit suggestions, and save to CSV
def generate_weather_and_outfit_data(city):
    # Fetch weather data
    weather_df = fetch_weather_data(city)
    
    # Generate outfit suggestions using Llama3 and add them to the dataframe
    outfit_suggestions = []
    for _, weather_info in weather_df.iterrows():
        prompt = generate_outfit_prompt(weather_info)
        outfit_suggestion = run_llama3(prompt)
        outfit_suggestions.append(outfit_suggestion)
    
    # Add outfit suggestions to the dataframe
    weather_df['Outfit_Suggestion'] = outfit_suggestions
    
    # Save the dataframe to a CSV file
    weather_df.to_csv(CSV_FILE, index=False)
    
    return weather_df

# Function to ensure CSV file is updated when changing city
def update_weather_data_for_city(city):
    st.write(f"Generating new data for {city}...")
    weather_df = generate_weather_and_outfit_data(city)
    return weather_df

# Function to create a Streamlit dashboard using Plotly for interactivity
def create_dashboard(df, city):
    st.title(f"14-Day Weather Forecast for {city}")
    
    # Plotly bar graph for temperature
    fig = px.bar(df, x='Date', y='Temperature', title=f'Temperature Over the Next 14 Days for {city}')
    
    # Display the plotly figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Let the user select a date via a selectbox
    selected_date = st.selectbox("Select a Date to Get Outfit Suggestions", df['Date'])
    
    # Fetch the weather info for the selected date from the already generated CSV
    weather_info = df[df['Date'] == selected_date].iloc[0]
    
    # Display the outfit suggestion for the selected date
    st.subheader(f"Outfit Suggestion for {selected_date}")
    if 'Outfit_Suggestion' in weather_info:
        st.write(weather_info['Outfit_Suggestion'])
    else:
        st.error(f"Outfit Suggestion for {selected_date} not found.")

# Main Streamlit app logic
def main():
    st.sidebar.title("Weather Forecast Dashboard")
    city = st.sidebar.text_input("Enter the city name", "New York")
    
    if st.sidebar.button("Get Weather Forecast"):
        # Update the CSV file and dashboard when the city changes
        weather_df = update_weather_data_for_city(city)
        
        # Display the updated dashboard with the new data
        create_dashboard(weather_df, city)

    # Load the existing CSV file to handle date changes without refreshing the city data
    elif os.path.exists(CSV_FILE):
        weather_df = pd.read_csv(CSV_FILE)
        # Display the dashboard based on the existing CSV file when the user selects a new date
        create_dashboard(weather_df, city)

if __name__ == "__main__":
    main()