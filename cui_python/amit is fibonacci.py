a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
x = int(input("enter the number of times to repeat: "))
l = [a,b]
for i in range(x):
    c = l[-2] + l[-1]
    l.append(c)
for i in l:
    print(i, ', ', end='')
