
from math import sin
def sinc(x):
    assert isinstance(x, (int, long, float)), "Error in sinc(x). x not a number"
    y = sin(x) / x
    return y

print sinc(2.0)
