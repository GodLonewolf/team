import random, time, os
print("""
Enter the number where you want to mark your 'X':

 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 

Computer will mark 'O'.
""")
format = """
  {} | {} | {} 
 ---+---+---
  {} | {} | {}
 ---+---+---
  {} | {} | {}"""
npa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
npna = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
while len(npa) != 0:
    user = str(input("""
Enter: """))
    if user in npa:
        npa[int(user) - 1] = ' '
        npna[int(user) - 1] = 'X'
        os.system('cls')
        print(format.format(npna[0], npna[1], npna[2], npna[3], npna[4], npna[5], npna[6], npna[7], npna[8]))
        if npna[0] == npna[1] and npna[1] == npna[2] and npna[2] != ' ':
            if npna[0] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[3] == npna[4] and npna[4] == npna[5] and npna[5] != ' ':
            if npna[3] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[6] == npna[7] and npna[7] == npna[8] and npna[8] != ' ':
            if npna[6] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[0] == npna[3] and npna[3] == npna[6] and npna[6] != ' ':
            if npna[0] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[1] == npna[4] and npna[4] == npna[7] and npna[7] != ' ':
            if npna[1] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[2] == npna[5] and npna[5] == npna[8] and npna[8] != ' ':
            if npna[2] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[0] == npna[4] and npna[4] == npna[8] and npna[8] != ' ':
            if npna[0] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        elif npna[2] == npna[4] and npna[4] == npna[6] and npna[6] != ' ':
            if npna[2] == 'X':
                print('You won!')
                exit()
            else:
                print('Better luck next time...')
                exit()
        comp = 9
        if npna[0] != ' ' and npna[1] != ' ' and npna[2] != ' ' and npna[3] != ' ' and npna[4] != ' ' and npna[5] != ' ' and npna[6] != ' ' and npna[7] != ' ' and npna[8] != ' ':
            print("Tied")
            exit()
        else:
            print("""Computer is thinking...
            """)
            time.sleep(random.uniform(0, 3))
            while npa[comp] == ' ':
                comp = random.randint(0, 8)
            npa[comp] = ' '
            npna[comp] = 'O'
        os.system('cls')
        print(format.format(npna[0], npna[1], npna[2], npna[3], npna[4], npna[5], npna[6], npna[7], npna[8]))
    else:
        print("Please provide a valid input.")