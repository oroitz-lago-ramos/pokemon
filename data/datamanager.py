import json

class Data_manager:
    def __init__(self):
        self.pokedex_filepath = 'data/pokedex.json'
        self.pokemon_filepath = 'data/pokemon.json'
        self.type_chart_filepath = 'data/type_chart.json'
        self.player_filepath = 'data/player.json'

        self.pokedex_data = self.read_json(self.pokedex_filepath)
        self.pokemon_data = self.read_json(self.pokemon_filepath)
        self.type_chart_data = self.read_json(self.type_chart_filepath)
        self.player_data = self.read_json(self.player_filepath)

    def read_json(self, FILEPATH):
        try :
            with open(FILEPATH) as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError:
            print("Le fichier n'existe pas")

    def store_json_data(self, data, FILEPATH):
        try:
            with open(FILEPATH, 'w') as outfile:
                json.dump(data, outfile)
        except FileNotFoundError:
            print("Le fichier n'existe pas")

    def get_pokedex_data(self):
        return self.pokedex_data
    def get_pokemon_data(self):
        return self.pokemon_data
    def get_type_chart_data(self):
        return self.type_chart_data
    
    def get_pokemon_by_name(self, pokemon_name):
        for pokemon in self.pokemon_data:
            if pokemon['name'] == pokemon_name:
                return pokemon
        return None
    
    def get_selected_pokemon(self):
        return self.player_data["selected_pokemon"]
    
    
    def get_pokemon_name_by_id(self, id):
        for pokemon in self.pokedex_data:
            if pokemon['id'] == id:
                return pokemon['name']
        return None
    
    def get_pokemon_by_name_in_pokedex(self, pokemon_name):
        for pokemon in self.pokedex_data:
            if pokemon['name'] == pokemon_name:
                return pokemon
        return None
    
    def set_pokedex_discovered(self, pokemon_name):
        for pokemon in self.pokedex_data:
            if pokemon['name'] == pokemon_name:
                pokemon['discovered'] = True
                self.store_json_data(self.pokedex_data, self.pokedex_filepath)
                break
    
    def from_pokedex_to_pokemon(self, pokemon_name):
        self.set_pokedex_discovered(pokemon_name)
        pokedex_pokemon = self.get_pokemon_by_name_in_pokedex(pokemon_name)
        if pokedex_pokemon:
            self.pokemon_data.append(pokedex_pokemon)
            self.store_json_data(self.pokemon_data, self.pokemon_filepath)
        
    def update_selected_pokemon(self,name):
            self.player_data["selected_pokemon"] = name
            self.store_json_data(self.player_data, self.player_filepath)
        
    """
    save_pokemon(name)
    
        for i in range len item:
        le charger dans le pokemon.json
    
    """
    """
    save  pokemon lvl(name):
    for item in self.pokedex_data
        for i in range len item:
        le charger dans le pokemon.json
    
    """
    
    