from getpass import getpass
r = ['q', 'r', 'u', 'p', 'd', 'h', 'l', 'c', 'n']
p = ['w', 't', 'i', 'a', 'f', 'j', 'z', 'v', 'm']
s = ['e', 'y', 'o', 's', 'g', 'k', 'x', 'b']
score = [0,0]
while True:
    print('''Enter one of the letters fron the list respecting your desired input:
Rock - q, r, u, p, d, h, l, c, n
Paper - w, t, i, a, f, j, z, v, m
Scissors - e, y, o, s, g, k, x, b
''')
    p1 = getpass("Enter: ")
    p2 = getpass("Enter: ")
    if p1 in r and p2 in p:
        print("Player 2 won! Paper beats Rock!")
        score[1] += 1
    elif p1 in r and p2 in s:
        print("Player 1 won! Rock beats Scissors!")
        score[0] += 1
    elif p1 in p and p2 in s:
        print("Player 2 won! Scissors beats Paper!")
        score[1] += 1
    elif p1 in p and p2 in r:
        print("Player 1 won! Paper beats Rock!")
        score[0] += 1
    elif p1 in s and p2 in p:
        print("Player 1 won! Scissors beats Paper!")
        score[0] += 1
    elif p1 in s and p2 in r:
        print("Player 2 won! Rock beats Scissors!")
        score[1] += 1
    elif p1 in r and p2 in r:
        print('Tied! Both picked Rock')
    elif p1 in p and p2 in p:
        print('Tied! Both picked Paper')
    elif p1 in s and p2 in s:
        print('Tied! Both picked Scissors')
    else:
        print('A fool entered invalid input!')
    print(f"Current score - {score[0]}-{score[1]}\n")