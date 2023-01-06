def doublon():
    list = [10,20,30,20,10,50,60,40,80,50,40]
    n = 0
    list2=[]

    for i in list:
       if i not in list2:
           list2 += [i]
    for i in list2:
        n += 1
    for i in range(0, n):
            for j in range(i, n):
                if list2[i] > list2[j]:
                    list2[i], list2[j] = list2[j], list2[i]
    print(list2)

doublon()