# by me (not precise)

import requests

def geolocate():
    response = requests.get('https://api.ipify.org?format=json')

    if response.status_code == 200:
        data = response.json()
        ip_address = data.get('ip')

        response = requests.get(f"https://ipapi.co/{ip_address}/json/")

        if response.status_code == 200:
            data = response.json()
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            map_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

            print(f"Geolocation of host PC's IP address {ip_address}: {latitude}, {longitude}")
            print(f"View on Google Maps: {map_url}")
        else:
            print("Failed to geolocate host PC's IP address.")
    else:
        print("Failed to retrieve host PC's IP address.")

geolocate()
