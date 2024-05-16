import nominatim
import wildlife

def display_menu()
    print("Help\n====")
    print("The following commands are recognised:")
    print("Display help wildlife> help")
    print("Exit the application wildlife> exit")
    print("Display animal species in a city wildlife> species <CityName>")
    print("Display animal sightings in a city wildlife> sightings <CityName> <TaxonID>")
    print("Display venomous species wildlife> species <CityName> venomous")

def search_species(city):
    coordinates = nominatim.gps_coordinate(city)
    return wildlife.get_species_list(coordinates, radius=100000)

def display_species(species_list):
    for species in species_list:
        print(f"{species['Species']['AcceptedCommonName']} - {species['Species']['PestStatus']}")

def filter_venomous(species_list):
    return [species for species in species_list if species['Species']['PestStatus'] == 'Venomous']

def search_sightings(taxonid, city):
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def display_sightings(sightings):
    for sighting in sightings:
        print(f"Sighted on {sighting['properties']['StartDate']} at {sighting['properties']['LocalityDetails']}")

def main():
    display_menu()
    while True:
        command = input("wildlife> ").strip().lower()
        if command == 'help':
            display_menu()
        elif command == 'exit':
            print("Exiting the program.")
            break
        elif command.startswith('species '):
            parts = command.split()
            if len(parts) == 3 and parts[2] == 'venomous':
                city = parts[1]
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            elif len(parts) == 2:
                city = parts[1]
                species_list = search_species(city)
                display_species(species_list)
            else:
                print("Invalid command.")
        elif command.startswith('sightings '):
            parts = command.split()
            if len(parts) == 3:
                city = parts[1]
                taxonid = parts[2]
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            else:
                print("Invalid command.")
        else:
            print("Invalid command. Type 'help' for options.")

if __name__ == "__main__":
    main()
