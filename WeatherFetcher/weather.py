
import requests
import json
import os
import argparse
from dotenv import load_dotenv
from utils.logger import log_weather

# Loading API from Environment
load_dotenv()
API_KEY = os.getenv("API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code != 200:
        raise Exception(response.json().get("message", "API request failed"))
    
    data = response.json()
    weather = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    return weather, temperature_celsius

def main():
    parser = argparse.ArgumentParser(description="Weather CLI")
    parser.add_argument("--city", type=str ,required= True, help="city that needs weather info")
    args = parser.parse_args()
    city = args.city
    
    try: 
        weather, temperature = fetch_weather(city)
        log_weather(city, weather, temperature)
        
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature:.2f}°C")
    
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()