import pandas as pd
import glob
import json
import os

RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def process_json(file):
    with open(file, "r") as f:
        data = json.load(f)
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "weather": data["weather"][0]["description"],
        "datetime": pd.to_datetime(data["dt"], unit="s")
    }

if __name__ == "__main__":
    files = glob.glob(RAW_DIR + "*.json")
    df = pd.DataFrame([process_json(file) for file in files])
    df.to_csv(PROCESSED_DIR + "weather_data_clean.csv", index=False)
    print(f"✅ Cleaned data saved to {PROCESSED_DIR}weather_data_clean.csv")
