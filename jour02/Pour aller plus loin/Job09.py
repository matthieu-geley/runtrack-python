def triangle(a, b, c):
    print("on considère C comme étant le plus grand coté")
    if a+b >= c:
        if a*a+b*b == c*c:
            print("triangle rectangle")
            if a == b or b == c or a == c:
                print("triangle rectangle isocèle")
        elif a == b or b == c or a == c:
                print("triangle isocèle")
        elif a == b == c:
            print("triangle équilatéral")
        else:
            print("triangle quelconque")
    else:
        print("triangle non-réalisable")

triangle(3,4,5)
triangle(2,2,2)
triangle(4,3,8)