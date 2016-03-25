from soundsystem import *
from gpanel import *

samples = getWavMono("mysound.wav")

makeGPanel(0, len(samples), -33000, 33000)
for i in range(len(samples)):
   if i == 0:
      move(i, samples[i] + 10000)
   else:
      draw(i, samples[i] + 10000)

for i in range(len(samples)):
   samples[i] = samples[i] // 4

for i in range(len(samples)):
   if i == 0:
      move(i, samples[i] - 10000)
   else:
      draw(i, samples[i] - 10000)

