import pygame
import data
import game

class Player_pokemon(game.Pokemon):
    def __init__(self, pokemon_name):
        self.data_manager = data.Data_manager()
        self.__pokemon_data = self.data_manager.get_pokemon_by_name(pokemon_name)
        super().__init__(pokemon_name, self.__pokemon_data)
        self.pokemon_sprite = pygame.image.load(f'assets/images/sprites/dos/{self.id}.png')
       
    




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



