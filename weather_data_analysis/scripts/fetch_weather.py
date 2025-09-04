import requests
import json
from datetime import datetime
from config import API_KEY, CITIES
import os

RAW_DIR = "data/raw/"
os.makedirs(RAW_DIR, exist_ok=True)

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def save_raw_data(city, data):
    filename = f"{RAW_DIR}{city}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    for city in CITIES:
        data = fetch_weather(city)
        save_raw_data(city, data)
        print(f"✅ Saved weather data for {city}")
