for i in range(2,8):
    print("""            elif (u1 == '{}') and (cn{} < 7):
                c{}[cn{}] = '●'
                cn{} += 1
                break""".format(i,i,i,i,i))