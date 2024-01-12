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
        self.__attack_type = self.__attacks_data['type']
        
        # Reflechir si mettre ici le sprite
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
<<<<<<< HEAD
    def get_attack_type(self):
        return self.__attack_type
=======
    def get_pokemon_sprite(self):
<<<<<<< HEAD:game/pokemon.py
        return self.pokemon_sprite
=======
        return self.pokemon_sprite
>>>>>>> 8c7954fcb6805fe7837e0941608de609af78c013

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

n = Pokemon("Salameche",)
print(n.get_attack_type())

>>>>>>> 45f801698a2521bb5bf3e9319dadf71e3254fa66:pokemon.py
