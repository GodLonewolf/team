import os
f1 = """\n 1 2 3 4 5 6 7\n║{}│{}│{}│{}│{}│{}│{}║\n║{}│{}│{}│{}│{}│{}│{}║\n║{}│{}│{}│{}│{}│{}│{}║\n║{}│{}│{}│{}│{}│{}│{}║\n║{}│{}│{}│{}│{}│{}│{}║\n║{}│{}│{}│{}│{}│{}│{}║\n╚═╧═╧═╧═╧═╧═╧═╝\n"""
def printmain(): print(f1.format(c1[5],c2[5],c3[5],c4[5],c5[5],c6[5],c7[5],c1[4],c2[4],c3[4],c4[4],c5[4],c6[4],c7[4],c1[3],c2[3],c3[3],c4[3],c5[3],c6[3],c7[3],c1[2],c2[2],c3[2],c4[2],c5[2],c6[2],c7[2],c1[1],c2[1],c3[1],c4[1],c5[1],c6[1],c7[1],c1[0],c2[0],c3[0],c4[0],c5[0],c6[0],c7[0]))
def clear(): os.system('cls')
def checksol():
    for i in range(8):
        for j in range(6):
            if (j > 2) and (c[i][j] == c[i+1][j-1]) and (c[i][j] == c[i+2][j-2]) and (c[i][j] == c[i+3][j-3]) and (c[i][j] != ' '): endgame(i,j)
            elif (c[i][j] == c[i][j+1]) and (c[i][j] == c[i][j+2]) and (c[i][j] == c[i][j+3]) and (c[i][j] != ' '): endgame(i,j)
            elif (c[i][j] == c[i+1][j]) and (c[i][j] == c[i+2][j]) and (c[i][j] == c[i+3][j]) and (c[i][j] != ' '): endgame(i,j)
            elif (c[i][j] == c[i+1][j+1]) and (c[i][j] == c[i+2][j+2]) and (c[i][j] == c[i+3][j+3]) and (c[i][j] != ' '): endgame(i,j)
def endgame(i,j):
    clear()
    printmain()
    print(c[i][j], "wins!")
    input("Enter anything to exit: ")
    exit()
cn1,cn2,cn3,cn4,cn5,cn6,cn7,cn8,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 = 0,0,0,0,0,0,0,0,[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ']
clear()
print("""\nWelcome to 4-in-a-row\n\nHere's how to play this game:\n  ● It is the goal of the game to connect four of your tokens in a line.\n  ● All directions (vertical, horizontal, diagonal) are allowed.\n  ● Players take turns putting one of their tokens into one of the seven slots.\n  ● A token falls down as far as possible within a slot. The player with the red tokens begins.\n  ● The game ends immediately when one player connects four stones.\n\n1. Start new game\n2. Quit\n""")
startgame = input("Enter: ")
c  = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]
while True:
    clear()
    printmain()
    if startgame == '1':
        u1, u2 = '',''
        trueinputs = []
        while u1 not in trueinputs:
            u1 = input("Enter ○: ")
            if u1 == '1':
                c1[cn1] = '○'
                cn1 += 1
                break
            elif u1 == '2':
                c2[cn2] = '○'
                cn2 += 1
                break
            elif u1 == '3':
                c3[cn3] = '○'
                cn3 += 1
                break
            elif u1 == '4':
                c4[cn4] = '○'
                cn4 += 1
                break
            elif u1 == '5':
                c5[cn5] = '○'
                cn5 += 1
                break
            elif u1 == '6':
                c6[cn6] = '○'
                cn6 += 1
                break
            elif u1 == '7':
                c7[cn7] = '○'
                cn7 += 1
                break
            else:
                print("Invalid!")
                continue
        checksol()
        clear()
        printmain()
        while u1 not in trueinputs:
            u1 = input("Enter ●: ")
            if u1 == '1':
                c1[cn1] = '●'
                cn1 += 1
                break
            elif u1 == '2':
                c2[cn2] = '●'
                cn2 += 1
                break
            elif u1 == '3':
                c3[cn3] = '●'
                cn3 += 1
                break
            elif u1 == '4':
                c4[cn4] = '●'
                cn4 += 1
                break
            elif u1 == '5':
                c5[cn5] = '●'
                cn5 += 1
                break
            elif u1 == '6':
                c6[cn6] = '●'
                cn6 += 1
                break
            elif u1 == '7':
                c7[cn7] = '●'
                cn7 += 1
                break
            else:
                print("Invalid!")
                continue
        checksol()
    elif startgame == '2': exit()
    else: print("Invalid!")