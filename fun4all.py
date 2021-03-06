#Paulin Brissonneau - 2021
#Exercice fun4all - systèmes de décision

import matplotlib.pyplot as plt
import math
from loader import load, save
from scipy.optimize import linprog
import numpy as np
import sys

###############################################
#PARTIE A MODIFIER POUR DEFINIR LES PREFERENCES
#il faut respecter la syntaxe xi>=xj
pref = ["x1>=x4", "x5>=x3", "x2>=x6"]
#pref = ["x5>=x2", "x7>=x6", "x3>=x11", "x9>=x10"]
#pref = ['x2>=x4', 'x5>=x3', 'x2>=x6']
#pref = ['x3>=x4', 'x5>=x3', 'x2>=x6']
#pref = ['x5>=x4', 'x5>=x3', 'x2>=x6']
###############################################

#charger les vecteurs (propositions) depuis fun4all.txt
data = load("fun4all.txt")

print(f"Préférences : {pref}\n\n")

#construction du système linéaire à résoudre par le solveur
lhs_ineq = []
rhs_ineq = []

for rule in pref :
    Lexpr = rule.split(">=")
    data_left = data[str(Lexpr[0])]
    data_right = data[str(Lexpr[1])]
    
    left = [data_right[0]-data_left[0]-data_right[2]+data_left[2], data_right[1]-data_left[1]-data_right[2]+data_left[2]]
    right = data_left[2]-data_right[2]

    lhs_ineq.append(left)
    rhs_ineq.append(right)


#ajout de la règle générale w<1/2 (ne dépend pas des entrées, donc elle peut être codée en dur)
lhs_ineq.append([ -1, -1])
rhs_ineq.append(-0.5)
bnd = [(0, 0.5),
       (0, 0.5)]

print(f"Equations du solveur : à gauche : {lhs_ineq} - à droite : {rhs_ineq} - limites {bnd}\n\n")


#résolution des contraintes par le solveur
#pour trouver les sommets facilement, on optimise le problème selon chacun des axes-frontières du polyèdre

sommets = []

directions = lhs_ineq+[list(-np.array(coord)) for coord in lhs_ineq]
for obj in directions :
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,method="revised simplex")
    if list(opt.x) not in sommets:
        sommets.append(list(opt.x))

if len(sommets) <= 2 :
    print("Pas de solution : polyèdre vide")
    sys.exit()

#on ajoute le poids w3 calculé à partir de w1 et w2
for sommet in sommets :
    sommet.append(1-sommet[0]-sommet[1])

print(f"Sommets du polyèdre : {sommets}\n\n")

#comparaison de toutes les propositions sur chacun des sommets
#on applique l'algorithme vu en TD

def get_value (sommet, vecteur):
    return sum([sommet[i]*vecteur[i] for i in range(len(sommet))])

output = []

print("Préférences sur tous les vecteurs :\n")
for name1, vecteur1 in data.items() :
    for name2, vecteur2 in data.items() :
        max_gx_gy = -1
        max_gy_gx = -1
        for sommet in sommets :
            val1 = get_value (sommet, vecteur1)
            val2 = get_value (sommet, vecteur2)
            if val1 - val2 > max_gx_gy : max_gx_gy = val1 - val2
            if val2 - val1 > max_gy_gx : max_gy_gx = val2 - val1
        #si le max est négatif, alors x est moins bon partout sur le polyèdre
        if max_gx_gy < 0 :
            jugement = f"{name1} moins bon que {name2}"
            print(jugement)
            output.append(jugement+'\n\n')
        #si le max est négatif, alors y est moins bon partout sur le polyèdre
        if max_gy_gx < 0 :
            jugement = f"{name1} meilleur que {name2}" 
            print(jugement)
            output.append(jugement+'\n\n')
        #si les deux max sont positifs, alors on ne peut rien dire
        if max_gx_gy >= 0 and max_gy_gx >= 0 :
            jugement = f"{name1} ne peut pas être comparé à {name2}"
            print(jugement)
            output.append(jugement+'\n\n')
        print("######################")


########################
# NOTE sur cette fonction : on peut mettre des inégalités larges.
# Cela transformerait les comparaisons de type "est meilleur que" en "est au moins aussi bon que".
# Cela correspondrait avec la façon dont les préférences sont données. En particulier, on pourrait inférer "x1 au moins aussi bon que x4", ce qui est donné dans les préférences.
# Comme la correction de l'exercice propose de garder des inégalités strictes, on les garde pour le programme. Mais on perd l'information que "x1 au moins aussi bon que x4", par exemple.
########################

save("output.txt", output)

#tri des sommets selon l'argument en coordonnées polaires
cent=(sum([p[0] for p in sommets])/len(sommets),sum([p[1] for p in sommets])/len(sommets))
sommets.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))

#affichage du polyèdre
x = [sommets[i][0] for i in range(len(sommets))]
y = [sommets[i][1] for i in range(len(sommets))]
plt.fill(x, y, color='black')
plt.axis('equal')
plt.title(f"polyèdre : espace des valeurs acceptables\navec préférences : {pref}")
plt.savefig(f'polyedre.png')