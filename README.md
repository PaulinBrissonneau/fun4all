# Exercice fun4all
## Paulin Brissonneau - Cours de systèmes de prise de décision

Pour lancer l'aglorithme : ```python fun4all.py```. Il se lancera avec les vecteurs  définis dans ```fun4all.txt``` et les préférences définies à la ligne 14 de ```fun4all.py```. Par défaut, ce sont les valeurs données dans le sujet mais l'algorithme fonctionne pour n'importe quelles préférences et valeurs cohérentes.

Les résultats sont enregistrés dans ```polyhedre.png``` (valeurs possibles des poids) et ```output.txt``` (comparaison des propositions).

#### I - Structure du code :

* défintion des préférences par l'utilisateur
* chargement des vecteurs (propositions) depuis fun4all.txt
* parsing des équations qui modélisent les préférences
* simplification des équations grâce à [Sympy](https://www.sympy.org/en/index.html)
* résolution du problème par le solveur [Scipy.otpimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
* recherche des sommets du polyhèdre
* comparaison de toutes les propositions sur chacun des sommets (algorithme vu en TD)
* affichage du polyhèdre


#### II - Solution des espaces de valeurs acceptables pour les poids (polyhedre.png) :

*Solutions données pour les préférénces définies à la questions c.*

![image polyhèdre](https://raw.githubusercontent.com/PaulinBrissonneau/fun4all/main/polyhedre.png)


#### III - Solution des comparaisons des propositions (output.txt) :

*Solutions données pour les vecteurs du sujet (fun4all.txt) et les préférénces définies à la questions c.*

x1 ni pire ni meilleur que x1

x1 meilleur que x2

x1 meilleur que x3

x1 ni pire ni meilleur que x4

x1 meilleur que x5

x1 meilleur que x6

x1 ni pire ni meilleur que x7

x1 ni pire ni meilleur que x8

x1 meilleur que x9

x1 meilleur que x10

x1 meilleur que x11

x1 meilleur que x12

x2 moins bon que x1

x2 ni pire ni meilleur que x2

x2 meilleur que x3

x2 moins bon que x4

x2 meilleur que x5

x2 meilleur que x6

x2 ni pire ni meilleur que x7

x2 moins bon que x8

x2 meilleur que x9

x2 ni pire ni meilleur que x10

x2 meilleur que x11

x2 ni pire ni meilleur que x12

x3 moins bon que x1

x3 moins bon que x2

x3 ni pire ni meilleur que x3

x3 moins bon que x4

x3 ni pire ni meilleur que x5

x3 moins bon que x6

x3 ni pire ni meilleur que x7

x3 moins bon que x8

x3 ni pire ni meilleur que x9

x3 moins bon que x10

x3 moins bon que x11

x3 moins bon que x12

x4 ni pire ni meilleur que x1

x4 meilleur que x2

x4 meilleur que x3

x4 ni pire ni meilleur que x4

x4 meilleur que x5

x4 meilleur que x6

x4 meilleur que x7

x4 meilleur que x8

x4 meilleur que x9

x4 meilleur que x10

x4 meilleur que x11

x4 meilleur que x12

x5 moins bon que x1

x5 moins bon que x2

x5 ni pire ni meilleur que x3

x5 moins bon que x4

x5 ni pire ni meilleur que x5

x5 moins bon que x6

x5 moins bon que x7

x5 moins bon que x8

x5 moins bon que x9

x5 moins bon que x10

x5 moins bon que x11

x5 moins bon que x12

x6 moins bon que x1

x6 moins bon que x2

x6 meilleur que x3

x6 moins bon que x4

x6 meilleur que x5

x6 ni pire ni meilleur que x6

x6 ni pire ni meilleur que x7

x6 moins bon que x8

x6 meilleur que x9

x6 ni pire ni meilleur que x10

x6 ni pire ni meilleur que x11

x6 ni pire ni meilleur que x12

x7 ni pire ni meilleur que x1

x7 ni pire ni meilleur que x2

x7 ni pire ni meilleur que x3

x7 moins bon que x4

x7 meilleur que x5

x7 ni pire ni meilleur que x6

x7 ni pire ni meilleur que x7

x7 moins bon que x8

x7 ni pire ni meilleur que x9

x7 ni pire ni meilleur que x10

x7 ni pire ni meilleur que x11

x7 ni pire ni meilleur que x12

x8 ni pire ni meilleur que x1

x8 meilleur que x2

x8 meilleur que x3

x8 moins bon que x4

x8 meilleur que x5

x8 meilleur que x6

x8 meilleur que x7

x8 ni pire ni meilleur que x8

x8 meilleur que x9

x8 meilleur que x10

x8 meilleur que x11

x8 meilleur que x12

x9 moins bon que x1

x9 moins bon que x2

x9 ni pire ni meilleur que x3

x9 moins bon que x4

x9 meilleur que x5

x9 moins bon que x6

x9 ni pire ni meilleur que x7

x9 moins bon que x8

x9 ni pire ni meilleur que x9

x9 moins bon que x10

x9 moins bon que x11

x9 moins bon que x12

x10 moins bon que x1

x10 ni pire ni meilleur que x2

x10 meilleur que x3

x10 moins bon que x4

x10 meilleur que x5

x10 ni pire ni meilleur que x6

x10 ni pire ni meilleur que x7

x10 moins bon que x8

x10 meilleur que x9

x10 ni pire ni meilleur que x10

x10 ni pire ni meilleur que x11

x10 moins bon que x12

x11 moins bon que x1

x11 moins bon que x2

x11 meilleur que x3

x11 moins bon que x4

x11 meilleur que x5

x11 ni pire ni meilleur que x6

x11 ni pire ni meilleur que x7

x11 moins bon que x8

x11 meilleur que x9

x11 ni pire ni meilleur que x10

x11 ni pire ni meilleur que x11

x11 moins bon que x12

x12 moins bon que x1

x12 ni pire ni meilleur que x2

x12 meilleur que x3

x12 moins bon que x4

x12 meilleur que x5

x12 ni pire ni meilleur que x6

x12 ni pire ni meilleur que x7

x12 moins bon que x8

x12 meilleur que x9

x12 meilleur que x10

x12 meilleur que x11

x12 ni pire ni meilleur que x12