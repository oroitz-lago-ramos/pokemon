import game
class Fight:
    def __init__(self, game) -> None:
        self.game = game
        
        self.enemy_pokemon = None
        self.player_pokemon = None
        
    def start_fight(self, player_pokemon_name, enemy_pokemon_name):
        self.player_pokemon = game.Pokemon(player_pokemon_name, self.game.data_manager)
        self.enemy_pokemon = game.Pokemon(enemy_pokemon_name, self.game.data_manager)
    def get_player_pokemon(self):
        return self.player_pokemon
    
