import pandas as pd
import mysql.connector
from config import DB_CONFIG

df = pd.read_csv("data/processed/weather_data_clean.csv")

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    weather VARCHAR(50),
    datetime DATETIME
)
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO weather_data (city, temperature, humidity, wind_speed, weather, datetime)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))


conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted into MySQL database")
