import random
import time
print("\nPress 'Enter' to throw dice\nEnter '0' to exit the program\n")
l = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]
print(len(l))
while True:
    a = input("\nPress Enter: ")
    if a == '0':
        print("Exiting...\n")
        time.sleep(.5)
        exit()
    else:
        print("Rolling...")
        time.sleep(random.uniform(.3, .9))
        print("Dice: {}".format(l[random.randint(0, (len(l)-1))]))