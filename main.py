#Write a python function named zeroCheck that is given three integers, and returns true if
# any of the integers is 0, otherwise, return False.
def zeroCheck(a1, a2, a3):
    if (a1 * a2 * a3) == 0:
        return True
    else:
        return False
#main program
print('Welcome to zeroCheck')
if zeroCheck(2, 0, 8) == True:
    print('True')
else:
    print('False')
