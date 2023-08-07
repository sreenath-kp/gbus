import gmaps
from key import api_key
gmaps.configure(api_key=api_key) 
from userlocation import get_current_location

center = get_current_location(api_key)
gmaps.figure(center=center, zoom_level=12, map_type='TERRAIN')
