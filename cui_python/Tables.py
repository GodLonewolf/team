while True:
    a = int(input("\nEnter the number for which you want the table: "))
    for i in range(1, int(input("Enter upto which number you want to multiply:: "))+1): print("{} x {} = {}".format(a,i,a*i)) 