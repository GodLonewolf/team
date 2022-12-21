import random, os
print("""
Enter:
R for Rock
P for Paper
S for Scissors
""")
winquotes = ['Adbhhut!', 'Nailed it!', 'Nicee', 'Checkmate!', 'Peekaboo', 'Afterall, we made computers', 'Game Point!']
losequotes = ['Wasted', 'Try again...', 'Life full of unfortunate events', 'Sed life', 'Will AI conquer us?', 'Lol', 'Aa gya swaad?']
userscore = 0
compscore = 0
while True:
    user = input("""
Your Turn: """)
    os.system("cls")
    possible = ["Rock", "Paper", "Scissors"]
    comp = possible[random.randint(0, 2)]
    if (user == 'r') or (user == 'R'):
        r = 'Rock'
        print("""You - {}
Computer - {}""".format(r, comp))
        if comp == 'Rock':
            print('Tied | Score : {}-{}'.format(userscore, compscore))
        elif comp == 'Scissors':
            userscore += 1
            print('{} | Score : {}-{}'.format(winquotes[random.randint(0, 6)], userscore, compscore))
        else:
            compscore += 1
            print('{} | Score : {}-{}'.format(losequotes[random.randint(0, 6)], userscore, compscore))
    elif (user == 'p') or (user == 'P'):
        p = 'Paper'
        print("""You - {}
Computer - {}""".format(p, comp))
        if comp == 'Paper':
            print('Tied | Score : {}-{}'.format(userscore, compscore))
        elif comp == 'Rock':
            userscore += 1
            print('{} | Score : {}-{}'.format(winquotes[random.randint(0, 6)], userscore, compscore))
        else:
            compscore += 1
            print('{} | Score : {}-{}'.format(losequotes[random.randint(0, 6)], userscore, compscore))
    elif (user == 's') or (user == 'S'):
        s = 'Scissors'
        print("""You - {}
Computer - {}""".format(s, comp))
        if comp == 'Scissors':
            print('Tied | Score : {}-{}'.format(userscore, compscore))
        elif comp == 'Paper':
            userscore += 1
            print('{} | Score : {}-{}'.format(winquotes[random.randint(0, 6)], userscore, compscore))
        else:
            compscore += 1
            print('{} | Score : {}-{}'.format(losequotes[random.randint(0, 6)], userscore, compscore))
    else:
        print("Please provide a valid input.")