import json
from datamanager import *
from pokemon import *

class Fight:
    def __init__(self,game):
        self.game = game
        
        
        self.player_pokemon = None
        self.enemy_pokemon = None

    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        self.player_pokemon = Pokemon(player_pokemon_name, self.game.data_manager)
        self.enemy_pokemon = Pokemon(enemy_pokemon_name, self.game.data_manager)
        

