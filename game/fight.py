import game
import time

class Fight:
    def __init__(self, game) -> None:
        self.game = game
        
        self.enemy_pokemon = None
        self.player_pokemon = None
        
    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        self.player_pokemon = game.Pokemon(player_pokemon_name)
        self.enemy_pokemon = game.Pokemon(enemy_pokemon_name)
        #self.run()

    def run_end(self):
        while self.player_pokemon.isAlive and self.enemy_pokemon.isAlive:
            self.player_turn()
            
            time.sleep(1)

            self.enemy_turn()
            
            if self.player_pokemon.isAlive == False:
                self.run()
                break

    def player_turn(self):
        pass

    def enemy_turn(self):
        pass




"""
# Check who attack first
        self.attacker = self.check_who_attack_first()

    def check_who_attack_first(self):
        if self.__player_pokemon.get_speed() > self.__enemy_pokemon.get_speed():
            return self.__player_pokemon
        elif self.__player_pokemon.get_speed() < self.__enemy_pokemon.get_speed():
            return self.__enemy_pokemon
        else:
            return random.choice([self.__player_pokemon, self.__enemy_pokemon])
"""
