from uagents import Agent, Context
from api.weather_api import fetch_weather_data
import json
import os
import signal
import sys
from dotenv import load_dotenv
from plyer import notification
from infi.systray import SysTrayIcon

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
city = USER_DATA.get("location")or "Kolkata"
frequency = USER_DATA.get("frequency") or "intermediate"

#Setting time interval for agent call
TIME_PERIOD = 60
if frequency == "fast":
    TIME_PERIOD *= 20
elif frequency == "intermediate":
    TIME_PERIOD *= 60
elif frequency == "slow":
    TIME_PERIOD *= 120

#creating the agent
alertAgent = Agent(name=os.getenv("AGENT_NAME"), seed=os.getenv("AGENT_SEED"))

# defining functions to fetch weather data
def fetchWeather():
    temp, des = fetch_weather_data(api_key, city)
    # printing the data
    if temp is not None and des is not None:
        return temp, des
    else:
        return None

# defining the agent function
@alertAgent.on_interval(period=TIME_PERIOD)
async def alertAgentFunc(ctx: Context):
    if fetchWeather():
        temp, des = fetchWeather()
        if USER_DATA:
            if temp < float(USER_DATA['min_temp']):
                # show notification
                notification.notify(
                    app_icon =os.getcwd()+"\\app\\logo.ico",
                    title="It is getting cold 🥶",
                    message=f"The current temperature is {int(temp - float(USER_DATA['min_temp']))} °C less than your set temperature.",
                    timeout=10

                )

            elif temp > float(USER_DATA['max_temp']):
                notification.notify(
                    app_icon =os.getcwd()+"\\app\\logo.ico",
                    title="It is getting hot 🥵",
                    message=f"The current temperature is {int(temp - float(USER_DATA['max_temp']))} °C more than your set temperature.",
                    timeout=10

                )




def on_quit_callback(systray):
    os.kill(os.getpid(), signal.SIGTERM)
    sys.exit()


systray = SysTrayIcon(os.getcwd()+"\\app\\logo.ico", "Temperature Alert Agent",
                      on_quit=on_quit_callback)

if __name__ == "__main__":
    systray.start()
    alertAgent.run()

