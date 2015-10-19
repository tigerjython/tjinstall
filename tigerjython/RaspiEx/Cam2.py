# Cam2.py
# Capture transfer and show image, remote mode

from raspibrick import *
from gpanel import *

width = 800
height = 600

robot = Robot()
camera = Camera()
makeGPanel(Size(width, height))
window(0, width, 0, height)
while not isEscapeHit():
   jpeg = camera.captureAndTransfer(width, height)
   img = readImage(jpeg)
   image(img, 0, 0)
robot.exit()
