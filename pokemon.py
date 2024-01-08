import json
class Pokemon:
    def __init__(self,name,health,defense,attack,speed,type):
        self.__name = name
        self.__health = health
        self.__defense = defense
        self.__attack = attack
        self.__speed = speed
        self.__type = type
        self.__level = 0

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_defense(self):
        return self.__defense
    def get_attaque(self):
        return self.__attack
    def get_vitesse(self):
        return self.__speed
    def get_type(self):
        return self.__type
    def get_level(self):
        return self.__level
    def take_damage(self,damage):
        self.__health -= damage





    