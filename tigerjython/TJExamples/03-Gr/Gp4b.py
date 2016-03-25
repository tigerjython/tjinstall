from gpanel import *

def squarenumber(x):
    y = x * x
    return y

makeGPanel(-25, 25, -25, 25)

# draw coordinate system
line(-25, 0, 25, 0) # x axis
line(0, -25, 0, 25) # y axis

x  = -5
while x < 5:
    y = squarenumber(x)
    if x == -5:
        move(x, y)
    else:
        draw(x, y)
    x = x + 0.01
