import random

def closest_tens(t):
    if str(t)[-1] == '0':
        return '0'
    elif str(t)[-1] == '1':
        return '9'
    elif str(t)[-1] == '2':
        return '8'
    elif str(t)[-1] == '3':
        return '7'
    elif str(t)[-1] == '4':
        return '6'
    elif str(t)[-1] == '5':
        return '5'
    elif str(t)[-1] == '6':
        return '4'
    elif str(t)[-1] == '7':
        return '3'
    elif str(t)[-1] == '8':
        return '2'
    elif str(t)[-1] == '9':
        return '1'

quantity = int(input("Quantity: "))
bin = int(input("BIN: "))
for i in range(quantity):
    cc = bin*1000000000+random.randint(100000000, 999999999)
    sc = str(cc)
    odd, even, x = [], [], 0
    for i in range(len(sc)):
        if i % 2 == 0:
            even.append(int(sc[i])*2)
        else:
            odd.append(int(sc[i]))
    for i in range(len(even)):
        if even[i] > 9:
            even[i] = int(str(even[i])[0]) + int(str(even[i])[1])
        odd.append(even[i])
    for i in odd:
        x += i
    sc += closest_tens(x)
    print(sc)