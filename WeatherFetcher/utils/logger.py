import csv
import os
from datetime import datetime

LOG_FILE = "weather_logs.csv"

def log_weather(city, weather, temp):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "city", "weather", "temperature_c"])

        writer.writerow([datetime.now(), city, weather, temp])
