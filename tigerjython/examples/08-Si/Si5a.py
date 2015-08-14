from gpanel import *

u = 1 # m/s
v = 20 # m/s
d = 1000  # m
a = 0     # hunter
h = 0     # dog
c = 2 * u / (u + v)
it = 0

makeGPanel(-50, 50, -100, 1100)
title("Hunter-Dog problem")
line(0, 0, 0, 1000)
line(-5, 1000, 5, 1000)
line(-5, 1050, 5, 1050)
line(-5, 1000, -5, 1050)
line(5, 1000, 5, 1050)

while not isDisposed():
    move(0, a)
    fillCircle(1)
    text(5, a, str(int(a)))
    getKeyWait()
    da = c * (d - a)
    dh = 2 * (d  - a) - da
    h += dh
    a += da 
    it += 1
    title("it = " + str(it) + "; hunter = " + str(a) +
          " m; dog = " + str(h) + " m")

