import requests
import googlemaps
from api_keys import *



def run():
   x = True

   while True:
       travel_guide()

def weather(country, city):
    weather_api_key = weather_API_KEY
    if (country == '1') and (city == '1'):
        weather_data = requests.get("http://api.wunderground.com/api/2ddcf526ba46b259/conditions/q/Kenya/Nairobi.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '1') and (city == '2'):
        weather_data = requests.get("http://api.wunderground.com/api/2ddcf526ba46b259/conditions/q/Kenya/Kisumu.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '2') and (city == '1'):
        weather_data = requests.get("http://api.wunderground.com/api/weather_api_key/conditions/q/Uganda/Kampala.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '2') and (city == '2'):
        weather_data = requests.get("http://api.wunderground.com/api/weather_api_key/conditions/q/Uganda/Entebbe.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    else:
        print('Invalid input')

def geometry(input_value):
    google_api_key = google_API_KEY
    gm = googlemaps.Client(key=google_API_KEY)
    geocode_result = gm.geocode(input_value)[0]
    latitude = geocode_result['geometry']['location']['lat']
    longitude = geocode_result['geometry']['location']['lng']
    print("Latitude:" + str(latitude), "Longitude:" + str(longitude))

def travel_guide():
    country_input = input('\n\t\tTRAVEL EAST AFRICA\n\t\t\tWELCOME\n\tPlease select a country:\n\t1. Kenya\n\t2. Uganda\n')
    if country_input == '1':
        city_input = input('\tPlease select city\n\t1. Nairobi\n\t2. Kisumu\n')
        if city_input == '1':
            city = 'nairobi'
            geometry(city)
            weather(country_input, city_input)
        elif city_input == '2':
            city = 'kisumu'
            geometry(city)
            weather(country_input, city_input)
        else:
            print('Invalid input')
    elif country_input == '2':
        city_input = input('\tPlease select city\n\t1. Kampala\n\t2. Entebbe\n')
        if city_input == '1':
            city = 'kampala'
            geometry(city)
        elif city_input == '2':
            city = 'entebbe'
            geometry(city)
            weather(country_input, city_input)
        else:
            print('Invalid input')
    else:
        print('Invalid input')


run()
