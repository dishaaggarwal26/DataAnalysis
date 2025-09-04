import pandas as pd
import mysql.connector
from config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
query = "SELECT * FROM weather_data"
df = pd.read_sql(query, conn)
conn.close()

df.to_csv("data/processed/weather_export_from_db.csv", index=False)
print("✅ Data exported from MySQL to CSV")
