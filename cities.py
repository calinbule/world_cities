from geopy.geocoders import Nominatim
import pandas as pd

nominatim_file = 'cities_nominatim.csv'
df_cities = pd.read_csv(nominatim_file, sep=',', encoding='utf-8')
geolocator = Nominatim(user_agent="application", timeout=10)

while len(df_cities[df_cities['nominatim_location'] == '*']) != 0:

    for i in range(df_cities.shape[0]):

        if df_cities.loc[i, 'nominatim_location'] == '*':

            city_name = df_cities.loc[i, 'city_name']
            location = geolocator.geocode(city_name, language="en")
            
            if location is not None:
                df_cities.loc[i, 'nominatim_location'] = str(list(location)[0])
                df_cities.loc[i, 'nominatim_coordinates'] = str(list(location)[1])
            else: 
                df_cities.loc[i, 'nominatim_location'] = 'no result'
                df_cities.loc[i, 'nominatim_coordinates'] = 'no result'

            df_cities.to_csv(nominatim_file, sep=',', encoding='utf-8')

            done = df_cities.shape[0] - len(df_cities[df_cities['nominatim_location'] == '*'])
            
            print(f'{done} of {df_cities.shape[0]} records done')



print(f'{done} of {df_cities.shape[0]} records done')
