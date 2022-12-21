import random
chars = ['!', '@', '#', '$', '%', '&', '!', '@', '#', '$', '%', '&', '!', '@', '#', '$', '%', '&', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
print("\nEnter the length of the password\nEnter 0 to exit\n")
def PasswordGen():
    while True:
        password = []
        length = input("Length:   ")
        if length != '0':
            try:
                length = int(length)
                for i in  range(length):
                    password.append(random.choice(chars))
                print("Password: ", end='')
                for i in range(len(password)):
                    print(password[i], end='')
                print("\n")
            except:
                print("Enter a valid input!\n")
        else:
            exit()
PasswordGen()