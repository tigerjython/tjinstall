from soundsystem import *

samples = getWavMono("mysound.wav")
soundlist = []
for item in samples:
  soundlist.append(item // 4)

openMonoPlayer(soundlist, 22010)
play()


