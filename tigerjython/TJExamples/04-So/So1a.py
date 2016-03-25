from soundsystem import *

samples = getWavMono("mysound.wav")
print getWavInfo("mysound.wav")

openMonoPlayer(samples, 44100)
play()
