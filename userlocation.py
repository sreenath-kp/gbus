import requests
import app
from key import api_key
def get_current_location(api_key):
    try:
            geolocation_url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'
            geolocation_data = {
                "considerIp": "true",
            }

            geolocation_response = requests.post(geolocation_url, json=geolocation_data)
            if geolocation_response.status_code == 200:
                location = geolocation_response.json()['location']
                latitude = location['lat']
                longitude = location['lng']
                return latitude, longitude
            else:
                print("Failed to get location")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None, None

if __name__ == "__main__":

    latitude, longitude = get_current_location(api_key)
    if latitude and longitude:
        print(f"User's current location: Latitude: {latitude}, Longitude: {longitude}")
        # destination = app.destination
        # print(destination)
    else:
        print("Failed to get the user's current location.")
