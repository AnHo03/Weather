import requests
from dotenv import load_dotenv
import os
from pprint import pprint
import time

load_dotenv()

def get_current_weather():
    print('\n*** Current Weather Condition in ***')

    city = input("\n Insert name of your city>")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f'\n\n***Current weather for {weather_data["name"]}***')
    print(f'\nTemperature: {weather_data["main"]["temp"]} degrees fahrenheit')
    print(f'Fells like: {weather_data["main"]["feels_like"]} degrees fahrenheit\nCloud cover: {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
    get_current_weather()

time.sleep(10)