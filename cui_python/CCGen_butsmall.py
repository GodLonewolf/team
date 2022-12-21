import random
bin = int(input("BIN: "))
for i in range(int(input("Quantity: "))):
    odd, even, x, sc = [], [], 0, str(bin*1000000000+random.randint(100000000, 999999999))
    for i in range(len(sc)): even.append(int(sc[i])*2) if i % 2 == 0 else odd.append(int(sc[i]))
    for i in range(len(even)): odd.append(int(str(even[i])[0]) + int(str(even[i])[1])) if even[i] > 9 else odd.append(even[i])
    for i in odd: x += i
    print(sc+str(10 - int(str(x)[-1]))[-1]+'|{}|{}|{}'.format(str(random.randint(1,13)).zfill(2), random.randint(2023, 2028), str(random.randint(0, 999)).zfill(3)))