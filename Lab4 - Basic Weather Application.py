import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=36.3134&longitude=-82.3535&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m"

response = requests.get(url)

data = response.json()

print(data["current"])
