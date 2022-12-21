while True:
    x = int(input("Enter number: "))
    y,z,l = 0,x,[]
    p = [2048,1024,512,256,128,64,32,16,8,4,2,1]
    for i in range(len(p)):
        if p[i] < z:
            y = i
            break
    while y != 12:
        if p[y] <= z:
            l.append(1)
            z -= p[y]
            y += 1
        else:
            y += 1
            l.append(0)
    print(*l)