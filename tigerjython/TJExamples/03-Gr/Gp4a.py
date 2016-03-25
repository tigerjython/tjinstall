from gpanel import *
makeGPanel(-25, 25, -25, 25)

def squarenumber(x):
   y = x * x
   return y

for x in range(-5, 6):
   y = squarenumber(x)
   if x == -5:
      move(x, y)
   else:
      draw(x, y)
