import requests

def fetch_weather_data(api_key, city, country_code=''): 
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Construct the complete URL with parameters
    params = {
        'q': f"{city},{country_code}",
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        res = requests.get(url, params)
        data = res.json()

        if res.status_code == 200:
            # Extract relevant weather information
            temp = data['main']['temp']
            des = data['weather'][0]['description']
            return temp, des
        else:
            print(f"Error: Unable to fetch weather data. Status code: {res.status_code}")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None
