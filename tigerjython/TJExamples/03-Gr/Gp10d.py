from gpanel import *
import random

MAXITERATIONS = 100000
makeGPanel(0, 10, 0, 10)

pA = [1, 1]
pB = [9, 1]
pC = [5, 8]

triangle(pA, pB, pC)
corners = [pA, pB, pC]
pt = [2, 2]

title("Working...")
for iter in range(MAXITERATIONS):
   i = random.randint(0, 2)
   pRand = corners[i]
   pt = getDividingPoint(pRand, pt, 0.5)
   point(pt)
title("Working...Done")



