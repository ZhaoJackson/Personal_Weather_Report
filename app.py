# app.py

from src.commonconst import *
from src.streamlit import update_weather_data_for_city, create_dashboard

# Main Streamlit app logic
def main():
    st.sidebar.title("Weather Forecast Dashboard")
    city = st.sidebar.text_input("Enter the city name", "New York")
    
    if st.sidebar.button("Get Weather Forecast"):
        # Update the CSV file and dashboard when the city changes
        weather_df = update_weather_data_for_city(city)
        create_dashboard(weather_df, city)

    elif os.path.exists(CSV_FILE):
        # Load the existing CSV file to handle date changes without refreshing the city data
        weather_df = pd.read_csv(CSV_FILE)
        create_dashboard(weather_df, city)

if __name__ == "__main__":
    main()