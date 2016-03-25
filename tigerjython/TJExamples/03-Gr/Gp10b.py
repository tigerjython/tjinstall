from gpanel import *
import random

NB_ROLLS = 100

makeGPanel(0, 7, 0, NB_ROLLS)
title("# Rolls: " + str(NB_ROLLS))
setColor("red")
line(0, NB_ROLLS / 6, 7, NB_ROLLS / 6)
setColor("blue")
line(0, 0, 7, 0)
for n in range(1, 7):
   text(n + 0.1, 0.1, str(n))

histo = [0, 0, 0, 0, 0, 0, 0]
# hist = [0] * 7  # short form

for i in range(NB_ROLLS):
   pip = random.randint(1, 6)
   histo[pip] += 1

lineWidth(10)
for n in range(1, 7):
   line(n, 0, n, histo[n])
