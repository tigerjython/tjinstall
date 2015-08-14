from gpanel import *

def translate(pA, pB, pC):
  pA[0] = pA[0] + 5
  pA[1] = pA[1] + 2
  pB[0] = pB[0] + 5
  pB[1] = pB[1] + 2
  pC[0] = pC[0] + 5
  pC[1] = pC[1] + 2

makeGPanel(-10, 10, -10, 10)

a = [0, 0]  
b = [0, 5]
c = [5, 0]
fillTriangle(a, b, c)
translate(a, b, c)
setColor("green")
fillTriangle(a, b, c)
