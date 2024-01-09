import json
from datamanager import *
class Pokemon:
    def __init__(self, pokemon_name, data_manager):
        
        self.__pokemon_data = data_manager.get_pokemon_data(pokemon_name)
        self.__attacks_data = data_manager.get_attack_data(pokemon_name)
        self.__name = pokemon_name
        self.__health = self.__pokemon_data['health']
        self.__defense = self.__pokemon_data['defense']
        self.__attack = self.__pokemon_data['attack']
        self.__speed = self.__pokemon_data['speed']
        self.__type = self.__pokemon_data['type']
        self.__level = 1
        self.__own_attacks = self.__attacks_data
        

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_defense(self):
        return self.__defense
    def get_attack(self):
        return self.__attack
    def get_attacks(self):
        return self.__own_attacks
    def get_speed(self):
        return self.__speed
    def get_type(self):
        return self.__type

    #Fonctions de debug
    def see_info(self):
        print(f"Name : {self.get_name()} Health : {self.get_health()} Defense : {self.get_defense()} Attaque : {self.get_attack()} Speed : {self.get_speed()} Type : {self.get_type()}")
    def see_attacks(self):
        print(f"Attaques : {self.get_attacks()}")
    def list_attacks(self):
        for key in self.__own_attacks:
            print(key)
            print(self.__own_attacks[key])
            print("Degats de flameche",self.__own_attacks["Flammeche"]["type"])



data_manager = Data_manager()
bulbizare = Pokemon("Bulbizarre",data_manager)
salameche = Pokemon("Salameche", data_manager)

# bulbizare.see_info()
# bulbizare.see_attacks()
# salameche.see_info()
# salameche.see_attacks()

salameche.list_attacks()
