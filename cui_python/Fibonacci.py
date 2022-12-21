import os
while True:
    x = int(input("\nEnter a number: "))
    y = int(input("Enter another number: "))
    z = int(input("How many times do you want to repeat: "))
    l = []
    for i in range(z):
        l.append(x)
        l.append(y)
        x = x + y
        y = x + y
    for i in range(int(len(l)/2)):
        print("{}  ".format(l[i]), end = '')
    os.system("cls")