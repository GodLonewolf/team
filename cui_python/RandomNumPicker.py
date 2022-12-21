import random
while True:
    x = input("\nEnter the smallest number: ")
    y = input("Enter the largest number:  ")
    try:
        x = int(x)
        try:
            y = int(y)
            if x < y:
                print("\nYour random number is: ", random.randint(x,y))
            elif x > y:
                print("\nYour random number is: ", random.randint(y,x))
        except:
            print("Enter a valid input!")
    except:
        print("Enter a valid input!")