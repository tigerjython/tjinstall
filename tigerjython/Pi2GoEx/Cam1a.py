# Cam1a.py
# Capture and store on Raspi, remote and autonomous mode

from raspibrick import *

robot = Robot()
camera = Camera()
print "Capturing and storing on remote..."
filename = "/home/pi/shot1.jpg"
jpeg = camera.captureAndSave(200, 100, filename)
print "Capture to remote:", filename
robot.exit()
