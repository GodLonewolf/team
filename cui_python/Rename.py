import os
path = '1'
while path != '0\\':
    path = input("Enter the path to the folder [0 to exit]: ") + '\\'
    if path == '0\\':
        exit()
    zf = 0
    os.chdir(path)
    files = os.listdir(path)
    autozf = input("Autodetect the number of files? [Y/N]: ")
    if autozf.lower == 'y':
        for i in files:
            print(i)
            zf += 1
    else:
        zf = input("Enter if the files are in 10s, 100s or 1000s: ")
    txt = input("Enter the text to rename the files: ")
    ext = input("Enter an extension (without a '.'): ")
    i = int(input("Enter the starting number: "))
    sep = input("Enter a separator: ")
    r1 = input("1. To add text before numbering\n2. To add numbering before text\nEnter [1/2]: ")
    if r1 == '1':
        for file in files:
            os.rename(path + file, txt + ' {} '.format(sep) + str(i).zfill(len(str(zf))) + '.' + ext)
            i += 1
        print("Renamed!")
    elif r1 == '2':
        for file in files:
            os.rename(path + file, str(i).zfill(len(str(zf))) + ' {} '.format(sep) + txt + '.' + ext)
            i += 1
        print("Renamed")