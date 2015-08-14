from gpanel import *

pA = [0, -3]
pB = [5, -3]
pC = [0, 7]
pD = [-5, 7]

makeGPanel(-10, 10, -10, 10)
line(-10, 0, 10, 0)
line(0, -10, 0, 10)

polygon = [0] * 4  # list with 4 elements, initialized with 0
polygon[0] = pA
polygon[1] = pB
polygon[2] = pC
polygon[3] = pD

for i in range(4):
    k = i + 1
    if k == 4:
        k = 0
    line(polygon[i], polygon[k])

