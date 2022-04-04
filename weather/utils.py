from datetime import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_data(city_name):

    BASE_URL = os.environ.get('BASE_URL')
    API_KEY = os.environ.get('API_KEY')
    URL = f"{BASE_URL}q={city_name}&appid={API_KEY}"

    city_weather = requests.get(URL).json()

    data = {
        'temperature': round((city_weather['main']['temp']) - 273.15, 1),
        'feels_like': round(city_weather['main']['feels_like'] - 273.15, 1),
        'description': city_weather['weather'][0]['description'],
        'humidity': city_weather['main']['humidity'],
        'pressure': city_weather['main']['pressure'],
        'country': city_weather['sys']['country'],
        'sunrise': datetime.utcfromtimestamp(city_weather['sys']['sunrise']),
        'sunset': datetime.utcfromtimestamp(city_weather['sys']['sunset']),
        'name': city_weather['name'],
        'windspeed': city_weather['wind']['speed']
    }

    return data
