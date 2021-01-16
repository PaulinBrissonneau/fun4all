#Paulin Brissonneau - 2021
#Exercice fun4all - systèmes de décision

import matplotlib.pyplot as plt
import math
from loader import load, save
from parser import parse_equation
from scipy.optimize import linprog
import numpy as np
from sympy import *


#init sympy pour les simpification d'équations
x, y = symbols('x y')

#charger les vecteurs (propositions) depuis fun4all.txt
data = load("fun4all.txt")

#comparaison des propositions xi
rules = ["x1>=x4", "x5>=x3", "x2>=x6"]

print(f"Préférences : {rules}\n\n")

#parsing des équations qui modélisent les préférences
equations = []
var = ["x", "y", "(1-x-y)"]
for rule in rules :
    expr = ''
    Lexpr = rule.split(">=")
    for i in range(len(data[Lexpr[0]])) :
        dim = data[Lexpr[0]][i]
        expr += str(dim)+'*'+str(var[i])+' + '
    expr = expr[:-3]
    expr+=" >= "
    for i in range(len(data[Lexpr[1]])) :
        dim = data[Lexpr[1]][i]
        expr += str(dim)+'*'+str(var[i])+' + '
    expr = expr[:-3]
    equations.append(expr)
    
print(f"Equations de préférences : {equations}\n\n")

#simplification des équations et ajout des équations au solveur
lhs_ineq = []
rhs_ineq = []
for eq in equations :
    a = str(simplify(eq))
    left, right = parse_equation(a)
    lhs_ineq.append(left)
    rhs_ineq.append(right)


#ajout de la règle générale w<1/2 (ne dépend pas des entrées, donc elle peut être codée en dur)
lhs_ineq.append([ -1, -1])
rhs_ineq.append(-0.5)
bnd = [(0, 0.5),
       (0, 0.5)]

print(f"Equations du solveur : à gauche : {lhs_ineq} - à droite : {rhs_ineq} - limites {bnd}\n\n")


#résolution des contraintes par le solveur
#pour trouver les sommets facilement, on optimise le problème selon chacun des axes-limites

sommets = []

directions = lhs_ineq+[list(-np.array(coord)) for coord in lhs_ineq]
for obj in directions :
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,method="revised simplex")
    if list(opt.x) not in sommets:
        sommets.append(list(opt.x))

print(f"Sommets du polyhèdre : {sommets}\n\n")

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
        if max_gx_gy < 0 :
            jugement = f"{name1} meilleur que {name2}" 
            print(jugement)
            output.append(jugement+'\n')
        if max_gy_gx < 0 :
            jugement = f"{name1} moins bon {name2}"
            print(jugement)
            output.append(jugement+'\n')
        if max_gx_gy >= 0 and max_gy_gx >= 0 :
            jugement = f"{name1} ni pire ni meilleur que {name2}"
            print(jugement)
            output.append(jugement+'\n')
        print("######################")

save("output.txt", output)

#tri des sommets selon l'argument en coordonnées polaires
cent=(sum([p[0] for p in sommets])/len(sommets),sum([p[1] for p in sommets])/len(sommets))
sommets.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))

#affichage du polyhèdre
x = [sommets[i][0] for i in range(len(sommets))]
y = [sommets[i][1] for i in range(len(sommets))]
plt.fill(x, y, color='black')
plt.axis('equal')
plt.title("Polyhèdre : espace des valeurs acceptables")
plt.savefig('polyhedre.png')
plt.show()
