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
        self.run_end()

    def run_end(self):
        while self.player_pokemon.isAlive and self.enemy_pokemon.isAlive:
            self.player_turn()
            
            time.sleep(1)

            self.enemy_turn()
            
            if self.player_pokemon.isAlive and self.enemy_pokemon.isAlive == False:
                break

    def player_turn(self):
        if self.player_pokemon.__speed > self.enemy_pokemon.__speed:
            self.player_attack()

    def enemy_turn(self):
        if self.player_pokemon.__speed < self.enemy_pokemon.__speed:
            self.enemy_pokemon_attack()

    def check_damage_type(self):
        damage = self.player_pokemon.get_type() 