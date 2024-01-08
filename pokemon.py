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
        self.__own_attack = []
        self.__degat_attack = 40
        self.__precision_attack = 100
        self.__type_attack = ""
        self.__attack_one = ""
        self.__attack_two = ""
        self.choose_pokemon_by_index()

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
    
    def get_info(self):
        print(f"Name : {self.__name} Health : {self.__health} Defense : {self.__defense} Attaque : {self.__attack} Speed : {self.__speed} Type : {self.__type} Index : {self.__index}")

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
                attacks_data = data[self.__name].get("attacks", {})
                for attack_name, attack_info in attacks_data.items():
                    print(f"Attack: {attack_name}, Damage: {attack_info['degat']}, Type: {attack_info['type']}")



bulbizare = Pokemon(1)
salameche = Pokemon(2)

bulbizare.get_info()
bulbizare.attacks_pokemon()
salameche.get_info()
salameche.attacks_pokemon()

