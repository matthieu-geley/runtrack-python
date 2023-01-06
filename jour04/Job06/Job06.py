def entier():
    L = [5, 6, 85, 215, 452, 10, 525562]
    exc = L[0]
    L[0]=L[-1]
    L[-1]=exc
    print(L)

entier()