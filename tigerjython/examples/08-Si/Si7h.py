from gpanel import *
import math
import cmath

R = 10
C = 0.001

def v(f):
    if f == 0:
        return 1 + 0j
    omega = 2 * math.pi * f
    XC = 1 / (1j * omega * C)
    return XC / (R + XC)

p1 = GPanel(-10, 110, -0.1, 1.1)
drawPanelGrid(p1, 0, 100, 0, 1.0, "gray")
p1.title("Bode Plot - Low Pass, Gain")
p1.setColor("blue")
f = 0
while f <= 100:
    if f == 0:
        p1.move(f, abs(v(f)))
    else:
        p1.draw(f, abs(v(f)))
    f += 1

p2 = GPanel(-10, 110, 9, -99)
drawPanelGrid(p2, 0, 100, 0, -90, 10, 9, "gray")
p2.title("Bode Plot - Low Pass, Phase")
p2.setColor("red")
f = 0
while f <= 100:
    if f == 0:
        p2.move(f, math.degrees(cmath.phase(v(f))))
    else:
        p2.draw(f, math.degrees(cmath.phase(v(f))))
    f += 1    