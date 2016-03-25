from math import sin

def sinc(x):
    y = sin(x) / x
    return y

print sinc("python")
