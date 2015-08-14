def exchange(x, y):
    y = x
    x = y
    return x, y

a = 2
b = 3
a, b = exchange(a, b)
print a, b
