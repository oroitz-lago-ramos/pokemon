import game
import time
import data

class Fight:
    def __init__(self, game, sound_effects) -> None:
        self.game = game
        self.sound_effects = sound_effects
        
        self.data_manager = data.Data_manager()
        self.type_chart = self.data_manager.get_type_chart_data()
        
        self.enemy_pokemon = None
        self.player_pokemon = None
        self.turn = None
        
        self.waiting_for_player = True
        self.selected_attack = None 


    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        print("Fight started")
        self.player_pokemon = game.Pokemon(player_pokemon_name)
        self.enemy_pokemon = game.Pokemon(enemy_pokemon_name)
        self.turn = self.determine_turn_order()
        
        
    def update(self):
        if self.turn == 'player' and not self.waiting_for_player:
            print("Player's turn")
            self.player_attack()
            self.turn = 'enemy'
            self.waiting_for_player = True
        elif self.turn == 'enemy' and not self.waiting_for_player:
            print("Enemy's turn")
            self.enemy_attack()
            self.turn = 'player'
            self.waiting_for_player = True
        if self.verify_if_fight_is_over():
            self.game.change_current_state(self.game.MENU)
            print("Fight is over")
            print(f"Winner is {self.determine_winner().get_name()}")
        else:
            print(f"Player's health: {self.player_pokemon.get_health()}")
            print(f"Enemy's health: {self.enemy_pokemon.get_health()}")
        

    def player_attack(self):
        damage = self.calculate_damage(self.player_pokemon, self.enemy_pokemon)
        self.enemy_pokemon.take_damage(damage)
        
    def enemy_attack(self):
        damage = self.calculate_damage(self.enemy_pokemon, self.player_pokemon)
        self.player_pokemon.take_damage(damage)
    
    def check_damage_type(self,attacker, defender):
        attacker_type = attacker.get_type()
        defender_type = defender.get_type()
        return attacker_type, defender_type
        
        
    def calculate_damage(self, attacker, defender):
        attacker_type, defender_type = self.check_damage_type(attacker, defender)
        damage_multiplicator = self.type_chart[attacker_type][defender_type]
        damage = (attacker.get_attack() * damage_multiplicator) / defender.get_defense()
        return damage
        
        
        
        
    
    def determine_turn_order(self):
        if self.player_pokemon.get_speed() > self.enemy_pokemon.get_speed():
            return 'player'
        else:
            return 'enemy'
    
    def verify_if_fight_is_over(self):
        if not self.player_pokemon.get_is_alive() or not self.enemy_pokemon.get_is_alive():
            return True
        else:
            return False
        
    def determine_winner(self):
        if self.player_pokemon.get_is_alive():
            return self.player_pokemon
        else:
            return self.enemy_pokemon