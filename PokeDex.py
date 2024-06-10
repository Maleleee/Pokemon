# Program is strictly for the Kanto Region only, other regions aren't included.

class Pokemon:
    def __init__(self, name, ptype, level, area):
        self.name = name
        self.ptype = ptype
        self.level = level
        self.area = area

    def __str__(self):
        return f"Name: {self.name}, Type: {self.ptype}, Level: {self.level}, Area: {self.area}"


class PokeDex:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        if any(p.name == pokemon.name for p in self.pokemon_list):
            print(f"{pokemon.name} is already in the Pokédex.")
        else:
            self.pokemon_list.append(pokemon)
            print(f"{pokemon.name} has been added to the Pokédex.")

    def get_pokemon_info(self, name):
        for pokemon in self.pokemon_list:
            if pokemon.name == name:
                return str(pokemon)
        return f"{name} is not in the Pokédex."

    def list_all_pokemon(self):
        if not self.pokemon_list:
            return "The Pokédex is empty."
        return "\n".join(str(pokemon) for pokemon in self.pokemon_list)


kanto_areas = [
    "Pallet Town", "Viridian City", "Pewter City", "Cerulean City", "Vermilion City",
    "Lavender Town", "Celadon City", "Fuchsia City", "Saffron City", "Cinnabar Island",
    "Indigo Plateau", "Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6",
    "Route 7", "Route 8", "Route 9", "Route 10", "Route 11", "Route 12", "Route 13",
    "Route 14", "Route 15", "Route 16", "Route 17", "Route 18", "Route 19", "Route 20",
    "Route 21", "Route 22", "Route 23", "Route 24", "Route 25", "Viridian Forest",
    "Mt. Moon", "S.S. Anne", "Rock Tunnel", "Power Plant", "Pokemon Tower",
    "Safari Zone", "Seafoam Islands", "Pokemon Mansion", "Victory Road", "Cerulean Cave",
    "Diglett's Cave"
]



def display_areas():
    print("Valid areas in the Kanto region:")
    for area in kanto_areas:
        print(f"- {area}")


kanto_pokedex = PokeDex()

while True:
    print("\nWelcome to the Kanto Pokédex!")
    print("1. Add a Pokémon")
    print("2. Get Pokémon info")
    print("3. List all Pokémon")
    print("4. Display valid areas")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the name of the Pokémon: ")
        ptype = input("Enter the type of the Pokémon: ")
        level = int(input("Enter the level of the Pokémon: "))
        area = input("Enter the area where you caught the Pokémon: ")

        if area not in kanto_areas:
            print("Invalid area. Please enter a valid Kanto region area.")
        else:
            kanto_pokedex.add_pokemon(Pokemon(name, ptype, level, area))

    elif choice == '2':
        name = input("Enter the name of the Pokémon: ")
        print(kanto_pokedex.get_pokemon_info(name))

    elif choice == '3':
        print(kanto_pokedex.list_all_pokemon())

    elif choice == '4':
        display_areas()

    elif choice == '5':
        print("Exiting the Kanto Pokédex. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
