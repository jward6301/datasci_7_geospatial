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


df2 = pd.read_csv("https://raw.githubusercontent.com/jward6301/datasci_7_geospatial/main/datasets/assignment7_slim_hospital_coordinates.csv")

df2['GEO'] = df2['X'].astype(str) + ',' + df2['Y'].astype(str)

df2_100 = df2.sample(100)


google_response = []

for coord in df2_100['GEO']: 

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = coord
    location_clean = urllib.parse.quote(location_raw)

    url_request = search + location_clean + '&key=' + api_key
    url_request

    response = requests.get(url_request)
    response_dictionary = response.json()

    address = response_dictionary['results'][0]['formatted_address']

    final = {'address': address, 'coordinates': coord}
    google_response.append(final)

    print(f'....finished with {coord}')


df2_new = pd.DataFrame(google_response)
df2_new.to_csv('reverse_geocoding.csv')