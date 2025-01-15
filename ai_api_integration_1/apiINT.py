import requests
from flask import Flask, render_template, request

# FLASK APPLICATION SETUP
app = Flask(__name__)

# API KEYS AND BASE URLS
WEATHER_API_KEY = "your_openweathermap_api_key"  # REPLACE WITH YOUR WEATHER API KEY
MAPS_API_KEY = "your_google_maps_api_key"  # REPLACE WITH YOUR GOOGLE MAPS API KEY
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
MAPS_API_URL = "https://maps.googleapis.com/maps/api/staticmap"

# ROUTE FOR HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    map_url = None

    if request.method == 'POST':
        city = request.form.get('city')

        # RESTFUL API METHOD UTILIZATION - GET REQUEST TO WEATHER API
        weather_response = requests.get(WEATHER_API_URL, params={
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        })

        if weather_response.status_code == 200:
            # STRUCTURING API REQUESTS AND RESPONSES - PARSE WEATHER RESPONSE
            weather_data = weather_response.json()

            # FORMAT AND DISPLAY API DATA
            map_url = f"{MAPS_API_URL}?center={city}&zoom=12&size=600x300&key={MAPS_API_KEY}"  # MAP URL FORMATTING

    return render_template('index.html', weather=weather_data, map_url=map_url)

if __name__ == '__main__':
    app.run(debug=True)