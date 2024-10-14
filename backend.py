from geopy import geocoders
import requests
import json
import datetime

def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def weather_api(latitude:str, longitude:str):
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}"
    headers = {"X-Yandex-Weather-Key": "7180f170-c802-4e1d-8e9d-446baa5d753f"}
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"Ошибка при подключении к API: {response}"

def start(city:str):
    latitude,longitude = geo_pos(city)
    weather = json.loads(weather_api(latitude,longitude))
    out=''
    now = datetime.datetime.now().hour
    for hour in weather['forecasts'][0]['hours']:
        if int(hour['hour']) >= now:
            out += f"Температура на {hour['hour']}:00: {hour['feels_like']}°\nВлажность:{hour['humidity']}%\nПогодные условия: {hour['condition']}\n\n"
    return out