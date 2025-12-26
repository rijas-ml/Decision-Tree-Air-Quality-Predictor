import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Temperature": 25,
    "Humidity": 70,
    "WindSpeed": 5,
    "NO2": 30,
    "PM25": 60
}

response = requests.post(url, json=data)
print(response.json())