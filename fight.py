import json
from datamanager import *
from pokemon import *

class Fight:
    def __init__(self,game):
        self.game = game
        self.data_manager = Data_manager()

    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        player_pokemon = Pokemon(player_pokemon_name)
        enemy_pokemon = Pokemon(enemy_pokemon_name)
        

