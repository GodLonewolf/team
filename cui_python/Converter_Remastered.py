import time, os
while True:
    print("""\nPhysical Quantities: \n1. Temperature\n2. Currency\n3. Length\n4. Area\n5. Volume\n0. To exit""")        #Main Menu of Convertible Quantities
    r1 = input("\nEnter a number from the unit list: ")
    os.system("cls")
    if r1 == '1':                                                                                                       #Temperature Section                      
        while True:
            print("\nList of Temperature units: \n1. Celcius\n2. Farenhite\n3. Kelvin\n0. To Main Menu")  
            r2 = input("\nEnter a number from the temperature unit list: ")
            os.system("cls")
            if r2 == '1':
                c = float(input("Enter the value in °C: "))
                f = ((9 / 5) * c ) + 32
                k = c + 273.15
                print("\n{}°C = {}°F\n{}°C = {}k".format(int(c), f, int(c), k))
            elif r2 == '2':
                f = float(input("Enter the value in °F: "))
                c = (f - 32) * (5 / 9)
                k = c + 273.15
                print("\n{}°F = {}°C\n{}°F = {}k".format(int(f), c, int(f), k))
            elif r2 == '3':
                k = float(input("Enter the value in k: "))
                c = k - 273.15
                f = ((9 / 5) * c ) + 32
                print("\n{}k = {}°C\n{}k = {}°F".format(int(k), c, int(k), f))
            elif r2 == '0':
                break
            else:
                print("Input invalid!")
    elif r1 == '2':                                                                                                     #Currencies Section
        while True:
            print("\nList of Currencies [As of 4th October 2021]: \n1. INR - Indian Rupee\n2. USD - United States Dollar\n3. GBP - United Kingdom Pound\n4. JPY - Japanese Yen\n5. EUR - Euro\n6. BTC - Bitcoin [Average taken to be US$47000]\n0. To Main Menu")
            r2 = input("\nEnter a number from the currency list: ")
            os.system("cls")
            if r2 == '1':
                inr = float(input("Enter the value in INR: "))
                usd = inr * 0.0134
                gbp = inr * 0.00987
                jpy = inr * 1.491
                eur = inr * 0.01156
                btc = inr * 2.858 * (10**(-7))
                print("\n{} INR\n{} USD\n{} GBP\n{} JPY\n{} EUR\n{} BTC\n".format(inr,usd,gbp,jpy,eur,btc))
            elif r2 == '2':
                usd = float(input("Enter the value in USD: "))
                inr = usd * 74.423
                gbp = usd * 0.7352
                jpy = usd * 110.940
                eur = usd * 0.861
                btc = usd * 2.127 * (10**(-5))
                print("\n{} USD\n{} INR\n{} GBP\n{} JPY\n{} EUR\n{} BTC\n".format(usd,inr,gbp,jpy,eur,btc))
            elif r2 == '3':
                gbp = float(input("Enter the value in GBP: "))
                inr = gbp * 101.2282
                usd = gbp * 1.3601
                jpy = gbp * 150.8977
                eur = gbp * 1.1707
                btc = gbp * 2.894 * (10**(-5))
                print("\n{} GBP\n{} INR\n{} USD\n{} JPY\n{} EUR\n{} BTC\n".format(gbp,inr,usd,jpy,eur,btc))
            elif r2 == '4':
                jpy = float(input("Enter the value in JPY: "))
                inr = jpy * 0.0671
                usd = jpy * 0.0090
                gbp = jpy * 0.0066
                eur = jpy * 0.00775
                btc = jpy * 1.917847  * (10**(-7))
                print("\n{} JPY\n{} INR\n{} USD\n{} GBP\n{} EUR\n{} BTC\n".format(jpy,inr,usd,gbp,eur,btc))
            elif r2 == '5':
                eur = float(input("Enter the value in EUR: "))
                inr = eur * 86.468
                usd = eur * 1.1618
                gbp = eur * 0.8542
                jpy = eur * 128.895085
                btc = eur * 2.47115  * (10**(-5))
                print("\n{} EUR\n{} INR\n{} USD\n{} GBP\n{} JPY\n{} BTC\n".format(eur,inr,usd,gbp,jpy,btc))
            elif r2 == '6':
                btc = float(input("Enter the value in BTC: "))
                inr = btc * 3497881
                usd = btc * 47000
                gbp = btc * 34555
                jpy = btc * 5214180
                eur = btc * 40467
                print("\n{} BTC\n{} INR\n{} USD\n{} GBP\n{} JPY\n{} EUR\n".format(btc,inr,usd,gbp,jpy,eur))
            elif r2 == '0':
                break
    elif r1 == '3':                                                                                                     #Length Section
        while True:
            print("\nList of Length units: \n1. Meters\n2. Inches\n3. Feet\n4. Yards\n5. Miles\n0. To Main Menu")
            r2 = input("Enter a number from the length units list: ")
            os.system("cls")
            if r2 == '1':
                m = float(input("Enter value in meters: "))
                i = m * 39.37008
                f = m * 3.28084
                y = m * 1.093613
                l = m * 0.000621371
                print("\n{} Meters\n{} Inches\n{} Feet\n{} Yards\n{} Miles\n".format(m,i,f,y,l))
            elif r2 == '2':
                i = float(input("Enter value in inches: "))
                m = i * 0.0254
                f = i * 0.083333
                y = i * 0.027778
                l = i * 0.000015782828
                print("\n{} Inches\n{} Meters\n{} Feet\n{} Yards\n{} Miles\n".format(i,m,f,y,l))
            elif r2 == '3':
                f = float(input("Enter value in feet: "))
                m = f * 0.3048
                i = f * 12
                y = f * 0.3334
                l = f * 0.0001893
                print("\n{} Feet\n{} Meters\n{} Inches\n{} Yards\n{} Miles\n".format(f,m,i,y,l))
            elif r2 == '4':
                y = float(input("Enter value in yards: "))
                m = y * 0.9144
                i = y * 36
                f = y * 3
                l = y * 0.000568182
                print("\n{} Yards\n{} Meters\n{} Inches\n{} Feet\n{} Miles\n".format(y,m,i,f,l))
            elif r2 == '5':
                l = float(input("Enter value in miles: "))
                m = l * 1609.344
                i = l * 63360
                f = l * 5280
                y = l * 1760
                print("\n{} Miles\n{} Meters\n{} Inches\n{} Feet\n{} Yards\n".format(l,m,i,f,y))
            elif r2 == '0':
                break
            else:
                print("Input invalid!")
    elif r1 == '4':                                                                                                     #Area Section
        while True:
            print("\nList of Area units: \n1. Square Meters\n2. Hectares\n3. Acers\n4. Square Miles\n0. To Main Menu")
            r2 = input("Enter a number from the area units list: ")
            os.system("cls")
            if r2 == '1':
                m = float(input("Enter value in square meters: "))
                h = m * 0.0001
                a = m * 0.0002471054
                l = m * 0.000000386102159
                print("\n{} square meters\n{} hectares\n{} acers\n{} square miles\n".format(m,h,a,l))
            elif r2 == '2':
                h = float(input("Enter value in hectares: "))
                m = h * 10000
                a = h * 2.4710538
                l = h * 0.00386102159
                print("\n{} hectares\n{} square meters\n{} acers\n{} square miles\n".format(m,h,a,l))
            elif r2 == '3':
                a = float(input("Enter value in acers: "))
                m = a * 0.0015625
                h = a * 0.4046856
                l = a * 0.00386102159
                print("\n{} acers\n{} square meters\n{} hectares\n{} square miles\n".format(a,m,h,l))
            elif r2 == '4':
                l = float(input("Enter value in square miles: "))
                m = l * 2589988.110
                h = l * 258.9988110
                a = l * 640
                print("\n{} square miles\n{} square meters\n{} hectares\n{} acers\n".format(l,m,h,a))
            elif r2 == '0':
                break
            else:
                print("Input invalid!")
    elif r1 == '5':                                                                                                     #Volume Section
        while True:
            print("\nList of Volume units: \n1. Cubic Meters\n2. Liters\n3. Gallons (US)\n0. To Main Menu")
            r2 = input("Enter a number from the volume units list: ")
            os.system("cls")
            if r2 == '1':
                m = float(input("Enter value in cubic meters: "))
                l = m * 1000
                g = m * 264.17205
                print("\n{} cubic meters\n{} liters\n{} gallons (US)\n".format(m,l,g))
            elif r2 == '2':
                l = float(input("Enter value in liters: "))
                m = l * 0.001
                g = l * 0.26417205
                print("\n{} liters\n{} cubic meters\n{} gallons (US)\n".format(l,m,g))
            elif r2 == '3':
                g = float(input("Enter value in gallons (US): "))
                m = g * 0.0037854118
                l = g * 3.7854118
                print("\n{} gallons (US)\n{} cubic meters\n{} liters\n".format(g,m,l))
            elif r2 == '0':
                break
            else:
                print("Input invalid!")
    elif r1 == '0':
        print("Bye, Have a great time....")
        time.sleep(1)
        exit()
    else:
        print("Please enter a valid input.")