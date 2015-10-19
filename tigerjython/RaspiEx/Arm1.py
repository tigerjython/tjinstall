# Arm1.py
# Remotecontrol: Robot arm

from raspibrick import *
robot = Robot()
camera = Camera()
horzPos = 0
vertPos = 0

while not robot.isEscapeHit():
    doMove = False
    if robot.isDownHit() and vertPos < 100:
        vertPos += 5
        doMove = True
    elif robot.isUpHit() and vertPos > - 100:
        vertPos -= 5
        doMove = True
    elif robot.isLeftHit() and horzPos < 70:
        horzPos += 5
        doMove = True
    elif robot.isRightHit() and horzPos > - 70:
        horzPos -= 5
        doMove = True
    if doMove:
        camera.setPos(horzPos, vertPos)
robot.exit()

