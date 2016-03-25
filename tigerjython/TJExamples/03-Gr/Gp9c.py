from gpanel import *

BS = 8
SPACE = 32
DEL = 127

def showInfo(key):
    text = "List length = " + str(len(letterList))
    if key != "":
        text += ". Last key code = " + str(ord(key))
    setStatusText(text)  
        
def updateGraphics():
    clear()
    for i in range(len(letterList)):
        text(i, 2, letterList[i], Font("Courier", Font.PLAIN, 24), 
              "blue", "light gray")
    line(cursorPos - 0.2, 1.7, cursorPos - 0.2, 2.7) 

def onMousePressed(e):
    x = toWindowX(e.getX())
    y = toWindowY(e.getY())
    setCursor(x)
    updateGraphics()

def setCursor(x):
    global cursorPos
    pos = int(x + 0.7)
    if pos <= len(letterList):    
       cursorPos = pos

makeGPanel(-1, 30, 0, 12, mousePressed = onMousePressed)

letterList = []
cursorPos = 0
addStatusBar(30)
setStatusText("Enter Text. Backspace to delete. Mouse to set cursor.")
lineWidth(3)

while True:
    delay(10)
    key = getKey()
    if key == "":
        continue
    keyCode = ord(key)
    if keyCode == BS:  # backspace
        if cursorPos > 0:
            cursorPos -= 1
            letterList.pop(cursorPos)
    elif keyCode >= SPACE and keyCode != DEL:      
        letterList.insert(cursorPos, key)
        cursorPos += 1
    updateGraphics()
    showInfo(key)