import sounds
from pygame import mixer

class Sound_effect(sounds.Sound):
    def __init__(self, game):
        super().__init__(game)
        self.click_sound = mixer.Sound('assets/sounds/click.mp3')
        self.attack_effective_sound = mixer.Sound('assets/sounds/attack.mp3')
        self.attack_sound = mixer.Sound('assets/sounds/attack2.mp3')
        # self.pokeball_sound = mixer.Sound('/assets/sounds/pokeball.wav')

    def play_click_sound(self):
        self.attack_sound.set_volume(0.5)
        self.click_sound.play()

    def play_pokemon_sound(self,pokemon):
        pokemon_sound = mixer.Sound(f'assets/sounds/pokemons/{pokemon}.mp3')
        pokemon_sound.play()
        
    def play_attack_sound(self):
        self.attack_sound.set_volume(0.3)
        self.attack_sound.play()
    
    def play_attack_effective_sound(self):
        self.attack_effective_sound.set_volume(0.3)
        self.attack_effective_sound.play()
    # def play_pokeball_sound(self):
    #     self.pokeball_sound.play()