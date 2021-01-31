# Exercice fun4all
## Paulin Brissonneau - Cours de systèmes de prise de décision

[ Si besoin, tout le contenu du .zip rendu sur Edunao est aussi disponible ici : https://github.com/PaulinBrissonneau/fun4all ]

Pour lancer l'aglorithme : ```python fun4all.py```. Il se lancera avec les vecteurs  définis dans ```fun4all.txt``` et les préférences définies à la ligne 14 de ```fun4all.py```. Par défaut, ce sont les valeurs données dans le sujet mais l'algorithme fonctionne pour n'importe quelles préférences et valeurs cohérentes. Si le polyèdre est vide, l'algorithme retournera "Pas de solution : polyèdre vide".

Les résultats sont enregistrés dans ```polyedre.png``` (valeurs possibles des poids) et ```output.txt``` (comparaison des propositions).

NOTE :
Pour comparer les vecteurs sur les sommets du polyèdres, on peut mettre des inégalités larges (lignes 91 et 96 de fun4all.py). Cela transformerait les comparaisons de type "est meilleur que" en "est au moins aussi bon que". Cela correspondrait avec la façon dont les préférences sont données. En particulier, on pourrait inférer "x1 au moins aussi bon que x4", ce qui est donné dans les préférences. Comme la correction de l'exercice propose de garder des inégalités strictes, on les garde pour le programme. Mais on perd l'information que "x1 au moins aussi bon que x4", par exemple.


#### I - Requirements :

En plus des classiques :
> matplotlib et numpy

J'utilise le solveur :
> scipy.optimize :  `pip install scipy`


#### II - Structure du code :

* définition des préférences par l'utilisateur
* chargement des vecteurs (propositions) depuis fun4all.txt
* construction du système linéaire à résoudre par le solveur
* résolution du problème par le solveur [Scipy.otpimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
* recherche des sommets du polyèdre
* comparaison de toutes les propositions sur chacun des sommets (algorithme vu en TD)
* affichage du polyèdre


#### III - Solution des espaces de valeurs acceptables pour les poids (polyedre.png) :

*Solutions données pour les préférénces définies à la questions c (["x1>=x4", "x5>=x3", "x2>=x6"]).*

![image polyèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/polyedre.png)


*Exemples d'autres solutions avec des préférences différentes*

![image polyèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/exemples/polyedre_x2>=x4_x5>=x3_x2>=x6.png)

![image polyèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/exemples/polyedre_x3>=x4_x5>=x3_x2>=x6.png)

![image polyèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/exemples/polyedre_x5>=x4_x5>=x3_x2>=x6.png)

![image polyèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/exemples/polyedre_x5>=x2_x7>=x6_x3>=x11_x9>=x10.png)

#### IV - Solution des comparaisons des propositions (output.txt) :

*Solutions données pour les vecteurs du sujet (fun4all.txt) et les préférénces définies à la questions c.*

x1 ne peut pas être comparé à x1

x1 moins bon que x2

x1 moins bon que x3

x1 ne peut pas être comparé à x4

x1 moins bon que x5

x1 moins bon que x6

x1 ne peut pas être comparé à x7

x1 ne peut pas être comparé à x8

x1 ne peut pas être comparé à x9

x1 ne peut pas être comparé à x10

x1 ne peut pas être comparé à x11

x1 ne peut pas être comparé à x12

x2 meilleur que x1

x2 ne peut pas être comparé à x2

x2 ne peut pas être comparé à x3

x2 meilleur que x4

x2 ne peut pas être comparé à x5

x2 ne peut pas être comparé à x6

x2 ne peut pas être comparé à x7

x2 meilleur que x8

x2 ne peut pas être comparé à x9

x2 ne peut pas être comparé à x10

x2 ne peut pas être comparé à x11

x2 meilleur que x12

x3 meilleur que x1

x3 ne peut pas être comparé à x2

x3 ne peut pas être comparé à x3

x3 meilleur que x4

x3 ne peut pas être comparé à x5

x3 ne peut pas être comparé à x6

x3 ne peut pas être comparé à x7

x3 ne peut pas être comparé à x8

x3 meilleur que x9

x3 meilleur que x10

x3 meilleur que x11

x3 meilleur que x12

x4 ne peut pas être comparé à x1

x4 moins bon que x2

x4 moins bon que x3

x4 ne peut pas être comparé à x4

x4 moins bon que x5

x4 moins bon que x6

x4 ne peut pas être comparé à x7

x4 moins bon que x8

x4 ne peut pas être comparé à x9

x4 ne peut pas être comparé à x10

x4 moins bon que x11

x4 ne peut pas être comparé à x12

x5 meilleur que x1

x5 ne peut pas être comparé à x2

x5 ne peut pas être comparé à x3

x5 meilleur que x4

x5 ne peut pas être comparé à x5

x5 meilleur que x6

x5 meilleur que x7

x5 meilleur que x8

x5 meilleur que x9

x5 meilleur que x10

x5 meilleur que x11

x5 meilleur que x12

x6 meilleur que x1

x6 ne peut pas être comparé à x2

x6 ne peut pas être comparé à x3

x6 meilleur que x4

x6 moins bon que x5

x6 ne peut pas être comparé à x6

x6 ne peut pas être comparé à x7

x6 ne peut pas être comparé à x8

x6 ne peut pas être comparé à x9

x6 ne peut pas être comparé à x10

x6 ne peut pas être comparé à x11

x6 meilleur que x12

x7 ne peut pas être comparé à x1

x7 ne peut pas être comparé à x2

x7 ne peut pas être comparé à x3

x7 ne peut pas être comparé à x4

x7 moins bon que x5

x7 ne peut pas être comparé à x6

x7 ne peut pas être comparé à x7

x7 ne peut pas être comparé à x8

x7 ne peut pas être comparé à x9

x7 ne peut pas être comparé à x10

x7 ne peut pas être comparé à x11

x7 ne peut pas être comparé à x12

x8 ne peut pas être comparé à x1

x8 moins bon que x2

x8 ne peut pas être comparé à x3

x8 meilleur que x4

x8 moins bon que x5

x8 ne peut pas être comparé à x6

x8 ne peut pas être comparé à x7

x8 ne peut pas être comparé à x8

x8 ne peut pas être comparé à x9

x8 ne peut pas être comparé à x10

x8 ne peut pas être comparé à x11

x8 ne peut pas être comparé à x12

x9 ne peut pas être comparé à x1

x9 ne peut pas être comparé à x2

x9 moins bon que x3

x9 ne peut pas être comparé à x4

x9 moins bon que x5

x9 ne peut pas être comparé à x6

x9 ne peut pas être comparé à x7

x9 ne peut pas être comparé à x8

x9 ne peut pas être comparé à x9

x9 meilleur que x10

x9 ne peut pas être comparé à x11

x9 meilleur que x12

x10 ne peut pas être comparé à x1

x10 ne peut pas être comparé à x2

x10 moins bon que x3

x10 ne peut pas être comparé à x4

x10 moins bon que x5

x10 ne peut pas être comparé à x6

x10 ne peut pas être comparé à x7

x10 ne peut pas être comparé à x8

x10 moins bon que x9

x10 ne peut pas être comparé à x10

x10 ne peut pas être comparé à x11

x10 ne peut pas être comparé à x12

x11 ne peut pas être comparé à x1

x11 ne peut pas être comparé à x2

x11 moins bon que x3

x11 meilleur que x4

x11 moins bon que x5

x11 ne peut pas être comparé à x6

x11 ne peut pas être comparé à x7

x11 ne peut pas être comparé à x8

x11 ne peut pas être comparé à x9

x11 ne peut pas être comparé à x10

x11 ne peut pas être comparé à x11

x11 meilleur que x12

x12 ne peut pas être comparé à x1

x12 moins bon que x2

x12 moins bon que x3

x12 ne peut pas être comparé à x4

x12 moins bon que x5

x12 moins bon que x6

x12 ne peut pas être comparé à x7

x12 ne peut pas être comparé à x8

x12 moins bon que x9

x12 ne peut pas être comparé à x10

x12 moins bon que x11

x12 ne peut pas être comparé à x12
