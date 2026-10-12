import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=36.3134&longitude=-82.3535&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code"

response = requests.get(url)

data = response.json()

print("Your local weather!")
print("-------------------")
print(f"Current temperature: {data["current"]["temperature_2m"]}")
print(f"Feels Like: {data["current"]["apparent_temperature"]}")
print(f"Humidity: {data["current"]["relative_humidity_2m"]}")
print(f"Wind Speed: {data["current"]["wind_speed_10m"]}")
print(f"Code: {data["current"]["weather_code"]}")

