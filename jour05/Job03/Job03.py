def draw_rectangle(width):
    bord = "+"
    for i in range(width + 1):
        bord += "-"
    bord += "+"
    print(bord)
    for i in range(width + 1):
        tapis = ""
        for j in range(width - i):
            tapis += "#"
        tapis += " "
        for j in range(i):
            tapis += "#"
        print("|" + tapis + "|")
    print(bord)

draw_rectangle(10)