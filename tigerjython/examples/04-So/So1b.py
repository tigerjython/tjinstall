from soundsystem import *

samples = getWavMono("bird.wav")
print getWavInfo("mysound.wav")

openMonoPlayer(samples, 44100)
play()

from gpanel import *

makeGPanel(0, len(samples), -33000, 33000)
for i in range(len(samples)):
   draw(i, samples[i])




