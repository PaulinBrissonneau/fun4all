from loader import load
from parser import parse_equation
from scipy.optimize import linprog
import numpy as np
from sympy import *
x, y = symbols('x y')

data = load("fun4all.txt")


#règles:

A = (0,12,12)
B = (13,13,13)
C = (12,21,0)

#comparaison des propositions xi
rules = ["x1>=x4", "x5>=x3", "x2>=x6"]

#rules = parse_rules(rules)

equations2 = []
var = ["x", "y", "(1-x-y)"]
for rule in rules :
    expr = ''
    Lexpr = rule.split(">=")
    for i in range(len(data[Lexpr[0]])) :
        dim = data[Lexpr[0]][i]
        print(dim)
        expr += str(dim)+'*'+str(var[i])+' + '
    expr = expr[:-3]
    expr+=" >= "
    for i in range(len(data[Lexpr[1]])) :
        dim = data[Lexpr[1]][i]
        expr += str(dim)+'*'+str(var[i])+' + '
    expr = expr[:-3]
    equations2.append(expr)
    

equations = ["10*x + 50*y + 70*(1-x-y) >= 30*x + 10*y + 70*(1-x-y)", "60*x + 80*y + 45*(1-x-y) >= 40*x + 90*y + 45*(1-x-y)", "34*x + 56*y + 84*(1-x-y) >= 49*x + 56*y + 54*(1-x-y)"]
print(equations)
equations = equations2


print(equations2)

lhs_ineq2 = []
rhs_ineq2 = []

for eq in equations :
    a = str(simplify(eq))
    left, right = parse_equation(a)
    lhs_ineq2.append(left)
    rhs_ineq2.append(right)

print(lhs_ineq2)
print(rhs_ineq2)

lhs_ineq = lhs_ineq2
rhs_ineq = rhs_ineq2

#ajout de la règle générale w<1/2
lhs_ineq.append([ -1, -1])
rhs_ineq.append(-0.5)

bnd = [(0, 0.5),  # Bounds of x
       (0, 0.5)]


print(data)

#mise en équation
#############################################################################
"""
lhs_ineq = [[ 1,  -2], 
            [-2,  1], 
            [ 3, 2],
            [ -1, -1]] 

rhs_ineq = [0,
            0, 
            2,
            -0.5]"""

  # Bounds of y

#résolution le long des lignes pour trouver les sommets
#####################################################################

sommets = []

directions = lhs_ineq+[list(-np.array(coord)) for coord in lhs_ineq]
print(directions)
for obj in directions :
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,method="revised simplex")
    print(opt.x)
    if list(opt.x) not in sommets:
        sommets.append(list(opt.x))

print(sommets)

#comparaison des vecteurs sur les sommets
#######################################################################

def get_value (sommet, vecteur):
    return sum([sommet[i]*vecteur[i] for i in range(len(sommet))])

for name1, vecteur1 in data.items() :
    for name2, vecteur2 in data.items() :
        #print(name1+' '+name2)
        max_gx_gy = -1
        max_gy_gx = -1
        for sommet in sommets :
            #print(sommet)
            val1 = get_value (sommet, vecteur1)
            val2 = get_value (sommet, vecteur2)
            if val1 - val2 > max_gx_gy : max_gx_gy = val1 - val2
            if val2 - val1 > max_gy_gx : max_gy_gx = val2 - val1
        print("######################")
        if max_gx_gy < 0 :
            print(f"{name1} meilleur que {name2}")
        if max_gy_gx < 0 :
            print(f"{name1} moins bon {name2}")
        if max_gx_gy >= 0 and max_gy_gx >= 0 :
            print(f"{name1} ni pire ni meilleur {name2}")


import matplotlib.pyplot as plt
import math

pp = sommets
cent=(sum([p[0] for p in pp])/len(pp),sum([p[1] for p in pp])/len(pp))
pp.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))

x = [pp[i][0] for i in range(len(sommets))]
y = [pp[i][1] for i in range(len(sommets))]

print(sommets)

#for i in range(len(sommets)) :
#    for j in range(len(sommets)) :
#        plt.plot([sommets[i][0], sommets[j][0]],[sommets[i][1], sommets[j][1]],'k-')

plt.axis('equal')
plt.savefig('polyhedre.png')
#plt.show()



import matplotlib.pyplot as plt
x1 = [3, 6, 6, 3, 3]
y1 = [2, 2, 4, 4, 2]
x2 = [0, 9, 9, 0, 0]
y2 = [0, 0, 6, 6, 0]


plt.fill(x, y, color='black')
plt.show()