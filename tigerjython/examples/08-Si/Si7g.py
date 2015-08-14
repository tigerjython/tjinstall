from gpanel import *
from math import pi

def drawAxis():
   line(-1, 0, 1, 0)  # Real axis
   line(0, -1, 0, 1) # Imaginary axis

makeGPanel(-1.2, 1.2, -1.2, 1.2)
drawGrid(-1.0, 1.0, -1.0, 1.0, "gray")
setColor("black")
drawAxis()
title("Complex gain factor – low pass")

R = 10
C = 0.001
def v(f):
    if f == 0:
        return 1 + 0j
    omega = 2 * pi * f
    XC = 1 / (1j * omega * C)
    return XC / (R + XC)

f = 0 # Frequency
while f <= 100:
    if f == 0:
        move(v(f))
    else:
        draw(v(f))
    if f % 10 == 0:
        text(str(f)) 
    f += 1
    delay(10)
    

