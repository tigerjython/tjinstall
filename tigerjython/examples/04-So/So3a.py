from soundsystem import *

openMonoRecorder(22050)
print("Recording...");
capture()
delay(5000)
stopCapture()
print("Stopped");
sound = getCapturedSound()

openMonoPlayer(sound, 22050)
play()


