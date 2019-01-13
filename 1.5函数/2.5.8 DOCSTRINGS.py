# docstrings
def printMax2(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # convert to integers, if possible
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


printMax2(3, 5)
print(printMax2.__doc__)