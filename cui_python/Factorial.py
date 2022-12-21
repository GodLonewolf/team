while True:
    a = int(input("A num: "))
    b = 1
    while True:
        if a == 0:
            break
        elif a < 0:
            b = str("Error")
            break
        else:
            b = b * a
            a -= 1
    print(b)