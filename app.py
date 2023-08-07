from flask import Flask, render_template
from flask import request
from nearby import initiate
from userlocation import get_current_location
import googlemaps
from key import api_key


app = Flask(__name__)
gmaps = googlemaps.Client(key=api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    target_latitude ,target_longitude = get_current_location(api_key)
    props = {
        "latitude":target_latitude,
        "longitude":target_longitude,
        "api_key":api_key
    }
    if request.method == 'POST':
        global destination
        destination = request.form['destination']
        print(destination)
        busstop1 = initiate(target_latitude ,target_longitude)
        dest = gmaps.geocode(destination)[0]['geometry']['location']
        busstop2 = initiate(dest['lat'],dest['lng'])
        props={
            "latitude":target_latitude,
            "longitude":target_longitude,
            "api_key":api_key,
            "busstop1":busstop1,
            "busstop2":busstop2,
            "destlat":dest['lat'],
            "destlng":dest['lng']
        }
        return render_template('index.html', title='Home',props=props)
    return render_template('index.html', title='Home',props=props)
# def get_directions():
#     target_latitude ,target_longitude = get_current_location(api_key)
#     busstop1 = initiate(target_latitude ,target_longitude)
    # if request.method == 'POST':
    #     global destination
    #     destination = request.form['destination']
    #     # print(destination)
#         dest = gmaps.geocode(destination)[0]['geometry']['location'] # type: ignore
#         busstop2 = initiate(dest['lat'],dest['lng'])
#     return render_template('index.html', title='Home',api_key=api_key)


if __name__ == '__main__':
    app.run(debug=True)
