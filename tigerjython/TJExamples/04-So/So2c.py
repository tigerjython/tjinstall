from soundsystem import *

samples = []
for i in range(4 * 5000):
  value = 5000
  if i % 10 == 0:
     value = -value
  samples.append(value)

openMonoPlayer(samples, 5000)
play()


