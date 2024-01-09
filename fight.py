import json
from datamanager import *
from pokemon import *

class Fight:
    def __init__(self):
        self.data_manager = Data_manager()

    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        player_pokemon_data = self.data_manager.get_pokemon_data(player_pokemon_name)
        player_pokemon_attacks_data = self.data_manager.get_attack_data(player_pokemon_name)
        enemy_pokemon_data = self.data_manager.get_pokemon_data(enemy_pokemon_name)
        enemy_pokemon_attacks_data = self.data_manager.get_attack_data(player_pokemon_name)
    
        player_pokemon = Pokemon(player_pokemon_data)
        enemy_pokemon = Pokemon(enemy_pokemon_data)

