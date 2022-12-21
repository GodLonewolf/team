while True:
    a = int(input("\nEnter a number: "))
    b = 0
    if ( a == 1 ) or ( a == 0 ):
        print("{} is neither prime nor composite.".format(a))
        continue
    else:
        for i in range(2, a-1):
            if a % i == 0:
                b = 1
    if b == 0:
        print("{} is a prime number.".format(a))
    elif b == 1:
        print("{} is not a prime number.".format(a))