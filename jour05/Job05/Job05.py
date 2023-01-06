def phare(nb,taille):
    dist = nb*taille*10
    Dsem = dist*7
    Conv = Dsem/100
    print("Pour",nb,"marches de",taille,"centimètres, le gardien du phare parcourt:",Conv,"mètres par semaines")

phare(25,5)