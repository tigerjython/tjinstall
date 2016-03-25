def exchange(x, y):
    x, y = y, x
    return x, y

a = 2
b = 3
a, b = exchange(a, b)
print a, b
