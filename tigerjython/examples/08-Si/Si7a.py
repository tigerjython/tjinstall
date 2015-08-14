from gpanel import *
makeGPanel(-1.2, 1.2, -1.2, 1.2)
title("Gausssche Zahlenebene")

z = 0.9 + 0.3j
for n in range(1, 60):
    y = z**n
    draw(y)
fill(0.2, 0, "white", "red")
fill(0.0, 0.2, "white", "green")
drawGrid(-1.0, 1.0, -1.0, 1.0)

