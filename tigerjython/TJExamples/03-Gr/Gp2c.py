from gpanel import *

makeGPanel(0, 40, 0, 40)

setColor("red")
y = 1
for i in range(2, 41, 2):
   move(20, y)
   fillRectangle(i, 1.5)
   y = y + 2 


