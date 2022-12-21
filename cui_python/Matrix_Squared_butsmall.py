o, l, s, lmax, smax = int(input("Order: ")), [], [], 0, 0 
for i in range(o):
    l1 = []
    for j in range(o): l1.append(int(input(f"a[{i+1}][{j+1}]: ")))
    l.append(l1)
for i in range(o):
    for j in range(o):
        if len(str(l[i][j])) > lmax: lmax = len(str(l[i][j]))
for i in range(o):
    p = []
    for j in range(o):
        x, y = 0, 0
        for k in range(o): x, y = x+(l[y][j]*l[i][y]), y+1
        p.append(x)
    s.append(p)
for i in range(o):
    for j in range(o):
        if len(str(s[i][j])) > smax: smax = len(str(s[i][j]))
msp, mlp = ' '*(smax*o) + ' '*(o+1), ' '*(lmax*o) + ' '*(o+1)
print(f"┌{mlp}┐\n│", end='')
for i in range(o):
    for j in range(o): print(" {}".format(str(l[i][j]).zfill(lmax)), end='')
    print(" │\n│", end='') if i != o-1 else print(" │")
print(f"└{mlp}┘\n┌{msp}┐\n│", end='')
for i in range(o):
    for j in range(o): print(" {}".format(str(s[i][j]).zfill(smax)), end='')
    print(" │\n│", end='') if i != o-1 else print(" │")
print(f"└{msp}┘")