import json
from datamanager import *
from pokemon import *

class Fight:
    def __init__(self):
        self.data_manager = Data_manager()
        self.enemy_pokemon = None
        self.player_pokemon = None
    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        self.player_pokemon = Pokemon(player_pokemon_name)
        self.enemy_pokemon = Pokemon(enemy_pokemon_name)
        if self.player_pokemon.get_speed() >= self.enemy_pokemon.get_speed():
            # Le joueur attaque en premier
            pass
        else:
            # l'adversaire attaque en premier
            pass

    def do_attack(self,attacker_pokemon, targeted_pokemon):
        degats = None
        targeted_pokemon.take_damage(degats)
    def calculte_damage(self):
        mulitpicateur_damage = 0
        if self.player_pokemon.get_type()  == self.enemy_pokemon.get_type():
            mulitpicateur_damage = 0
            self.player_pokemon.__health -= self.enemy_pokemon.degat_attack
        elif self.player_pokemon.get_type() == 
            mulitpicateur_damage = 2
            self.player_pokemon.__health -= mulitpicateur_damage *self.enemy_pokemon.degat_attack






        
        


