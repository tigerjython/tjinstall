from gpanel import *
import random

def randomColor():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return makeColor(r, g, b)

makeGPanel()
bgColor(randomColor())

for i in range(20):
   setColor(randomColor())
   move(random.random(), random.random())
   a = random.random() / 2
   b = random.random() / 2
   fillEllipse(a, b)

