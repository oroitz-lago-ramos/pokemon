import pygame
import data

class Pokemon:
    """Classe représentant un pokemon"""
    def __init__(self, pokemon_name, data):
        
        self.__name = pokemon_name
        self.id = data['id']
        self.__level = 1
        self.__max_health = data['max_health'] + 0.5 * self.__level
        self.__health = self.__max_health
        self.__attack = data['attack'] + 0.1 * self.__level
        self.__defense = data['defense'] + 0.05 * self.__level 
        self.__speed = data['speed'] + 0.05 * self.__level
        self.__type = data['type']
        self.__until_next_level = 100
        self.is_alive = True
        
        # Reflechir si mettre ici le sprite
        self.pokemon_sprite = None
       
        

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_max_health(self):
        return self.__max_health
    def get_defense(self):
        return self.__defense
    def get_attack(self):
        return self.__attack
    def get_speed(self):
        return self.__speed
    def get_type(self):
        return self.__type
    def get_level(self):
        return self.__level
    def get_until_next_level(self):
        return self.__until_next_level
    def get_is_alive(self):
        return self.is_alive
    

    def get_pokemon_sprite(self):
        return self.pokemon_sprite
    def decreease_until_next_level(self, amount):
        self.__until_next_level -= amount
    
    def take_damage(self, damage):
        self.__health -= damage
        # for i in range(damage):
        #     self.__health -= 1
        self.check_if_alive()
    
    def check_if_alive(self):
        if self.__health <= 0:
            self.is_alive = False
            self.__health = 0
        
    




    #Fonctions de debug
    # def see_info(self):
    #     print(f"Name : {self.get_name()} Health : {self.get_health()} Defense : {self.get_defense()} Attaque : {self.get_attack()} Speed : {self.get_speed()} Type : {self.get_type()}")
    # def see_attacks(self):
    #     print(f"Attaques : {self.get_attacks()}")
    # def list_attacks(self):
    #     for key in self.__own_attacks:
    #         print(key)
    #         print(self.__own_attacks[key])
    #         print("Degats de flameche",self.__own_attacks["Flammeche"]["type"])



