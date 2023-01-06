def add1():
    L = [7, 11, 42, 39, 2]
    L2 = []
    cache = 0
    for i in L:
        cache = i+1
        L2.append(cache)
    print(L)
    print(L2)

add1()