def multiple():
    L = [8,24,48,2,16]
    resultat = 0
    for i in L:
        if i % 3 == 0 :
            resultat += 1
    print(resultat)

multiple()