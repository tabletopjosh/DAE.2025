import requests
import os
from dotenv import load_dotenv

def get_coordinates(address, google_maps_api_key):
    """Fetches latitude and longitude from Google Maps Geocoding API."""
    try:
        # API Integration: Using Google Maps API to get coordinates
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Error Handling: Raise exception for HTTP errors
        data = response.json()
        
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise ValueError(f"Error from Google API: {data['status']}")
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {e}"  # Error Handling: Network or API failure
    except ValueError as ve:
        return f"Data Error: {ve}"  # Error Handling: Invalid response format

def get_weather(lat, lon, openweather_api_key):
    """Fetches weather data using OpenWeather API based on coordinates."""
    try:
        # API Integration: Using OpenWeather API to fetch weather details
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
        return f"API Request Error: {e}"  # Error Handling: Network or API failure

def main():
    # Security: Avoid hardcoding API keys in production (Use environment variables instead)
    GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
    OPENWEATHER_API_KEY = "93fbb97f6679e811afedf68dd755b7e1"  # Replace with environment variable in production
    
    # User input for location
    address = input("Enter a location: ")
    
    # Integrating Multiple APIs: Fetch coordinates from Google Maps API
    coordinates = get_coordinates(address, GOOGLE_MAPS_API_KEY)
    if isinstance(coordinates, str):
        print(coordinates)  # Error Handling: Print error message if API call fails
        return
    
    lat, lon = coordinates
    
    # Integrating Multiple APIs: Fetch weather data using OpenWeather API
    weather_data = get_weather(lat, lon, OPENWEATHER_API_KEY)
    if isinstance(weather_data, str):
        print(weather_data)  # Error Handling: Print error message if API call fails
        return
    
    # Output results to the user
    print(f"Weather in {weather_data['city']}: {weather_data['weather']}, {weather_data['temperature']}°C")
    
if __name__ == "__main__":
    main()  # Testing & Troubleshooting: Runs the program to validate API responses