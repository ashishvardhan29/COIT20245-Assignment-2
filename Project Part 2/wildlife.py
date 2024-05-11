import requests

def get_species_list(coordinate, radius):
    lat, lon = coordinate['latitude'], coordinate['longitude']
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={lat},{lon},{radius}"
    response = requests.get(url)
    data = response.json()
    return data['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']
