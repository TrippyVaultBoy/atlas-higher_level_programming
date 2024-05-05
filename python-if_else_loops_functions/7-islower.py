def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{letter} is lower".format(c))
        return True
    else ord(c) >= 65 and ord(c) <= 90:
        print("{letter} is upper".format(c))
        return False
