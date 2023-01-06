def tri(list):
    n = 0
    for i in list:
        n += 1
    for i in range(0, n):
            for j in range(i, n):
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
    print(list)

tri([41, 135, 3, 4, 17, 51, 2554, 356, 1])