def chiffrement(str):
    lettres = [*str]
    chifr = [*"abcdefghijklmnopqrstuvwxyz"]
    i = 0
    rangement=[]
    for j in lettres:
        lettres[i] = chifr[(i+3) % 26]
        i += 1
    print(lettres)
    print(chifr)
    for i in str:
        chifr.index(i)
        i+=1

chiffrement("Luke Skywalker un professeur de Math fait passer un test et decide")