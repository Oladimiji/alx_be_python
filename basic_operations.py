# weather.py

import requests

API_KEY = "c724279f3c2949d1907173440250806"
CITY = "London"  # You can change this to any city you'd like
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

try:
    response = requests.get(URL)
    response.raise_for_status()  # Check for HTTP request errors
    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    feelslike_c = data["current"]["feelslike_c"]

    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Feels Like: {feelslike_c}°C")
    print(f"Condition: {condition}")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)
except KeyError:
    print("Error parsing weather data. Please check the city name or API key.")