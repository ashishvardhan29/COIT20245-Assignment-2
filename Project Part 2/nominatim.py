import requests

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()[0]
    return {'latitude': float(data['lat']), 'longitude': float(data['lon'])}
