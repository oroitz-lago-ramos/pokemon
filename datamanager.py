import json

class Data_manager:
    def __init__(self):
        self.pokemon_data = self.load_data('pokemon.json')
        self.attacks_data = self.load_data('attacks.json')

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    def get_pokemon_data(self, pokemon_name):
        return self.pokemon_data.get(pokemon_name)

    def get_attack_data(self, pokemon_name):
        return self.attacks_data.get(pokemon_name)