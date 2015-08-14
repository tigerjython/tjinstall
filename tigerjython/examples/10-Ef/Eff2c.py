from gpanel import *
from math import factorial

z = 100 

def nbCombi(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)

makeGPanel(-5, 55, -1e5, 1.1e6)
drawGrid(0, 50, 0, 1e6, "gray")
setColor("black")
lineWidth(2)
for n in range(2, z + 1):
    sum = 0
    for k in range(1, n):
        sum += nbCombi(n, k)
    print "n =", n, ", nb =", sum
    if n == 2:
        move(n, sum)
    else:
        draw(n, sum)
print "Laufzeit mit 10^9 Operationen pro Sekunde:", sum / 3.142e16, "Jahre" 
print "oder:", int(sum / 2e20), "Mal das Alter des Universums"
