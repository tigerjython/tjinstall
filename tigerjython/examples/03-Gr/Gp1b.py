from gpanel import *

makeGPanel(0, 20, 0, 20)

setColor("red")
x = 2
y = 2
while y < 20:
   move(x, y)
   fillCircle(1)
   move(x, 20 - y)
   fillRectangle(2, 2)
   x = x + 2
   y = y + 2

