import game
import time
import data

class Fight:
    def __init__(self, game) -> None:
        self.game = game
        self.data_manager = data.Data_manager()
        self.type_chart = self.data_manager.get_type_chart_data()
        
        self.enemy_pokemon = None
        self.player_pokemon = None
        self.turn_order = None
        
        self.selected_attack = None 
        
    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        self.player_pokemon = game.Pokemon(player_pokemon_name)
        self.enemy_pokemon = game.Pokemon(enemy_pokemon_name)
        self.turn_order = self.determine_turn_order()
        # self.run_end()
        # self.determine_winner()
        print(self.type_chart[self.player_pokemon.get_type()][self.enemy_pokemon.get_type()])

    def run_end(self):
        
        
        while self.player_pokemon.isAlive and self.enemy_pokemon.isAlive:
            for pokemon in self.turn_order:
                if pokemon == self.player_pokemon:
                    self.player_turn()
                else:
                    self.enemy_attack()

                if not self.player_pokemon.isAlive or not self.enemy_pokemon.isAlive:
                    break

            time.sleep(1)

    def player_turn(self):  # Add this method
        self.selected_attack = None
        while self.selected_attack is None:
            pass
            # self.selected_attack = self.game.get_player_choice()
        self.player_attack()
    
    def player_attack(self):
        self.calculate_damage(self.player_pokemon, self.enemy_pokemon)
    def enemy_attack(self):
        self.calculate_damage(self.enemy_pokemon, self.player_pokemon)
    
    def check_damage_type(self,attacker, defender):
        attacker_type = attacker.get_type()
        defender_type = defender.get_type()
        return attacker_type, defender_type
        
        
    def calculate_damage(self, attacker, defender):
        attacker_type, defender_type = self.check_damage_type(attacker, defender)
        damage_multiplicator = self.type_chart[attacker_type][defender_type]
        damage = (attacker.get_attack() * damage_multiplicator) / (defender.get_defense() / 100)
        return damage
        
        
        
        
    
    def determine_turn_order(self):
        if self.player_pokemon.get_speed() > self.enemy_pokemon.get_speed():
            return [self.player_pokemon, self.enemy_pokemon]
        else:
            return [self.enemy_pokemon, self.player_pokemon]
    def get_turn_order(self):
        return [pokemon.name for pokemon in self.turn_order]
    
    def determine_winner(self):
        if self.player_pokemon.isAlive:
            return self.player_pokemon
        else:
            return self.enemy_pokemon