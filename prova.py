import streamlit as st
import json, requests 

# add your own APIkey
APIkey = 'b0dc5ff479faf43dff849169f51ad2b0'
location = 'Bolzano'

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

st.text("current max temperature in Bolzano: ",weatherData['main']['temp_max'])
# more???????????
