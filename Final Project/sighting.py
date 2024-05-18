from nominatim import gps_coordinate
from wildlife import get_species_list, get_surveys_by_species

# Constants
RADIUS = 100000

def display_menu():
    """
    Displays the menu to the user.
    """
    print("Help")
    print("====")
    print("The following commands are recognised.")
    print("Display help    wildlife> help")
    print("Exit the application  wildlife> exit")
    print("Display animal species in a city    wildlife> species <city>")
    print("Display animal sightings in a city  wildlife> sightings <city> <taxonid>")
    print("Display venomous species   wildlife> species <city> venomous")

def gps(city):
    """
    Retrieves GPS coordinates for a given city.
    """
    return gps_coordinate(city)

def search_species(city):
    """
    Retrieves a list of species for a given city.
    """
    coordinates = gps(city)
    species_list = get_species_list(coordinates, RADIUS)
    return species_list

def search_sightings(taxonid, city):
    """
    Retrieves a list of sightings for a given species and city.
    """
    coordinates = gps(city)
    sightings = get_surveys_by_species(coordinates, RADIUS, taxonid)
    incidental_sightings = [sighting for sighting in sightings if sighting["properties"]["SiteCode"] == "INCIDENTAL"]
    return incidental_sightings

def filter_venomous(species_list):
    """
    Filters the list of species to include only venomous species.
    """
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

def display_species(species_list):
    """
    Displays a list of species.
    """
    for species in species_list:
        common_name = species["Species"]["AcceptedCommonName"]
        pest_status = species["Species"]["PestStatus"]
        print(f"Species: {common_name}, Pest Status: {pest_status}")

def display_sightings(sightings):
    """
    Displays a list of animal sightings, sorted by date.
    """
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Sighting Date: {start_date}, Locality: {locality}")

def earliest(sightings):
    """
    Returns the sighting with the earliest start date.
    """
    return min(sightings, key=lambda x: x["properties"]["StartDate"])

def sort_by_date(sightings):
    """
    Returns the sightings sorted by date.
    """
    return sorted(sightings, key=lambda x: x["properties"]["StartDate"])

def main():
    """
    Main function to handle user input and commands.
    """
    display_menu()
    while True:
        command = input("wildlife> ").strip()
        if command == "help":
            display_menu()
        elif command == "exit":
            break
        elif command.startswith("species "):
            parts = command[len("species "):].strip().split()
            if len(parts) == 1:
                city = parts[0]
                species_list = search_species(city)
                display_species(species_list)
            elif len(parts) == 2 and parts[1] == "venomous":
                city = parts[0]
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                print("Invalid command format. Use: species <city> [venomous]")
        elif command.startswith("sightings "):
            parts = command[len("sightings "):].strip().split()
            if len(parts) == 2:
                city, taxonid = parts
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            else:
                print("Invalid command format. Use: sightings <city> <taxonid>")
        else:
            print("Unrecognized command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
