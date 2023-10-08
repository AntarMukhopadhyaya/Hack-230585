from uagents import Agent, Context
from plyer import notification
from api.weather_api import fetch_weather_data
import os
import json
from dotenv import load_dotenv

# loading the env variables
load_dotenv()

# defining the api key and city
USER_DATA = {}
# if file exists then open it and load the data
if os.path.isfile("user-data.json"):
    with open("user-data.json") as f:
        USER_DATA = json.load(f)

# setting up the api key and city
api_key = os.getenv("API_KEY")
city = USER_DATA['location'] or "Kolkata"
# country_code = 'IN'  # Country code (optional)
frequency = USER_DATA['frequency'] or "intermediate"

# creating the agent
alertAgent = Agent(name="alertAgent", seed="alertAgentReovery")

# defining functions to fetch weather data
def fetchWeather():
    temp, des = fetch_weather_data(api_key, city)
    # printing the data
    if temp is not None and des is not None:
        return temp, des
    else:
        return None


if __name__ == "__main__":
    alertAgent.run()