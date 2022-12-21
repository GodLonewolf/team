o1 = int(input("Number of rows    of Matrix A: "))
o2 = int(input("Number of columns of Matrix A: "))
o3 = o2
print("Number of rows    of Matrix B:", o3)
o4 = int(input("Number of columns of Matrix B: "))

a = []
b = []
s = []

print()
for i in range(o1):
    t = []
    for j in range(o2):
        t.append(int(input(f"Enter a[{i}][{j}]: ")))
    a.append(t)
print()
for i in range(o3):
    t = []
    for j in range(o4):
        t.append(int(input(f"Enter b[{i}][{j}]: ")))
    b.append(t)

for i in range(o1):
    p = []
    for j in range(o4):
        x, y = 0, 0
        for k in range(o3):
            x += b[y][j]*a[i][y]
            y += 1
        p.append(x)
    s.append(p)

smax = 0
for i in range(o1):
    for j in range(o4):
        if len(str(s[i][j])) > smax:
            smax = len(str(s[i][j]))
msp = ' '*(smax*o4) + ' '*(o4+1)

print(f"\n┌{msp}┐", end='')
print("\n│", end='')
for i in range(o1):
    for j in range(o4):
        print(" {}".format(str(s[i][j]).zfill(smax)), end='')
    if i != o1-1:
        print(" │\n│", end='')
    else:
        print(" │")
print(f"└{msp}┘")