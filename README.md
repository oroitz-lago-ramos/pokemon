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
//Gerer bien le pokedex et la generation aleatoires de pokemon ennemis
//ecran de selection de pokemon
//affichage scroll pokedex
//heredité pour diferencier ennemi ou player pokemon?
//demander aux autres si on fusionne les json pokemon et pokedex
implementer xp et evolution (dans le json attribut evolu et passe a l'id suivant)
modifier l'attaque et la defense et la vie en focntion du niveau (grace init pokemon)
degats critiques et louper attaque
que le message du pokemon attaque vienne apres que les degats aient ete réalisés
Recuperer la valeur du multiplicateur pour afficher un message personnalisé et pour pouvoir ajouter un son different
Message de fin annuler l'attaque de celui qui a perdu (ajouter un nouveau state pour afficher le message)
Ajout bouton pour commencer une nouvelle partie
//Ajout bouton qui debloque automatiquement pokemon
Mettre a jour type-chart
Modifier comment le jeu gere la defense afin que les combats soient moins longs