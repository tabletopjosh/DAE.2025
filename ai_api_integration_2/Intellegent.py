import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_coordinates(address):
    """Fetches latitude and longitude from Google Maps Geocoding API."""
    try:
        google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")  # Secure API key retrieval
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise ValueError(f"Error from Google API: {data['status']}")
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {e}"
    except ValueError as ve:
        return f"Data Error: {ve}"

def get_weather(lat, lon):
    """Fetches weather data using OpenWeather API based on coordinates."""
    try:
        openweather_api_key = os.getenv("OPENWEATHER_API_KEY")  # Secure API key retrieval
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "city": data["name"]
        }
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {e}"

def main():
    address = input("Enter a location: ")
    
    # Fetch coordinates from Google Maps API
    coordinates = get_coordinates(address)
    if isinstance(coordinates, str):
        print(coordinates)
        return
    
    lat, lon = coordinates
    
    # Fetch weather data using OpenWeather API
    weather_data = get_weather(lat, lon)
    if isinstance(weather_data, str):
        print(weather_data)
        return
    
    print(f"Weather in {weather_data['city']}: {weather_data['weather']}, {weather_data['temperature']}°C")

if __name__ == "__main__":
    main()
