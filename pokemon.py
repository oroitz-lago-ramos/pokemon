import json

class Pokemon:
    def __init__(self,index):
        self.__name = ""
        self.__health = 0
        self.__defense = 0
        self.__attack = 0
        self.__speed = 0
        self.__type = ""
        self.__level = 0
        self.__index = index
        self.__own_attack = {}
        self.choose_pokemon_by_index()
        self.attacks_pokemon()

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_defense(self):
        return self.__defense
    def get_attack(self):
        return self.__attack
    def get_speed(self):
        return self.__speed
    def get_type(self):
        return self.__type
    def get_index(self):
        return self.__index
    def get_attacks(self):
        return self.__own_attack
    def see_info(self):
        print(f"Name : {self.get_name()} Health : {self.get_health()} Defense : {self.get_defense()} Attaque : {self.get_attacks()} Speed : {self.get_speed()} Type : {self.get_type()} Index : {self.get_index()}")
    def see_attacks(self):
        print(f"Attques : {self.get_attack()}")

    def choose_pokemon_by_index(self):
        with open('pokemon.json', 'r') as fichier_json:
            data = json.load(fichier_json)
            for name, pokemon_data in data.items():
                if pokemon_data.get("index") == self.__index:
                    self.__name = name
                    self.__health = pokemon_data.get("health", 0)
                    self.__defense = pokemon_data.get("defense", 0)
                    self.__attack = pokemon_data.get("attack", 0)
                    self.__speed = pokemon_data.get("speed", 0)
                    self.__type = pokemon_data.get("type", "")
                    self.__index = pokemon_data.get("index", 0)
    def attacks_pokemon(self):
        with open('attacks.json', 'r') as fichier_json:
            data = json.load(fichier_json)
            if self.__name in data:
                self.__own_attack = data[self.__name]



bulbizare = Pokemon(1)
salameche = Pokemon(2)

bulbizare.see_info()
bulbizare.see_attacks()
salameche.see_info()
salameche.see_attacks()

