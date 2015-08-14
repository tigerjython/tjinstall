def exchange(x, y):
    if debug: print "exchange() with params", x, y
    temp = y
    y = x
    x = temp
    if debug: print "exchange() returning", x, y
    return x, y

debug = False
a = 2
b = 3
a, b = exchange(a, b)
print a, b
