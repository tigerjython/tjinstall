from soundsystem import *

openMonoRecorder(22050)
print("Recording...");
capture()
delay(5000)
stopCapture()
print("Stopped");
sound = getCapturedSound()

from gpanel import *
makeGPanel(0, len(sound), -33000, 33000)
for i in range(len(sound)):
   draw(i, sound[i])


