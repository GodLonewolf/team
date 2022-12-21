while True:
    x = list(input("Enter binary: "))
    x.reverse()
    z = 0
    for i in range(len(x)):
        if x[i] == '1':
            z += 2 ** i
    print(z)
