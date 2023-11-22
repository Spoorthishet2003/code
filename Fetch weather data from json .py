###Python Program to fetch current weather data from the JSON file

import json

with open('weather_data.json') as f: //# Load the JSON data from file
    data = json.load(f)

current_temp = data['main']['temp']  //# Extract the required weather data
humidity = data['main']['humidity']
weather_desc = data['weather'][0]['description']

print(f"Current temperature: {current_temp}°C") //# Display the weather data
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")

###JSON FILE

{
  "coord": {
    "lon": -73.99,
    "lat": 40.73
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 15.45,
    "feels_like": 12.74,
    "temp_min": 14.44,
    "temp_max": 16.11,
    "pressure": 1017,
    "humidity": 64
  },
  "visibility": 10000,
  "wind": {
    "speed": 4.63,
    "deg": 180
  },
  "clouds": {
    "all": 1
  },
  "dt": 1617979985,
  "sys": {
    "type": 1,
    "id": 5141,
    "country": "US",
    "sunrise": 1617951158,
    "sunset": 1618000213
  },
  "timezone": -14400,
  "id": 5128581,
  "name": "New York",
  "cod": 200
}
