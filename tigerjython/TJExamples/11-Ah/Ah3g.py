def exchange(x, y):
    print "exchange() with params", x, y
    temp = y
    y = x
    x = temp
    print "exchange() returning", x, y
    return x, y

a = 2
b = 3
a, b = exchange(a, b)
print a, b
