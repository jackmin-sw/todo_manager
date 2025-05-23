import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
        return "Failed to fetch weather data"