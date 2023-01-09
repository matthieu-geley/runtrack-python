def chiffrement(str):
    split_str = ""
    lettr = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < len(str):
        j = 0
        while j < len(lettr):
            if str[i].lower() == lettr[j]:
                split_str += lettr[(j + 3) % len(lettr)]
            j += 1

        i += 1
    print(split_str)

chiffrement("abcdefghijklmnopqrstuvwxyz")
chiffrement("ceci est un message sous chiffrage")