import requests

def gps_coordinate():
    """
    Retrieves GPS coordinates for a given city using the Nominatim web service.
    """
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url).json()
    if response:
        latitude = float(response[0]['lat'])
        longitude = float(response[0]['lon'])
        return {'latitude': latitude, 'longitude': longitude}
    return None

# Uncomment to test the function
# assert gps_coordinate("Brisbane") == {'latitude': -27.4689682, 'longitude': 153.0234991}
