# llama3.py
from src.commonconst import *

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