# Weather App 🌦️

A sleek and user-friendly web application to display current weather conditions, air quality, forecasts, and more. This app dynamically updates based on user input and provides weather insights for today, tomorrow, and the day after.

---

## 🚀 Features

- **Current Weather**: Displays temperature, weather condition, and location details.
- **Forecast**: Provides a three-day weather forecast.
- **Air Quality**: Real-time AQI information.
- **UV Index**: Categorized as Weak, Normal, High, Very High, or Extreme.
- **Real Feel**: Shows perceived temperature.
- **Additional Details**:
  - Humidity
  - Wind Speed and Direction
  - Pressure
  - Sunset Time
- **Dynamic Day Labels**: Updates "Day After Tomorrow" automatically.
- **User Location Support**: Fetches weather data based on geolocation.

---

## 🛠️ Tech Stack

- **HTML/CSS/JavaScript**: Frontend development.
- **Python (Flask)**: Backend server to handle dynamic rendering and API calls.
- **Weather API Integration**: Fetches real-time weather data using [Weather Api Providers](https://www.weatherapi.com/) .
- **Jinja2**: Template rendering for server-side HTML generation.

---

## 📦 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/nakul-verma2/weather-app-flask
    ```
    ```bash
    cd weather-app-flask
    ```
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your Weather API key:
    Obtain an API key from your preferred weather API provider [WeatherAPI](https://www.weatherapi.com/).
    Add the API key to your app.py file.
    ```python
    API_KEY = "<YOUR-API-KEY"
    ```
4. Run the application:
    ```bash
    python3 app.py
    ```
5. Open the app in your browser:
    ```bash
    http://127.0.0.1:5000
    ````
    
## 🌐 Usage
- Enter the city name (e.g., London) or use the Use My Location button to fetch weather details.
- View detailed weather forecasts and other statistics in the organized dashboard.
  
## 🌐 App Live On Using [Render](https://render.com/)

**Experience the live app:**
[Weather App Live](https://weather-app-jqak.onrender.com/)  

## 📸 Screenshots
![Screenshot 2024-12-15 at 12 04 26 PM](https://github.com/user-attachments/assets/af39ed65-c477-4c82-8a87-785acb511a7f)
![Screenshot 2024-12-15 at 12 05 12 PM](https://github.com/user-attachments/assets/9af22426-07a1-4967-b6e6-2fa1714ea39b)



## 🎉 Contributing
Feel free to open issues or submit pull requests to enhance the functionality of the App.

## 📜 License
This project is licensed under the MIT [License](https://github.com/nakul-verma2/weather-app-flask/blob/main/LICENSE).
