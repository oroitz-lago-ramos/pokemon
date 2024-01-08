# pokemon

## Rules

Ecrire les fonctions, les classes et les variables en anglais
Creer des branches par fonctionnalités




## Structure du projet

class Pokemon:
    attributs : 
        name
        MaxLife
        life
        level
        attack
        defense
        type
    methodes : 
        Getters and Setters
        recevoir degats
        

class Combat:
    Permettra de gerer le combat
    attributs : 
        my_pokemon
        ennemi_pokemon
    methodes : 
        recup info ennemi
        calcul de degats
        faire degats

class Game:
    Permettra de gerer la boucle et les differents etats(menu, pokedex, combat)
    attributs :
        display = Graphics()
    methodes : 
        play
        stop

class Graphics:
    Permet de gerer le display


## On doit discutter de

comment structurer le pokedex.json
comment gerer les types
si utiliser des sous classes qui herites de pokemon (ex. FirePokemon(Pokemon)) ou utiliser une autre méthode
comment gerer le calcul des damages


