# Cam1.py
# Capture and transfer, remote mode

from raspibrick import *


robot = Robot()
camera = Camera()
print "Capturing and transferring in JPEG format now..."
jpeg = camera.captureAndTransfer(640, 480)
print "Capture image size:", len(jpeg)
print "Saving it in local file space"
camera.saveData(jpeg, "c:/scratch/aplux.jpg")
robot.exit()
