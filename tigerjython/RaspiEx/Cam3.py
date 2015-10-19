# Cam3.py
# Capture, transfer and show eingepasst in GPanel, remote mode

from raspibrick import *
from gpanel import *

width = 800
height = 600

robot = Robot()
camera = Camera()
makeGPanel(Size(width - 2, height - 2))
window(0, width, 0, height)
while not isEscapeHit():
   jpeg = camera.captureAndTransfer(width, height)
   img = readImage(jpeg)
   image(img, -1, -1)
robot.exit()
