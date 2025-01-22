import requests

def get_weather(city, api_key):
    """Fetch weather data for a city using OpenWeatherMap API."""
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch weather data", "status_code": response.status_code}

def get_news(api_key):
    """Fetch top headlines using News API."""
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(news_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch news data", "status_code": response.status_code}

def format_weather_data(weather_data):
    """Format weather data for display."""
    if "error" in weather_data:
        return weather_data["error"]

    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    return f"Weather in {city}: {temp}°C, {description.capitalize()}"

def format_news_data(news_data):
    """Format news headlines for display."""
    if "error" in news_data:
        return news_data["error"]

    articles = news_data.get("articles", [])
    formatted_news = "\n".join([f"- {article['title']}" for article in articles[:5]])
    return f"Top News Headlines:\n{formatted_news}"

def main():
    # API keys
    weather_api_key = "5e8fb2c80fe69508b23b1a4596ac4816"
    news_api_key = "6a5df9f4d9ba47ddaf704b9e714045bc"

    # Fetch and display weather data
    city = input("Enter a city for weather information: ")
    weather_data = get_weather(city, weather_api_key)
    print(format_weather_data(weather_data))

    # Fetch and display news data
    news_data = get_news(news_api_key)
    print(format_news_data(news_data))

if __name__ == "__main__":
    main()
