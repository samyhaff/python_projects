for i in range(0, 100):
    if i % 11 == 0:
        fin = " \n"
    else:
        fin = ' '
    print("{:3}".format(str(i)), end = fin )