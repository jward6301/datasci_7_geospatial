import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API")

df = pd.read_csv("https://raw.githubusercontent.com/jward6301/datasci_7_geospatial/main/datasets/assignment7_slim_hospital_addresses.csv")

df['GEO'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']

df_100 = df.sample(100)

google_response = []

for address in df_100['GEO']:  

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df_new = pd.DataFrame(google_response)
df_new.to_csv('geocoding.csv')
