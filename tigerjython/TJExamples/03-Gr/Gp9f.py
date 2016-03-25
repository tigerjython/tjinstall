from gpanel import *

makeGPanel(-10, 10, -10, 10)

a = [0, 0]  
a_alias = a
b = [0, 5]
c = [5, 0]

fillTriangle(a, b, c)
a[0] = 1
setColor("green")
fillTriangle(a_alias, b, c)

