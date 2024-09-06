# weather_processing.py

from src.commonconst import *
from src.data_processing import fetch_weather_data
from src.llama3 import run_llama3, generate_outfit_prompt

# Function to fetch weather data, generate outfit suggestions, and save to CSV
def generate_weather_and_outfit_data(city):
    weather_df = fetch_weather_data(city)
    
    outfit_suggestions = []
    for _, weather_info in weather_df.iterrows():
        prompt = generate_outfit_prompt(weather_info)
        outfit_suggestion = run_llama3(prompt)
        outfit_suggestions.append(outfit_suggestion)

    weather_df['Outfit_Suggestion'] = outfit_suggestions

    weather_df.to_csv(CSV_FILE, index=False)
    
    return weather_df