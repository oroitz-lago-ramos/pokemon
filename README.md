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


demander comment ameilleurer display, fight avec le datamanager, pokemon




#
Message de fin annuler l'attaque de celui qui a perdu (ajouter un nouveau state pour afficher le message)
Gerer bien le pokedex et la generation aleatoires de pokemon ennemis
ecran de selection de pokemon
implementer xp et evolution (dans le json attribut evolu et passe a l'id suivant)
modifier l'attaque et la defense en focntion du niveau (grace init pokemon)
heredité pour diferencier ennemi ou player pokemon?
que le message du pokemon attaque vienne apres que les degats aient ete réalisés
demander aux autres si on fusionne les json pokemon et pokedex
Recuperer la valeur du multiplicateur pour afficher un message personnalisé et pour pouvoir ajouter un son different