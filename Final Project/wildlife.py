import requests

def get_species_list(coordinate, radius):
    """
    Retrieves a list of species in an area defined by coordinates and radius.
    """
    lat = coordinate['']
    lon = coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={lat},{lon},{radius}"
    response = requests.get(url).json()
    species_list = response.get("SpeciesSightingSummariesContainer", {}).get("SpeciesSightingSummary", [])
    return species_list

def get_surveys_by_species(coordinate, radius, taxonid):
    """
    Retrieves a list of surveys for a given species in an area defined by coordinates and radius.
    """
    lat = coordinate['latitude']
    lon = coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&circle={lat},{lon},{radius}"
    response = requests.get(url).json()
    features = response.get("features", [])
    return features

# Uncomment to test the functions
# assert get_species_list({'latitude': -27.4689682, 'longitude': 153.0234991}, 100000)
# assert get_surveys_by_species({'latitude': -27.4689682, 'longitude': 153.0234991}, 100000, 1039)
