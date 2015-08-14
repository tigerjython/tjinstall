from gpanel import *

def onMousePressed(x, y):
  if isLeftMouseButton():
      pixColor = getPixelColor(x, y)
      if pixColor == makeColor("white"):
          return
      clear()
      setColor(pixColor)
      move(5, 5)
      fillCircle(2)
      
  if isRightMouseButton():
      for i in range(5):
          move(9, 2 * i + 1)
          if i == 0:
              setColor("deep pink")
          if i == 1:
              setColor("green")
          if i == 2:
              setColor("yellow")
          if i == 3:
              setColor("deep sky blue")
          if i == 4:
              setColor("dark violet")
          fillRectangle(2, 2)

makeGPanel(0, 10, 0, 10, mousePressed = onMousePressed)
move(5, 5)
fillCircle(2)

