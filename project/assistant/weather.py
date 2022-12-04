import datetime as dt 
import requests




def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit


def forecast():
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '325e7dde17b837c0af78e84101449c6b'
    CITY = "Hanoi"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    wind_speed = response["wind"]["speed"]
    humidity = response["main"]["humidity"]
    description = response["weather"][0]["description"]
    sunrise_time = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
    sunset_time = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])


    message = "Here is the Weather: Today will be mostly " + description \
                + ", with a temperature of  " + str(temp_celsius) + "°C" \
                + ", humidity of " + str(humidity) + " percent" \
                + " and a wind speed " + str(wind_speed) + " meters per second" \
                + ". Sunrise was at " + str(sunrise_time) + " local time." \
                + ", and Sunset at " + str(sunset_time) + " local time."
    # print(message) 
    return message
       
