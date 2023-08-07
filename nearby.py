import requests 
import googlemaps
# from userlocation import get_current_location
from key import api_key

gmap = googlemaps.Client(key=api_key)


def get_nearby_bus_stops(api_key, latitude, longitude, radius=1000):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        # "type": "bus_station",
        "keyword": "Bus stop",
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        bus_stops = []
        for place in data.get('results', []):
            name = place['name']
            location = place['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            
            distance = calculate_distance(latitude, longitude, lat, lng)
            
            bus_stops.append((name, lat, lng, distance))

        # Sort bus stops by distance (closest first)
        bus_stops.sort(key=lambda x: x[3])

        return bus_stops
    else:
        print("Failed to get nearby bus stops.")
        return []

def calculate_distance(lat1, lng1, lat2, lng2):
    distance = gmap.distance_matrix([str(lat1) + " " + str(lng1)], [str(lat2) + " " + str(lng2)], mode='walking')['rows'][0]['elements'][0] # type: ignore
    return distance['distance']['value']





def initiate(target_latitude ,target_longitude):
    
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    
    

    # Replace these coordinates with the latitude and longitude of the target location
    # print(get_current_location(api_key))

    # Set the search radius in meters (default is 1000 meters)
    search_radius = 1000

    bus_stops = get_nearby_bus_stops(api_key, target_latitude, target_longitude, search_radius)

    if bus_stops:
        # print("Nearby bus stops:")
        # for stop in bus_stops:
        #     name, lat, lng, distance = stop
        #     print(f"{name} (Latitude: {lat}, Longitude: {lng}), Distance: {distance:.2f} meters")
        # print(bus_stops[0])
        return bus_stops[0]
    else:
        print("No nearby bus stops found.")
        return None
        

