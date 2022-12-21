while True:
    a = int(input("A num: "))
    if a < 0:
        print("Error...")
    else:
        b = 1
        for i in range(1,a):
            b = b * ( i + 1 )
        print(b)