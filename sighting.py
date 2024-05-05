def display_menu():
    """
    Function to display the main menu options.
    """
    print("Help\n====")
    print("The following commands are recognised:")
    print("Display help: help")
    print("Exit the application: exit")
    print("Display animal species in a city: species <city>")
    print("Display animal sightings in a city: sightings <city> <taxonid>")
    print("Display venomous species in a city: species <city> venomous")

# For debugging
display_menu()

def search_species(city):
    """
    Stub function to simulate species search in a city.
    """
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    """
    Function to display a list of species.
    """
    for species in species_list:
        print(f"{species['Species']['AcceptedCommonName']} ({species['Species']['PestStatus']})")

def search_sightings(taxonid, city):
    """
    Stub function to simulate searching for animal sightings based on taxonid and city.
    """
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def display_sightings(sightings):
    """
    Function to display animal sightings.
    """
    for sighting in sightings:
        print(f"Sighting on {sighting['properties']['StartDate']} at {sighting['properties']['LocalityDetails']}")


def filter_venomous(species_list):
    """
    Filters and returns only venomous species from the list.
    """
    return [species for species in species_list if species['Species']['PestStatus'] == 'Venomous']

def main():
    """
    Main function to handle user commands.
    """
    display_menu()
    while True:
        command = input("wildlife> ").strip()
        if command == "help":
            display_menu()
        elif command == "exit":
            print("Exiting the application.")
            break
        elif command.startswith("species"):
            parts = command.split()
            if len(parts) == 3 and parts[2] == "venomous":
                # Later implementation for venomous species filter
                pass
            elif len(parts) == 2:
                species_list = search_species(parts[1])
                display_species(species_list)
            else:
                print("Invalid command or parameters.")
        elif command.startswith("sightings"):
            parts = command.split()
            if len(parts) == 3:
                sightings_list = search_sightings(parts[2], parts[1])
                display_sightings(sightings_list)
            else:
                print("Invalid command or parameters.")
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
