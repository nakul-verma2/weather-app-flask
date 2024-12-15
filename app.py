from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "YOUR-API-KEY"

@app.route("/")
def home():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    weather_data = None

    if city:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=yes"
    elif lat and lon:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days=3&aqi=yes"
    else:
        url = None

    if url:
        print(f"Fetching weather data from: {url}")
        response = requests.get(url)
        print(f"API Response: {response.status_code}, {response.text}")  # Debug response
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "Unable to fetch weather data."}

    return render_template("index.html", weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
