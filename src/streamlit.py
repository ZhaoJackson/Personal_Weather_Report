# streamlit.py
from src.commonconst import *
from src.weather_processing import generate_weather_and_outfit_data

# Function to ensure CSV file is updated when changing city
def update_weather_data_for_city(city):
    st.write(f"Generating new data for {city}...")
    weather_df = generate_weather_and_outfit_data(city)
    return weather_df

# Function to create a Streamlit dashboard using Plotly for interactivity
def create_dashboard(df, city):
    st.title(f"14-Day Weather Forecast for {city}")
    fig = px.bar(df, x='Date', y='Temperature', title=f'Temperature Over the Next 14 Days for {city}')
    st.plotly_chart(fig, use_container_width=True)
    selected_date = st.selectbox("Select a Date to Get Outfit Suggestions", df['Date'])
    weather_info = df[df['Date'] == selected_date].iloc[0]

    st.subheader(f"Outfit Suggestion for {selected_date}")
    if 'Outfit_Suggestion' in weather_info:
        st.write(weather_info['Outfit_Suggestion'])
    else:
        st.error(f"Outfit Suggestion for {selected_date} not found.")