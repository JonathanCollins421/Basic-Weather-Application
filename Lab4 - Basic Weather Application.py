import requests

print("Welcome to Jonathan's simple weather application! To use the app you'll need to enter the lat and lon of your local area!")

lat = input("lat: ")
lon = input("long: ")
units = input("The default units are imperial do you want to change to metric? (y for yes):")
temp_unit_symbol = "°F"
speed_unit_symbol = "mph"
temp_unit_request = "fahrenheit"
speed_unit_request = "mph"

if units == "y":
     temp_unit_symbol = "°c"
     speed_unit_symbol = "km/h"
     temp_unit_request = "celsius"
     speed_unit_request = "kmh"


url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code&temperature_unit={temp_unit_request}&wind_speed_unit={speed_unit_request}"

response = requests.get(url)

data = response.json()

def get_conditions(code: int):
    match code:
       case 0:
            return "Clear sky"
       case 1:
            return "Mainly clear"
       case 2:
            return "Partly cloudy"
       case 3:
            return "Overcast"
       case 45 | 48:
            return "Foggy"
       case 51 | 53 | 55:
            return "Drizzle"
       case 61:
            return "Light rain"
       case 63:
            return "Moderate rain"
       case 65:
            return "Heavy rain"
       case 71:
            return "Light snow"
       case 73:
            return "Moderate snow"
       case 75:
            return "Heavy snow"
       case 80 | 81 | 82:
            return "Rain showers"
       case 85 | 86:
            return "Snow showers"
       case 95 | 96 | 99:
            return "Thunderstorm"
       case _:
            return "Unknown conditions"

conditions = get_conditions(data["current"]["weather_code"])

print(f"\nYour local weather!")
print("-------------------")
print(f"Current temperature: {data["current"]["temperature_2m"]}{temp_unit_symbol}")
print(f"Feels Like: {data["current"]["apparent_temperature"]}{temp_unit_symbol}")
print(f"Humidity: {data["current"]["relative_humidity_2m"]}%")
print(f"Wind Speed: {data["current"]["wind_speed_10m"]} {speed_unit_symbol}")
print(f"Conditions: {conditions}")










