import pygame
import data

class Pokemon:
    def __init__(self, pokemon_name):
        self.data_manager = data.Data_manager()
        self.__pokemon_data = self.data_manager.get_pokemon_by_name(pokemon_name)
        self.__name = pokemon_name
        self.__max_health = self.__pokemon_data['max_health']
        self.__health = self.__max_health
        self.__attack = self.__pokemon_data['attack']
        self.__defense = self.__pokemon_data['defense']
        self.__speed = self.__pokemon_data['speed']
        self.__type = self.__pokemon_data['type']
        self.__level = 1 
        self.__xp = 100 #mise en place de la variable a 100
        self.__until_next_level = self.__xp #j'ai basé la variable sur la valeur de base de xp juste au dessus 
        self.is_alive = True
        
        # Reflechir si mettre ici le sprite
        self.pokemon_sprite = pygame.image.load(f'assets/images/sprites/{self.__name}.png')
       
        

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


    def gain_experience(self, xp):
        self.__until_next_level -= xp

        if self.__until_next_level <= 0:
            self.__level += 1
            self.__until_next_level += 100 + (self.__level - 1) * 100
        else:
            self.__until_next_level -= xp



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



