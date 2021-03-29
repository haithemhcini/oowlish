import json
import requests
import pandas as pd
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    # Google Maps Api Key
    API_KEY = "hX5vsvK8K93ze6FADh1s4dCUuvRFKvnk"

    # Import CSV + Data Processing (Replace NaN Values with Zeros)
    df = pd.read_csv("customers.csv").fillna(0)
    pd.set_option('display.max_rows', None)

    for i, row in df.iterrows():
        # Customer Address
        Address = str(df.at[i, 'city'])

        # Geocoding API request parameters
        parameters = {
            "key": API_KEY,
            "location": Address
        }

        # Geocoding responses
        response = requests.get(
            "http://www.mapquestapi.com/geocoding/v1/address", params=parameters)

        # When the geocoder returns results, it places them within a (JSON)
        data = response.text
        dataJ = json.loads(data)['results']

        # Extracting lat/lon from geocode result
        lat = (dataJ[0]['locations'][0]['latLng']['lat'])
        lng = (dataJ[0]['locations'][0]['latLng']['lng'])

        df.at[i, 'lat'] = lat
        df.at[i, 'lng'] = lng

        # Load data into a new .csv file
        df.to_csv('customers_geo.csv')

    def handle(self, *args, **options):
        print(' Google Maps API Successful response')
