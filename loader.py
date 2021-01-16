def load(file) :

    with open(file, "r") as f :
        L = f.readlines()

    for i in range(len(L)):
        L[i] = L[i].replace('\n', '')

    data = {}
    step = 13
    for i in range (12) :
        data[L[i]] = [int(L[i+step]), int(L[i+2*step]), int(L[i+3*step])]

    return data