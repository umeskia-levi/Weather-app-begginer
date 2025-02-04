import requests
from pprint import pprint

API_KEY = '701b74a40aaa9be6d6d3e0129cbbd54b'

city = input("Enter a City: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+ API_KEY +"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

