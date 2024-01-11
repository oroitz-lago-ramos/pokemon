import pygame
class Pokemon:
    def __init__(self, pokemon_name, data_manager):
        self.__pokemon_data = data_manager.get_pokemon_data(pokemon_name)
        self.__attacks_data = data_manager.get_attack_data(pokemon_name)
        self.__name = pokemon_name
        self.__health = self.__pokemon_data['health']
        self.__maxhealth = self.__pokemon_data['health']
        self.__defense = self.__pokemon_data['defense']
        self.__attack = self.__pokemon_data['attack']
        self.__speed = self.__pokemon_data['speed']
        self.__type = self.__pokemon_data['type']
        self.__level = 1
        self.__own_attacks = self.__attacks_data
        
        self.pokemon_sprite = pygame.image.load(f'assets/images/sprites/{self.__name}.png')
       
        

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_max_health(self):
        return self.__maxhealth
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
    def get_pokemon_sprite(self):
        return self.pokemon_sprite