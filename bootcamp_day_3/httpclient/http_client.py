import requests
import googlemaps


def run():
   x = True

   while True:
       travel_guide()

def weather(country, city):
    if (country == '1') and (city == '1'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Kenya/Nairobi.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '1') and (city == '2'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Kenya/Kisumu.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '2') and (city == '1'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Uganda/Kampala.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '2') and (city == '2'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Uganda/Entebbe.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '3') and (city == '1'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Tanzania/Dodoma.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    elif (country == '3') and (city == '2'):
        weather_data = requests.get("http://api.wunderground.com/api/b9f730afe2b552a5/conditions/q/Tanzania/Arusha.json")
        temp = weather_data.json()['current_observation']['temp_c']
        humidity = weather_data.json()['current_observation']['relative_humidity']
        local_time = weather_data.json()['current_observation']['local_time_rfc822']
        print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    else:
        print('Invalid input')

def geometry(input_value):
    gm = googlemaps.Client(key='AIzaSyDMngKtxnUgPQAwD80_e0IsvHAnx-6Xuw8')
    geocode_result = gm.geocode(input_value)[0]
    latitude = geocode_result['geometry']['location']['lat']
    longitude = geocode_result['geometry']['location']['lng']
    print("Latitude:" + str(latitude), "Longitude" + str(longitude))

def currency(input_value):
    curr_data = requests.get('https://openexchangerates.org/api/latest.json?app_id=a3db7dbfca7744ca93488b91fdd84eba')
    if input_value == '1':
        converted_currency = curr_data.json()['rates']['KES']
        print("1 USD = " + str(converted_currency))
    elif input_value == '2':
        converted_currency = curr_data.json()['rates']['UGX']
        print("1 USD = " + str(converted_currency))
    else:
        converted_currency = curr_data.json()['rates']['TZS']
        print("1 USD = " + str(converted_currency))

def travel_guide():
    country_input = input('\n\t\tTRAVEL EAST AFRICA\n\t\t\tWELCOME\n\tPlease select a country:\n\t1. Kenya\n\t2. Uganda\n\t3. Tanzania\n\t')
    if country_input == '1':
        city_input = input('\tPlease select city\n\t1. Nairobi\n\t2. Kisumu\n')
        if city_input == '1':
            city = 'nairobi'
            geometry(city)
            weather(country_input, city_input)
            currency(country_input)
        elif city_input == '2':
            city = 'kisumu'
            geometry(city)
            currency(country_input)
            weather(country_input, city_input)
        else:
            print('Invalid input')
    elif country_input == '2':
        city_input = input('\tPlease select city\n\t1. Kampala\n\t2. Entebbe\n')
        if city_input == '1':
            city = 'kampala'
            geometry(city)
            currency(country_input)
        elif city_input == '2':
            city = 'entebbe'
            geometry(city)
            currency(country_input)
            weather(country_input, city_input)
        else:
            print('Invalid input')
    elif country_input == '3':
        city_input = input('\tPlease select city\n\t1. Dodoma\n\t2. Arusha\n')
        if city_input == '1':
            city = 'dodoma'
            geometry(city)
            currency(country_input)
            weather(country_input, city_input)
        elif city_input == '2':
            city = 'arusha'
            geometry(city)
            currency(country_input)
            weather(country_input, city_input)
        else:
            print('Invalid input')
    else:
        print('Invalid input')


run()
