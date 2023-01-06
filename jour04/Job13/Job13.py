def doublon():
    list = [10,20,30,20,10,50,60,40,80,50,40]
    n = 0
    list2=[]
    for i in list:
        n += 1
    for i in range(0, n):
        for j in range(i, n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
        for i in range(0, n):
            for j in range(i, n):
                if list[i] == list[j]:
                    list[i] = list2
        print(list)
    print(list2)

doublon()