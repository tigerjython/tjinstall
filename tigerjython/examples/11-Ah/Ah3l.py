from math import sin

def sinc(x):
    try:
        if x == 0:
            return 1.0
        y = sin(x) / x
    except TypeError:
        return None
    return y

y = sinc("python")
if y == None:
   print "Illegal call"
else:
   print y
