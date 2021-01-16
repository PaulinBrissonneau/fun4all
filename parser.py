from sympy import *

def clean(expr) :
    expr = expr.replace("*", '').replace("x", '').replace("y", '').replace("+", '')
    if '/' in expr :
        a = expr.split('/')
        if '-' in a[0] : return -float(a[0][1:])/float([1])
        else : return float(a[0])/float(a[1])

    if expr == '' : return 1
    if expr == '-' : return -1
    else : return float(expr)

def parse_equation(eq) :

    print(eq)

    left = [None, None]
    right = None
    split = eq.split(' ')
    delimiter = False
    for term in split :
        if "<" in term or ">" in term :
            delimiter = True
        elif "x" not in term and "y" not in term :
            if not delimiter or '>' in eq :
                if not delimiter and '>' in eq : right = clean(term)
                else : right = -clean(term)
            else : right = clean(term)
        elif "x" in term :
            if delimiter or '>' in eq :
                if delimiter and '>' in eq : left[0] = clean(term)
                else : left[0] = -clean(term)
            else : left[0] = clean(term)
        elif "y" in term :
            if delimiter or '>' in eq :
                if delimiter and '>' in eq : left[1] = clean(term)
                else : left[1] = -clean(term)
            else : left[1] = clean(term)
        else : pass
    if right == None : right = 0
    return left, right