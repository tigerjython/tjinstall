from sys import exit
from math import sin

def sinc(x):
    try:
        if x == 0:
            return 1.0
        y = sin(x) / x
    except TypeError:
        print "Error in sinc(x). x =", x, "is not a number"
        exit()
    return y

print sinc("python")
